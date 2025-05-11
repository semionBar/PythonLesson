from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Функция для отправки ключа
async def send_key(update: Update, context: CallbackContext) -> None:
    your_key = "ваш_ключ"  # Здесь вместо 'ваш_ключ' может быть ваш реальный ключ
    await update.message.reply_text(f'Ваш ключ: {your_key}')

# Функция для обработки текстовых сообщений
async def reply_hello(update: Update, context: CallbackContext) -> None:
    # Создаем клавиатуру с кнопкой "Получить ключ"
    keyboard = [
        ["Получить ключ"]  # Кнопка "Получить ключ"
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text('Привет! Нажмите кнопку ниже, чтобы получить ключ.', reply_markup=reply_markup)

# Обработчик нажатия на кнопку
async def handle_button(update: Update, context: CallbackContext) -> None:
    # Проверяем, какое сообщение пришло
    if update.message.text == "Получить ключ":
        await send_key(update, context)

def main():
    # Ваш токен здесь
    TOKEN = 'YOUR_TOKEN'
    
    app = Application.builder().token(TOKEN).build()

    # Обработчики
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex("Получить ключ"), reply_hello))  # Обрабатывает сообщения, кроме "Получить ключ"
    app.add_handler(MessageHandler(filters.TEXT, handle_button))  # Обработка нажатий кнопок

    app.run_polling()

if __name__ == '__main__':
    main()
