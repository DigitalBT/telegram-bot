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

    (
        [
            "сотрудничество", "сотрудничать", "по сотрудничеству", "сотрудничества", "сотрудничестве"
        ],
        "По вопросам сотрудничества, вы можете обратиться на почту info@blacktab.ru"
    ),

    (
        [
            "цена", "цены", "стоимость", "сколько",
            "какая цена", "сколько стоит", "какая стоимость", "по чем", "почем",
            "есть", "в наличии", "наличие", "наличия", "наличий",
            "поступление", "поступит", "поступили"
        ],
        "Информацию о стоимости и актуальном наличии товаров просьба уточнять непосредственно в интересующем магазине.\n\nКарта магазинов BlackTab — https://blacktab.ru/map"
    ),

    (
        [
            "доставка", "отправите", "заказать", "купить", "приобрести"
        ],
        "К сожалению, мы не осуществляем доставку. По законодательству РФ доставка никотиносодержащей продукции запрещена."
    ),

    (
        [
            "трудоустройство", "вакансия", "вакансии", "отдел кадров"
        ],
        "По вопросам трудоустройства, вы можете обратиться по номеру 8 (800) 222-15-05 (доб. 2)"
    ),

    (
        [
            "франшиза", "франчайзинг", "франчайзи"
        ],
        "По вопросам франшизы, вы можете обратиться на почту franchise@blacktab.ru или по номеру 8 (800) 222-15-05 (доб. 3)"
    ),

    (
        [
            "жалоба", "возврат", "обмен", "поменять"
        ],
        "По вопросам жалоб и предложений, вы можете обратиться на почту otzyv@blacktab.ru"
    ),

    (
        [
            "маленький ассортимент", "нет выбора", "мало выбора"
        ],
        "Благодарим за Ваш отзыв! Мы постоянно обновляем ассортимент."
    ),

    (
        [
            "открыт", "открыто"
        ],
        "Магазины BlackTab на Яндекс Картах — https://yandex.com/maps/213/moscow/chain/blacktab/41361998584"
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


def back_button():
    keyboard = [
        [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)


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


# 🔘 КНОПКИ + НАВИГАЦИЯ
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "rules":
        await query.edit_message_text(
            "📜 Правила:\n\n"
            "1. Уважайте участников\n"
            "2. Без спама\n"
            "3. Без рекламы",
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


# 🚀 ЗАПУСК БОТА
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for keywords, response in responses:
        for key in keywords:
            if key in text:
                await update.message.reply_text(response)
                return


# 👋 Приветствие с кнопками
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📜 Правила", callback_data="rules")],
        [InlineKeyboardButton("📍 Магазины", callback_data="shops")],
        [InlineKeyboardButton("❓ Помощь", callback_data="help")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Добро пожаловать в BlackTab, {user.first_name}! 👋\n\nВыберите, что вас интересует:",
            reply_markup=reply_markup
        )


# 🔘 Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "rules":
        await query.edit_message_text("📜 Правила: уважайте участников, без спама и рекламы.")

    elif data == "shops":
        await query.edit_message_text("📍 Магазины: https://blacktab.ru/map")

    elif data == "help":
        await query.edit_message_text("❓ Поддержка: otzyv@blacktab.ru")


# 🚀 Запуск бота
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
