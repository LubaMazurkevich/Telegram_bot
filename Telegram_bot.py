import telebot

bot=telebot.TeleBot("1905760075:AAEnumTrfQDsy9dD4bmapBnZkJos2IF7Xgo")
import datetime
spisok_stolov = [7, 7, 6, 6, 3, 6, 6, 2, 7, 3, 7, 6, 6, 4, 5, 4, 5, 4,
                 3, 1, 6, 7, 6, 7, 2, 1, 3, 7, 6, 2, 7, 1, 3, 7, 1, 2,
                 6, 7, 7, 6, 4, 5, 4, 4, 6, 2, 5, 7, 4, 4, 3, 4, 4, 2, 1]
dct={}
spisok_gostey = ['Атрашкевич Александр', 'Атрашкевич Людмила', 'Бондарик Никита', 'Васютович Кирилл', 'Веселко Сергей',
                 'Волнистая Ксения', 'Гедимин Валерий', 'Гедимин Виталий', 'Гедимин Лариса', 'Гедимин Мария',
                 'Гедимин Наталья',
                 'Грамыко Дмитрий', 'Грамыко Ольга', 'Демидюк Дмитрий', 'Демидюк Карина', 'Демидюк Наталья',
                 'Демидюк Тимур', 'Кишкурно Татьяна',
                 'Ковалева Алиса', 'Крапивин Семён', 'Мазуркевич Александра', 'Мазуркевич Алексей', 'Мазуркевич Артем',
                 'Мазуркевич Виктор',
                 'Мазуркевич Любовь', 'Макаревич Анастасия', 'Миско Александр', 'Можейко Алексей', 'Нестеренко Джейн',
                 'Никревич Алексей',
                 'Павлюк Андрей', 'Прозецкий Кирилл', 'Пятаков Андрей', 'Рабкевич Ирина', 'Савастюк Владислав',
                 'Савастюк Катерина',
                 'Сарнова Анастасия', 'Сикорская Людмила', 'Суремкина Елена', 'Томашевская Дарья', 'Трифонов Алексей',
                 'Трифонов Роман',
                 'Трифонова Антонина', 'Трифонова Кристина', 'Усов Алексей', 'Чепелева Марина', 'Шавалда Анастасия',
                 'Шавалда Владимир',
                 'Шавалда Евгений', 'Шавалда Инна', 'Шавалда Лиана', 'Шавалда Наталья', 'Шавалда Николай',
                 'Шуляковский Артем', 'Яскевич Татьяна']


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    print(message.from_user.id)
    if message.text=="/start":
        print(message.from_user.id)
        bot.send_message(message.from_user.id,"Привет\U0001F60A")
        checking_name(message.from_user.id)

def checking_name(id):
    keybord = telebot.types.InlineKeyboardMarkup()
    for i in range(1, len(spisok_gostey), 2):
        keybord.add(telebot.types.InlineKeyboardButton(text=spisok_gostey[i-1],
                                                       callback_data=f"name_{i-1}"),
                    telebot.types.InlineKeyboardButton(text=spisok_gostey[i],
                                                       callback_data=f"name_{i}"))
    if len(spisok_gostey) % 2 == 1:
        keybord.add(telebot.types.InlineKeyboardButton(text=spisok_gostey[-1],
                                                       callback_data=f"name_{len(spisok_gostey)-1}"))

    bot.send_message(id, text="Выберите ваше имя:", reply_markup=keybord)

def checking(call):
    keybord = telebot.types.InlineKeyboardMarkup()
    key_yes = telebot.types.InlineKeyboardButton(text="Да", callback_data=f"createMenu_{call.data[5:]}")
    keybord.add(key_yes)
    key__back = telebot.types.InlineKeyboardButton(text="Назад",callback_data="checking_name")
    keybord.add(key__back)
    bot.send_message(call.message.chat.id, text=f"Вы уверены,что вы {spisok_gostey[int(call.data[5:])]}?", reply_markup=keybord)

