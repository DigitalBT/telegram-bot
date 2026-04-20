from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CallbackQueryHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

responses = [
    (
        [
            "привет", "приветствую", "здравствуйте", "хай", "хелло", "здрасьте",
            "добрый день", "добрый вечер", "доброе утро"
        ],
        "Здравствуйте😇"
    ),
]


# 📌 ГЛАВНОЕ МЕНЮ
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📜 Правила", callback_data="rules")],
        [InlineKeyboardButton("📍 Магазины", callback_data="shops")],
        [InlineKeyboardButton("❓ Помощь", callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)


# 📌 КНОПКА НАЗАД
def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])


# 💬 Обычные сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for keywords, response in responses:
        for key in keywords:
            if key in text:
                await update.message.reply_text(response)
                return


# 👋 Приветствие с меню
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Добро пожаловать в BlackTab, {user.first_name}! 👋\n\nВыберите, что вас интересует:",
            reply_markup=main_menu()
        )


# 🔘 Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "rules":
        await query.edit_message_text(
            "📜 Правила:\n\n"
            "• Уважайте участников\n"
            "• Без спама\n"
            "• Без рекламы",
            reply_markup=back_button()
        )

    elif data == "shops":
        await query.edit_message_text(
            "📍 Магазины:\nhttps://blacktab.ru/map",
            reply_markup=back_button()
        )

    elif data == "help":
        await query.edit_message_text(
            "❓ Поддержка: otzyv@blacktab.ru",
            reply_markup=back_button()
        )

    elif data == "back":
        await query.edit_message_text(
            "Выберите, что вас интересует:",
            reply_markup=main_menu()
        )


# 🚀 Запуск бота
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
