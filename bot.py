from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CallbackQueryHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

responses = [
    (
        ["привет", "здравствуйте", "хай"],
        "Здравствуйте😇"
    ),
]

# ---------------- МЕНЮ ----------------
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📜 Правила", callback_data="rules")],
        [InlineKeyboardButton("📍 Магазины", callback_data="shops")],
        [InlineKeyboardButton("❓ Помощь", callback_data="help")]
    ])


def back_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])


# ---------------- СООБЩЕНИЯ ----------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for keywords, response in responses:
        for key in keywords:
            if key in text:
                await update.message.reply_text(response)
                return


# ---------------- ПРИВЕТСТВИЕ ----------------
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Добро пожаловать, {user.first_name}! 👋",
            reply_markup=main_menu()
        )


# ---------------- КНОПКИ ----------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "rules":
        await query.edit_message_text(
            "📜 Правила:\n- Без спама\n- Уважение",
            reply_markup=back_menu()
        )

    elif data == "shops":
        await query.edit_message_text(
            "📍 Магазины: https://blacktab.ru/map",
            reply_markup=back_menu()
        )

    elif data == "help":
        await query.edit_message_text(
            "❓ Поддержка: otzyv@blacktab.ru",
            reply_markup=back_menu()
        )

    elif data == "back":
        await query.edit_message_text(
            "Главное меню:",
            reply_markup=main_menu()
        )


# ---------------- ЗАПУСК ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
