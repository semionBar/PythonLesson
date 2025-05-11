from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Функция для отправки ключа
async def send_key(update: Update, context: CallbackContext) -> None:
    your_key = "ваш_ключ"  # Здесь вместо 'ваш_ключ' может быть ваш реальный ключ
    await update.message.reply_text(f'Ваш ключ: {your_key}')

# Функция для отправки ссылки для оплаты
async def send_payment_link(update: Update, context: CallbackContext) -> None:
    payment_link = "ссылка_для_оплаты"  # Здесь замените на реальную ссылку для оплаты
    await update.message.reply_text(f'Ссылка для пополнения: {payment_link}')

# Функция для обработки текстовых сообщений
async def reply_hello(update: Update, context: CallbackContext) -> None:
    # Создаем клавиатуру с кнопками "Получить ключ" и "Пополнить"
    keyboard = [
        ["Получить ключ", "Пополнить"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text('Привет! Нажмите кнопку ниже, чтобы получить ключ или пополнить баланс.', reply_markup=reply_markup)

# Обработчик нажатия на кнопку "Получить ключ"
async def handle_key_button(update: Update, context: CallbackContext) -> None:
    await send_key(update, context)

# Обработчик нажатия на кнопку "Пополнить"
async def handle_payment_button(update: Update, context: CallbackContext) -> None:
    await send_payment_link(update, context)

def main():
    # Ваш токен здесь
    TOKEN = '7707653021:AAH4vn2HBSCp0KXc2erc2aMvuZHv27tSOwo'
    
    app = Application.builder().token(TOKEN).build()

    # Обработчики
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex("Получить ключ|Пополнить"), reply_hello))  # Обработка сообщений для приветствия
    app.add_handler(MessageHandler(filters.Regex("Получить ключ"), handle_key_button))  # Обработка нажатий кнопки "Получить ключ"
    app.add_handler(MessageHandler(filters.Regex("Пополнить"), handle_payment_button))  # Обработка нажатий кнопки "Пополнить"

    app.run_polling()

if __name__ == '__main__':
    main()