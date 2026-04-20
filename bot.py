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
        "Магазины BlackTab — https://blacktab.ru/map"
    ),
]


# 📌 ГЛАВНОЕ МЕНЮ (НОВЫЙ ПОРЯДОК 1–9)
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📃 Правила", callback_data="rules")],

        [InlineKeyboardButton("💳 Цена/Наличие", callback_data="price")],

        [
            InlineKeyboardButton("📍 Магазины", url="https://blacktab.ru/map"),
            InlineKeyboardButton("📦 Доставки нет", callback_data="delivery")
        ],

        [
            InlineKeyboardButton("❓ Обратная связь", callback_data="help"),
            InlineKeyboardButton("🏢 Франшиза", url="https://franchise.blacktab.ru")
        ],

        [
            InlineKeyboardButton("🌐 Сайт", url="https://blacktab.ru"),
            InlineKeyboardButton("📱 ВК", url="https://vk.com/Blacktab_official"),
            InlineKeyboardButton("▶️ YouTube", url="https://www.youtube.com/@Blacktab_official")
        ]
    ])


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


# 👋 Приветствие
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Добро пожаловать в BlackTab, {user.first_name}! 👋\n\nОбратите внимание: ниже приведены все сведения, которые могут быть вам полезны.\nПожалуйста, ознакомьтесь с правилами чата"


# 🔘 Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "rules":
        await query.edit_message_text(
            "Доводим до вашего сведения: вся информация в сообществе носит ознакомительный характер.\n\n"
            "Вступая в «BlackTab», вы подтверждаете, что достигли 18-летнего возраста.\n\n"
            "📃 Общие правила:\n"
            "• Соблюдайте уважение к другим участникам.\n"
            "• Избегайте провокаций и не участвуйте в конфликтах.\n\n"
            "❗️ Нарушения:\n"
            "• Спам и флуд.\n"
            "• Реклама.\n"
            "• Оскорбления и нецензурная лексика.\n"
            "• Разжигание ненависти (в том числе по политическим мотивам).\n"
            "• Введение в заблуждение.\n"
            "• Продажа или обмен товарами.\n"
            "• 18+ контент.\n"
            "• Дискриминация по любым признакам (раса, пол, возраст, религия, профессия, ориентация и т.д.).\n\n"
            "Участник, нарушивший правила, будет заблокирован без возможности восстановления доступа к каналу/чату!",
            reply_markup=back_button()
        )

    elif data == "price":
        await query.edit_message_text(
            "Информацию о стоимости и актуальном наличии товаров просьба уточнять непосредственно в интересующем магазине.\n\n"
            "Карта магазинов BlackTab — https://blacktab.ru/map",
            reply_markup=back_button()
        )

    elif data == "shops":
        await query.edit_message_text("Магазины BlackTab — https://blacktab.ru/map", reply_markup=back_button())

    elif data == "delivery":
        await query.edit_message_text(
            "К сожалению, мы не осуществляем доставку. По законодательству РФ доставка никотиносодержащей продукции запрещена.",
            reply_markup=back_button()
        )

    elif data == "help":
        await query.edit_message_text("Обратная связь: otzyv@blacktab.ru", reply_markup=back_button())

    elif data == "franchise":
        await query.edit_message_text(
            "По вопросам франшизы: franchise@blacktab.ru или 8 (800) 222-15-05 (доб. 3)",
            reply_markup=back_button()
        )

    elif data == "site":
        await query.edit_message_text("Сайт компании: https://blacktab.ru", reply_markup=back_button())

    elif data == "vk":
        await query.edit_message_text("Сообщество ВКонтакте: https://vk.com/Blacktab_official", reply_markup=back_button())

    elif data == "youtube":
        await query.edit_message_text(
            "YouTube канал: https://www.youtube.com/@Blacktab_official",
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

app.run_polling()
