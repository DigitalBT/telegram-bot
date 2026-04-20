from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters, CallbackQueryHandler, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)


responses = [
    (
        ["привет", "приветствую", "здравствуйте", "хай", "хелло", "здрасьте",
         "добрый день", "добрый вечер", "доброе утро"],
        "<b>Здравствуйте! 😇</b>"
    ),

    (
        ["сотрудничество", "сотрудничать"],
        "📩 <b>Сотрудничество</b>\n\nНапишите на почту:\n<code>info@blacktab.ru</code>"
    ),

    (
        ["цена", "стоимость", "сколько", "наличие"],
        "💳 <b>Цена и наличие</b>\n\n"
        "Уточняйте актуальную информацию <i>в магазине</i>.\n\n"
        "📍 <a href='https://blacktab.ru/map'>Открыть карту магазинов</a>"
    ),

    (
        ["доставка", "заказать", "купить"],
        "📦 <b>Доставка</b>\n\n"
        "Мы <b>не осуществляем доставку</b>.\n"
        "<i>По законодательству РФ это запрещено.</i>"
    ),

    (
        ["трудоустройство", "вакансия"],
        "👨‍💼 <b>Работа</b>\n\n"
        "📞 8 (800) 222-15-05 (доб. 2)"
    ),

    (
        ["франшиза"],
        "🏢 <b>Франшиза</b>\n\n"
        "📩 <code>franchise@blacktab.ru</code>\n"
        "📞 8 (800) 222-15-05 (доб. 3)"
    ),

    (
        ["жалоба", "возврат"],
        "❗ <b>Обратная связь</b>\n\n"
        "📩 <code>otzyv@blacktab.ru</code>"
    ),

    (
        ["ассортимент"],
        "🙏 Спасибо за отзыв!\n\nМы <b>постоянно расширяем ассортимент</b>."
    ),

    (
        ["открыт"],
        "📍 <a href='https://blacktab.ru/map'>Смотреть магазины</a>"
    ),
]


# 📌 МЕНЮ
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📃 Правила", callback_data="rules")],
        [InlineKeyboardButton("💳 Цена/Наличие", callback_data="price")],
        [
            InlineKeyboardButton("📍 Магазины", url="https://blacktab.ru/map"),
            InlineKeyboardButton("📦 Доставка", callback_data="delivery")
        ],
        [
            InlineKeyboardButton("❓ Обратная связь", callback_data="help"),
            InlineKeyboardButton("🏢 Франшиза", callback_data="franchise")
        ],
        [
            InlineKeyboardButton("🌐 Сайт", url="https://blacktab.ru"),
            InlineKeyboardButton("📱 ВК", url="https://vk.com/Blacktab_official"),
            InlineKeyboardButton("▶️ YouTube", url="https://www.youtube.com/@Blacktab_official")
        ]
    ])


def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ])


# 🚀 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"<b>Привет, {user.first_name}! 👋</b>\n\n"
        "Добро пожаловать в <b>BlackTab</b>\n\n"
        "<i>Выберите, что вас интересует 👇</i>",
        reply_markup=main_menu(),
        parse_mode="HTML"
    )


# 💬 сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for keywords, response in responses:
        for key in keywords:
            if key in text:
                await update.message.reply_text(
                    response,
                    reply_markup=main_menu(),
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return

    # если не понял
    await update.message.reply_text(
        "🤔 Не совсем понял вопрос.\n\nВыберите вариант ниже 👇",
        reply_markup=main_menu()
    )


# 👋 приветствие в чате
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Добро пожаловать, {user.first_name}! 👋",
            reply_markup=main_menu()
        )


# 🔘 кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "rules":
        text = (
            "<b>📃 Правила</b>\n\n"
            "Только для лиц <b>18+</b>\n\n"
            "<b>❌ Запрещено:</b>\n"
            "• Спам\n• Оскорбления\n• Реклама\n\n"
            "<i>Нарушение = блокировка</i>"
        )

    elif data == "price":
        text = (
            "💳 <b>Цена и наличие</b>\n\n"
            "Уточняйте в магазине 👇\n\n"
            "<a href='https://blacktab.ru/map'>Открыть карту</a>"
        )

    elif data == "delivery":
        text = (
            "📦 <b>Доставка</b>\n\n"
            "Мы не доставляем товары.\n"
            "<i>Запрещено законом РФ</i>"
        )

    elif data == "help":
        text = "📩 <b>Связь:</b>\n<code>otzyv@blacktab.ru</code>"

    elif data == "franchise":
        text = (
            "🏢 <b>Франшиза</b>\n\n"
            "<code>franchise@blacktab.ru</code>\n"
            "📞 8 (800) 222-15-05"
        )

    elif data == "back":
        await query.edit_message_text(
            "Выберите раздел 👇",
            reply_markup=main_menu()
        )
        return

    else:
        return

    await query.edit_message_text(
        text,
        reply_markup=back_button(),
        parse_mode="HTML",
        disable_web_page_preview=True
    )


# 🚀 запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