def createMenu():
        keybord = telebot.types.InlineKeyboardMarkup()  # готовим кнопки
        key_rassadka=telebot.types.InlineKeyboardButton(text="Рассадка",callback_data="seating") #callbackdata-это метод,который отвечает за гороскоп
        keybord.add(key_rassadka) #добавляем кнопку на экран

        key_cocktails = telebot.types.InlineKeyboardButton(text="Коктейли",callback_data="alcohol_not_alcohol")
        keybord.add(key_cocktails)

        key_timing = telebot.types.InlineKeyboardButton(text="Тайминг",callback_data="timing")
        keybord.add(key_timing)
        return keybord

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data[:10] == "createMenu":
        dct[call.message.chat.id] = int(call.data[11:])
        bot.send_message(call.message.chat.id, text="Выберите что хотите посмотреть\U0001F609", reply_markup=createMenu())
    if call.data[:4] == "name":
        checking(call)
    if call.data=="alcohol_not_alcohol":
        alcohol_not_alcohol(call)
    if call.data=="seating":
        seating(call)
    if call.data=="timing":
        timing(call)
    if call.data=="alcohol_names":
        create_alcohol_names(call)
    if call.data=="not_alcohol":
        create_not_alcohol_names(call)
    if call.data=="back_main_menu":
        bot.send_message(call.message.chat.id, text="Выберите что хотите посмотреть\U0001F609",
                         reply_markup=createMenu())
    if call.data[:5] == "order":
        order(call)

    if call.data=="checking_name":
        checking_name(id=call.message.chat.id)

    all_cocktails_order(call)

def alcohol_not_alcohol(call):
    CurrentTime = datetime.datetime.now()
    time_for_timing="Выберите алкогольные или безалкогольные коктейли желаете \U0001F914"
    if CurrentTime <= datetime.datetime(2021, 8, 14, hour=17, minute=15, second=0, microsecond=0, tzinfo=None):
        time_for_timing+="Учтите, бар работает 14.08 с 17:15:)"

    bot.send_message(call.message.chat.id, text=time_for_timing, reply_markup=create_cocktailmenu())

def create_cocktailmenu():
    keybord = telebot.types.InlineKeyboardMarkup()  # готовим кнопки
    key_alcohol = telebot.types.InlineKeyboardButton(text="Алкогольные",callback_data="alcohol_names")  # callbackdata-это метод,который вызывается при выборе кнопки
    keybord.add(key_alcohol)  # добавляем кнопку на экран
    key_cocktails = telebot.types.InlineKeyboardButton(text="Безалкогольные",callback_data="not_alcohol")
    keybord.add(key_cocktails)
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="back_main_menu")
    keybord.add(key_back)
    return keybord

def seating(call):
    keybord = telebot.types.InlineKeyboardMarkup()
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="back_main_menu")
    keybord.add(key_back)
    bot.send_message(call.message.chat.id, text="Найдите ваше место\U0001F609")
    with open("rassadka.jpg","rb") as photo:
        bot.send_photo(call.message.chat.id, photo, reply_markup=keybord)


