from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)

responses = [
    ([
        "привет", "приветствую", "здравствуйте", "хай", "хелло", "здрасьте",
        "добрый день", "добрый вечер", "доброе утро"
    ],
     "Здравствуйте"),

    ([
        "цена", "цены", "стоимость", "сколько",
        "какая цена", "сколько стоит", "какая стоимость", "по чем", "почем"
    ],
     "Информацию о стоимости и актуальном наличии товаров просьба уточнять непосредственно в интересующем магазине.\n\nКарта магазинов BlackTab — https://blacktab.ru/map"),

    ([
        "доставка", "отправите", "заказать", "купить", "приобрести"
    ],
     "К сожалению, мы не осуществляем доставку. По законодательству РФ доставка никотиносодержащей продукции запрещена.")
]


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for keywords, response in responses:
        for key in keywords:
            if key in text:
                await update.message.reply_text(response)
                return


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
