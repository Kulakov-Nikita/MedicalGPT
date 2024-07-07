from langchain.chat_models.gigachat import GigaChat
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from langchain_community.embeddings.gigachat import GigaChatEmbeddings
from langchain.chains import RetrievalQA
from langchain.schema import HumanMessage
from pdfminer.high_level import extract_text
import requests
import urllib
import re
import io


class GigaChatAPI:
    def __init__(self, path: str = "tmp.txt", limit: int = 3):
        self.llm = GigaChat(
            credentials="NWM1MDQxOWYtNzk0Yi00NzI4LTkxNTctNTY5YWFjYzcyM2MxOjc3MGVmZTdiLTYzNzUtNGE3OC1iN2Y0LTU5ODNiNWJjYWZjNQ==",
            verify_ssl_certs=False)
        self.path: str = path
        self.qa_chain = None
        self.limit: int = limit

    def set_topic(self, topic: str) -> None:
        keywords = self.extract_keywords(topic)
        self.getPDFs(keywords)
        self.vectorise_data()

    def set_limits(self, limit: int = 3):
        self.limit = limit

    def extract_keywords(self, user_input: str) -> list:
        question = f"Выдели ключевые слова, необходимые для поиска медицинских документов для ответа на вопросы по этой теме: '{user_input}'. Перечисли слова через запятую."
        text = self.llm([HumanMessage(content=question)]).content[0:200]
        pattern = r'"(.*?)"'
        matches = re.findall(pattern, text)
        return matches

    def get_links(self, keyword: str) -> tuple[list, int]:
        f = {"q": keyword, "type": "clinical", "offset": "0", "limit": f"{self.limit}"}
        url = "https://demo.onco-reg.ru/docs/api?" + urllib.parse.urlencode(f)
        answer = requests.get(url).json()
        number_of_pdf: int = int(answer['result']['total'])
        return [doc['link'] for doc in answer['result']['documents']], number_of_pdf

    def getPDFs(self, keywords: list) -> None:
        links = set()
        for keyword in keywords:
            x, y = self.get_links(keyword=keyword)
            for link in x:
                links.add(link)

        PDFs = '\n'.join([extract_text(io.BytesIO(requests.get(link).content)) for link in links])

        with open(self.path, 'w+', encoding='utf-8') as file:
            file.write(PDFs)

    def vectorise_data(self) -> None:
        loader = TextLoader(self.path, encoding='utf-8')
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        documents = text_splitter.split_documents(documents)
        embeddings = GigaChatEmbeddings(
            credentials="NWM1MDQxOWYtNzk0Yi00NzI4LTkxNTctNTY5YWFjYzcyM2MxOjc3MGVmZTdiLTYzNzUtNGE3OC1iN2Y0LTU5ODNiNWJjYWZjNQ==",
            verify_ssl_certs=False
        )
        db = Chroma.from_documents(
            documents,
            embeddings,
            client_settings=Settings(anonymized_telemetry=False),
        )
        self.qa_chain = RetrievalQA.from_chain_type(self.llm, retriever=db.as_retriever())

    def process_question(self, question: str) -> str:
        return self.qa_chain({"query": question})['result']
