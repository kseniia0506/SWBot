import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("7507013882:AAFnuZ893lkQNOTKfGRF04n-8rMy5DiJlis")

def delete_message(update: Update, context: CallbackContext):
    """Удаляет все входящие сообщения."""
    try:
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        print(f"Ошибка: {e}")

def start(update: Update, context: CallbackContext):
    """Ответ на команду /start."""
    update.message.reply_text("Бот активен и удаляет все сообщения!")

def main():
    """Запускает бота."""
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    # Обработка команды /start
    dp.add_handler(CommandHandler("start", start))

    # Обработка всех входящих сообщений
    dp.add_handler(MessageHandler(Filters.all, delete_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
