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
