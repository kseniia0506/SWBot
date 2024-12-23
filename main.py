from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# Функция для обработки текстовых сообщений
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:  # Проверяем, существует ли сообщение
        try:
            await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        except Exception as e:
            print(f"Ошибка удаления сообщения: {e}")

def main():
    # Укажите ваш токен бота
    BOT_TOKEN = "7507013882:AAFnuZ893lkQNOTKfGRF04n-8rMy5DiJlis"

    # Создайте приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавление обработчика для текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