def timing(call):
    keybord = telebot.types.InlineKeyboardMarkup()
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="back_main_menu")
    keybord.add(key_back)
    CurrentTime = datetime.datetime.now()
    time_for_timing=f"15.30 - 16.00 - Фуршет"+"\n 16.00 - 16.30 - Церемония" \
                    +"\n 16.30 - 17.15 - Вручение подарков, фотосессия по желанию(2 фотографа)" +"\n" \
                    + "17.15 - 18.10 - Первый застольный блок" + "\n"\
                    + "18.10 - 18.40 - Фотосессия(2 фотографа) + конкурсы/свободное время/танцы"+ "\n"\
                    + "18.40 - 19.40 - Сюприз для гостей"+"\n"\
                    + "19.40 - 20.30 - Второй застольный блок"+"\n"\
                    + "20.30 - 20.40 - Вынос торта, завершение официальной части вечера"+"\n"\
                    + "20.40 - 21.30 - Дискотека, караоке и бар\n20.40 - 21.30 - Терасса, Барбекю и чил-зона с кальянами"+"\n"\
                    + "21.30 - 22.00 - Конкурсы"+"\n"\
                    + "22.00 - 23.00 - Дискотека, караоке и бар\
                     22.00 - 23.00 - Терасса ,Барбекю и чил-зона с кальянами"+"\n"\
                    + "23.00 - 23.15 - Fireshow"+"\n"\
                    + "23.15 - 02.00 - Дискотека, караоке и бар\
                       23.15 - 02.00 - Терасса ,Барбекю и чил-зона с кальянами"




    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=16, minute=00, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing += f"15.30 - 16.00 - Фуршет"+"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=16, minute=30, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "16.00 - 16.30 - Церемония" +"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=17, minute=15, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "16.30 - 17.15 - Вручение подарков, фотосессия по желанию(2 фотографа)" +"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=18, minute=10, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "17.15 - 18.10 - Первый застольный блок" +"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=18, minute=40, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "18.10 - 18.40 - Фотосессия(2 фотографа) + конкурсы/свободное время/танцы"+"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=19, minute=40, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "18.40 - 19.40 - Сюприз для гостей"+"\n"
    # # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=20, minute=30, second=0, microsecond=0, tzinfo=None):
    # #     time_for_timing +=  "19.40 - 20.30 - Второй застольный блок"+"\n"
    # # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=20, minute=40, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "20.30 - 20.40 - Вынос торта, завершение официальной части вечера"+"\n"
    # # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=21, minute=30, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "20.40 - 21.30 - Дискотека, караоке и бар\n20.40 - 21.30 - Терасса, Барбекю и чил-зона с кальянами"+"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=22, minute=0, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "21.30 - 22.00 - Конкурсы"+"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=23, minute=0, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "22.00 - 23.00 - Дискотека, караоке и бар\
    #                          22.00 - 23.00 - Терасса ,Барбекю и чил-зона с кальянами"+"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 14, hour=23, minute=15, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "23.00 - 23.15 - Fireshow"+"\n"
    # if CurrentTime <= datetime.datetime(2021, 8, 15, hour=2, minute=00, second=0, microsecond=0, tzinfo=None):
    #     time_for_timing +=  "23.15 - 02.00 - Дискотека, караоке и бар\
    #                          23.15 - 02.00 - Терасса ,Барбекю и чил-зона с кальянами"
    bot.send_message(call.message.chat.id, text= time_for_timing,reply_markup=keybord)


def alcohol_names():
    keybord = telebot.types.InlineKeyboardMarkup()  # готовим кнопки
    keybord.add(telebot.types.InlineKeyboardButton(text="Синий иней",callback_data="description_sinei"))  # добавляем кнопку на экран
    keybord.add(telebot.types.InlineKeyboardButton(text="Особа", callback_data="description_osoba"))
    keybord.add(telebot.types.InlineKeyboardButton(text="Бочка рома", callback_data="description_bochka"))
    keybord.add(telebot.types.InlineKeyboardButton(text="Порн стар мартини", callback_data="description_porn_star"))
    keybord.add(telebot.types.InlineKeyboardButton(text="Дайкири", callback_data="description_daikiri"))
    keybord.add(telebot.types.InlineKeyboardButton(text="Секс на пляже", callback_data="description_sex"))
    keybord.add(telebot.types.InlineKeyboardButton(text="Негрони", callback_data="description_negroni"))
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="alcohol_not_alcohol")
    keybord.add(key_back)
    return keybord

def create_alcohol_names(call):
    bot.send_message(call.message.chat.id, text="Выберите какой алкольный коктейль желаете\U0001F60E", reply_markup=alcohol_names())

def create_not_alcohol_names(call):
    bot.send_message(call.message.chat.id, text="Выберите какой безалкогольный коктейль желаете\U0001F913", reply_markup=not_alcohol())

def not_alcohol():
    keybord = telebot.types.InlineKeyboardMarkup()  # готовим кнопки
    keybord.add(telebot.types.InlineKeyboardButton(text="Лимонад «Лесные ягоды»",callback_data="description_meri"))  # добавляем кнопку на экран
    keybord.add(telebot.types.InlineKeyboardButton(text="Лимонад «M&M’s»",callback_data="description_shirli_templ"))
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="alcohol_not_alcohol")
    keybord.add(key_back)
    return keybord

