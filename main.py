from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Функция для отправки ключа
async def send_key(update: Update, context: CallbackContext) -> None:
    your_key = "ваш_ключ"  # Здесь вместо 'ваш_ключ' может быть ваш реальный ключ
    await update.callback_query.message.reply_text(f'Ваш ключ: {your_key}')

# Функция для отправки ссылки для оплаты
async def send_payment_link(update: Update, context: CallbackContext) -> None:
    payment_link = "ссылка_для_оплаты"  # Здесь замените на реальную ссылку для оплаты
    await update.callback_query.message.reply_text(f'Ссылка для пополнения: {payment_link}')

# Функция для отправки приветственного сообщения с кнопками
async def start_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Получить ключ", callback_data="get_key"),
            InlineKeyboardButton("Пополнить", callback_data="replenish")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        'Привет! Нажмите кнопку ниже, чтобы получить ключ или пополнить баланс.',
        reply_markup=reply_markup
    )

# Обработчик команды /start и нажатий кнопок
async def handle_button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Подтверждение нажатия кнопки
    
    if query.data == "get_key":
        await send_key(update, context)  # Передаем update
    elif query.data == "replenish":
        await send_payment_link(update, context)  # Передаем update

def main():
    # Ваш токен здесь
    TOKEN = '7707653021:AAH4vn2HBSCp0KXc2erc2aMvuZHv27tSOwo'
    
    app = Application.builder().token(TOKEN).build()

    # Обработчики
    app.add_handler(CommandHandler('start', start_command))  # Обработка команды /start
    app.add_handler(CallbackQueryHandler(handle_button_click))  # Обработка нажатий кнопок

    app.run_polling()

if __name__ == '__main__':
    main()
