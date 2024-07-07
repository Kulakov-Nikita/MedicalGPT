from langchain.chat_models.gigachat import GigaChat
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from langchain_community.embeddings.gigachat import GigaChatEmbeddings
from langchain.schema import HumanMessage
import urllib
import requests
import re
from pdfminer.high_level import extract_text
import io

llm = GigaChat(credentials="NWM1MDQxOWYtNzk0Yi00NzI4LTkxNTctNTY5YWFjYzcyM2MxOjc3MGVmZTdiLTYzNzUtNGE3OC1iN2Y0LTU5ODNiNWJjYWZjNQ==", verify_ssl_certs=False)

def extract_keywords(user_input: str) -> list:
    question = "У меня на правой ягодице пятно зеленого цвета."
    question = f"Выдели ключевые слова, необходимые для поиска медицинских документов для ответа на вопросы по этой теме: '{question}'. Перечисли слова через запятую."
    text = llm([HumanMessage(content=question)]).content[0:200]
    pattern = r'"(.*?)"'
    matches = re.findall(pattern, text)
    return matches

def get_links(keyword: str, limit: int = 3) -> tuple[list, int]:
    f = {"q":keyword,"type":"clinical", "offset":"0", "limit":f"{limit}"}
    url = "https://demo.onco-reg.ru/docs/api?" + urllib.parse.urlencode(f)
    answer = requests.get(url).json()
    number_of_pdf: int = int(answer['result']['total'])
    return [doc['link'] for doc in answer['result']['documents']], number_of_pdf

        
def getPDFs(keywords: list) -> None:
    links = set()
    for keyword in keywords:
        x, y = get_links(keyword=keyword)
        for link in x:
            links.add(link)

    PDFs = '\n'.join([extract_text(io.BytesIO(requests.get(link).content)) for link in links])

    with open("tmp.txt", 'w+', encoding='utf-8') as file:
        file.write(PDFs)