import logging
from GigaChatAPI import GigaChatAPI
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler

TELEGRAM_BOT_TOKEN = '7170378925:AAER0ESqjDFp_DSqQwk51g3Ag_okEDVwwDw'

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния для ConversationHandler
CHOOSING, TYPING_REPLY = range(2)

gigachat = GigaChatAPI()


async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Привет! Пожалуйста, выбери тему, по которой ты хочешь общаться."
    )
    return CHOOSING

async def start_error(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Тема уже задана. Можете задавать вопросы. Если хотите сменить тему введите /change_topic."
    )
    return CHOOSING


async def received_information(update: Update, context: CallbackContext) -> int:
    user_text = update.message.text
    context.user_data['theme'] = user_text

    await update.message.reply_text(
        f"Тема {user_text}. Ищу документы по теме"
    )

    # Кормим документы нейронке (здесь примерный код, так как конкретная реализация зависит от вашей нейронной сети)
    gigachat.set_topic(user_text)

    await update.message.reply_text(
        f"Документы по теме '{user_text}' загружены. Ты можешь начать общение по этой теме."
    )
    return TYPING_REPLY


async def handle_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text

    processing_message = await update.message.reply_text("Пожалуйста, подождите немного. Ваш запрос обрабатывается.")

    # Обработка запроса нейросетью с учетом документов
    response = gigachat.process_question(user_text)

    # Отправка окончательного ответа
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def change_topic(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "Пожалуйста, выбери новую тему, по которой ты хочешь общаться."
    )
    return CHOOSING


def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(filters.TEXT & ~filters.COMMAND, received_information)],
            TYPING_REPLY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)],
        },
        fallbacks=[CommandHandler('change_topic', change_topic), CommandHandler('start', start_error)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("change_topic", change_topic))

    application.run_polling()


if __name__ == '__main__':
    main()