def order_back(huina, order):
    keybord = telebot.types.InlineKeyboardMarkup()
    key_order_cocktail = telebot.types.InlineKeyboardButton(text="Заказать", callback_data=order)
    keybord.add(key_order_cocktail)
    key_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data=huina)
    keybord.add(key_back)
    return keybord

def all_cocktails_order(call):
    if call.data=="description_sinei":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449джин Beefeater,портвейн,сироп Малина,сироп Блю Кюрасао,сок лимонный,сахарный сироп,Фаба/белок \
                                                     Классификация по вкусовым качествам:сладко-кислый", reply_markup= order_back("alcohol_names", "order_Синий иней"))
    if call.data=="description_osoba":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449ром Havana 3 Anos,пряный ликер DIY,сливки,сироп голубика,пюре черника \
                                                     Классификация по вкусовым качествам:сладкий", reply_markup=order_back("alcohol_names", "order_Особа"))
    if call.data=="description_bochka":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449ром Havana 3 Anos,сироп Гренадин,сок ананасовый,сок апельсиновый,сок лимонный \
                                                     Классификация по вкусовым качествам:сладкий", reply_markup=order_back("alcohol_names", "order_Бочка Рома"))
    if call.data== "description_porn_star":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449водка,сахарный сироп,сок лимонный,пюре манго,игристое вино \
                                                     Классификация по вкусовым качествам:кисло-сладкий",reply_markup=order_back("alcohol_names", "order_Порн стар Мартини"))
    if call.data == "description_daikiri":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449Ром Havana 3 Anos,сахарный сироп,сок лайма \
                                                        Классификация по вкусовым качествам:кислый-кислый",reply_markup=order_back("alcohol_names", "order_Дайкири"))
    if call.data == "description_sex":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449Водка,морс клюквенный,ликер Peach Tree,сок ананасовый,сироп Малина\
                                                            Классификация по вкусовым качествам:кисло-сладкий",reply_markup=order_back("alcohol_names", "order_Секс на пляже"))
    if call.data == "description_negroni":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449джин Beefeater,Вермут Martini Rosso,Биттер Campari\
                                                            Классификация по вкусовым качествам:терпкий",reply_markup=order_back("alcohol_names", "order_Негрони"))
    if call.data == "description_meri":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449пюре черника,сироп гренадин,сироп голубика,вода газированная",reply_markup=order_back("not_alcohol","order_Лесные ягоды"))
    if call.data == "description_shirli_templ":
        bot.send_message(call.message.chat.id, text="Состав\U0001F449пюре манго,сироп малина,сок лимонный,вода газированная",reply_markup=order_back("not_alcohol","order_Лимонад M&M’s"))

def order(call):
    CurrentTime = datetime.datetime.now()
    if call.message.chat.id not in dct.keys():
        bot.send_message(call.message.chat.id,
                         text="Пожалуйста, вернитесь в начало или очистите историю и выберите своё имя.")
    elif CurrentTime >datetime.datetime(2021,8,15,hour=2,minute=10, second=0, microsecond=0,tzinfo=None):
        bot.send_message(call.message.chat.id, text="Заказ коктейля уже невозможен\U0001F614")
    elif CurrentTime < datetime.datetime(2021,8,14,hour=17,minute=15, second=0, microsecond=0,tzinfo=None):
        bot.send_message(call.message.chat.id, text="Заказ коктейля возможен только 14.08 с 17:15\U0001F63D")
    else:
        bot.send_message(call.message.chat.id, text="Заказ принят\U0001F44FОфициант принесет вам коктейль")
        name = spisok_gostey[dct[call.message.chat.id]]
        table= spisok_stolov[dct[call.message.chat.id]]
        cocktail = call.data.split("_")[1]
        bot.send_message(655092828, text=f"{name}  заказал(а) {cocktail} стол гостя {table}")



bot.polling(none_stop=True,interval=0)
