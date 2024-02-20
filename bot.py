import telebot
import database
import buttons
from telebot import types

bot = telebot.TeleBot("6986619740:AAFJvNoqZGZZ55C7vlkREEq9wWCQ5Rpll4Y")

users= {}

# def main_menu(message, photo, text):
#     user_id = message.from_user.id
#     bot.send_photo(user_id, photo, caption=text, reply_markup=buttons.pay_feedback_uz())

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    language = database.check_language(user_id)
    if language == False:
        bot.send_message(user_id, "Выберите язык / Tilni tanlang", reply_markup=buttons.language_kb())
        bot.register_next_step_handler(message, registration)
    elif language == "Rus 🇷🇺":
        mm = bot.send_message(user_id, "Главное меню", reply_markup=types.ReplyKeyboardRemove())
        bot.delete_message(user_id, mm.message_id)
        check_user = database.check_users(user_id)
        bot.send_message(user_id, "Выберите действие",
                        reply_markup=buttons.main_menu(check_users))
    elif language == "Uzb 🇺🇿":
        mm = bot.send_message(user_id, "Бош меню", reply_markup=types.ReplyKeyboardRemove())
        bot.delete_message(user_id, mm.message_id)
        check_user = database.check_users(user_id)
        bot.send_message(user_id, "Ҳаракатни танланг",
                         reply_markup=buttons.main_menu(check_users))


def registration(message):
    user_id = message.from_user.id
    if message.text == "Русский язык 🇷🇺":
        language = "Rus"
        bot.send_message(user_id, "Напишите своё имя: ")
        bot.register_next_step_handler(message, get_name, language)
    elif message.text == "O'zbek tili 🇺🇿":
        database.add_user(user_id, "uzb")
        mm = bot.send_message(user_id, "Bosh menyu", reply_markup=types.ReplyKeyboardRemove())
        bot.delete_message(user_id, mm.message_id)
        check_users = database.check_users(user_id)
        bot.send_message(user_id, "Xarakatni tanlang",
                         reply_markup=buttons.main_menu(check_users))
    else:
        bot.send_message(user_id, "Выберите язык из списка в меню / Tilni menudan tanlang",
                         reply_markup=buttons.language_kb())
        bot.register_next_step_handler(message, register_user)

def get_name(message, language):
    user_id = message.from_user.id
    name = message.text
    users[user_id] = [name, language]
    bot.send_message(user_id, "Место работы: ", reply_markup=buttons.work_kb())
def get_name_uz(message, language):
    user_id = message.from_user.id
    name = message.text
    users[user_id] = [name, language]
    bot.send_message(user_id, "Ish joyingizni kiriting: ", reply_markup=buttons.work_kb_uz())

@bot.callback_query_handler(lambda call: call.data in ['Чирчик', 'ВВС Управление', 'Академия Вооруженных Сил', 'Центральный военный госпиталь'])
def get_work(call):
    user_id = call.message.chat.id
    work = call.data
    if users.get(user_id)[1] == "Rus":
        bot.send_message(user_id, "Отправьте свой номер телефона: ", reply_markup=buttons.get_phone_number())
        bot.register_next_step_handler(call.message, get_number, work)
    else:
        bot.send_message(user_id, "Telefon raqamingizni jo'nating: ", reply_markup=buttons.get_phone_number())
        bot.register_next_step_handler(call.message, get_number, work)
def get_number(message, work):
    user_id = message.from_user.id
    if user_id in users:
        if message.contact:
            phone_number = message.contact.phone_number
            bot.send_message(user_id, "Вы успешно зарегестрировались!", reply_markup=types.ReplyKeyboardRemove())
            database.add_user(user_id=user_id, user_name=users.get(user_id)[0],
                              user_phone_number=phone_number, user_work=work, language='users.get(user_id)[1]')
            bot.send_message(-1001996929800, f"Новый курьер: \n"
                                             f"Имя: {users.get(user_id)[0]} \n"
                                             f"Локация: {work} \n"
                                             f"Контактный номер: {phone_number} \n"
                                             f"Аккаунт: @{message.from_user.username}", reply_markup=types.ReplyKeyboardRemove())
            users.pop(user_id)
            database.get_users()
            bot.send_photo(user_id, photo=open('photo_2024-02-15_20-39-17.jpg', 'rb'), caption='Assalomu aleykum', reply_markup=buttons.pay_feedback_uz())
            print(users)
        else:
            bot.send_message(user_id, "Ошибка! Перезагрузите бота")
    else:
        bot.send_message(user_id, "Отправьте свой номер через кнопку")
        bot.register_next_step_handler(message, get_number, work)

def get_number_uz(message, work):
    user_id = message.from_user.id
    if user_id in users:
        if message.contact:
            phone_number = message.contact.phone_number
            bot.send_message(user_id, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!", reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(-1001996929800, f"Yangi kuryer: \n"
                                             f"Ismi: {users.get(user_id)[0]} \n"
                                             f"Lokatsiya: {work} \n"
                                             f"Telefon raqam: {phone_number} \n"
                                             f"Akkaunt: @{message.from_user.username}", reply_markup=types.ReplyKeyboardRemove())
            users.pop(user_id)
        else:
            bot.send_message(user_id, "Xatolik! Qayta urinib ko'ring")
    else:
        bot.send_message(user_id, "Telefon raqamingizni jo'nating")
        bot.register_next_step_handler(message, get_number, work)

@bot.callback_query_handler(lambda call: call.data in ['pay', 'feedback', 'click', 'payme', 'paynet', 'toladim', 'otmena', 'tashladim'])
def pay_answer(call):
    user_id = call.message.chat.id
    if call.data=='pay':
        bot.send_message(user_id, "Siz to'laydigan miqdorni kiriting:\n"
                                  "Shakli: '100000", reply_markup=buttons.back())
        bot.register_next_step_handler(message, choosing_payment)
    elif call.data=='feedback':
        pass
    elif call.data=='click':
        bot.send_message(user_id, f'''
        Ismingiz: {users.get(user_id)[0]};
{users.get(user_id)[0]} miqdorini usbu hamyonga o'tqazing:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen_uz())
    elif call.data=='payme':
        bot.send_message(user_id, f'''Ismingiz: {users.get(user_id)[0]};
{users.get(user_id)[0]} miqdorini usbu hamyonga o'tqazing:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen_uz())
    elif call.data=='paynet':
        bot.send_message(user_id, f'''Ismingiz: {users.get(user_id)[0]};
{users.get(user_id)[0]} miqdorini usbu hamyonga o'tqazing:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen_uz())
    elif call.data=='toladim':
        bot.send_message(user_id, "To'lov checkini ushbu adminga yuboring: @adminangus", reply_markup=buttons.oplata_uz())
    elif call.data=='otmena':
        bot.send_photo(user_id, photo=open('photo_2024-02-15_20-39-17.jpg', 'rb'), caption='Assalomu aleykum',
                       reply_markup=buttons.pay_feedback_uz())
    elif call.data=='tashladim':
        bot.send_message(user_id, "To'lov uchun rahmat!")
        bot.send_photo(user_id, photo=open('photo_2024-02-15_20-39-17.jpg', 'rb'), caption='Assalomu aleykum',
                       reply_markup=buttons.pay_feedback_uz())
        bot.send_message(-1001996929800, f'''Заплата за долг: {users.get(user_id)[0]}
Имя: 
Телефонный номер:
Район:''')

@bot.message_handler(content_types=['text'])
def choosing_payment(message):
    user_id = message.from_user.id
    lend = [message.text]
    users[user_id] = lend
    print(users)
    bot.send_message(user_id, "Qaysi platrforma orqali tolamoxchisiz?", reply_markup=buttons.payment())





#################################################
# def registration_uz(message):
#     user_id = message.from_user.id
#     language = message.text
#     bot.send_message(user_id, "Telefon raqamingizni jo'nating", reply_markup=buttons.get_phone_number())
#     bot.register_next_step_handler(message, get_number(), name)
#
# def get_name(message):
#     user_id = message.from_user.id
#     name = message.text
#     bot.send_message(user_id, "Напишите своё имя и фамилю")
#     bot.register_next_step_handler(message, get_number)
#
# def get_number(message, name):
#     user_id = message.from_user.id
#     if message.contact:
#         phone_number = message.contact.phone_number
#         bot.send_message(user_id, "Вы успешно зарегестрировались!", reply_markup=types.ReplyKeyboardRemove())
#         database.add_user(user_id=user_id, user_name=name, user_phone_number=phone_number)
#         print(database.get_users())
#     else:
#         bot.send_message(user_id, "Отправьте свой номер через кнопку")
#         bot.register_next_step_handler(message, get_number, name)
#     print(message.contact)
# def get_number_uz(message, name):
#     user_id = message.from_user.id
#     if message.contact:
#         phone_number = message.contact.phone_number
#         bot.send_message(user_id, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz!", reply_markup=types.ReplyKeyboardRemove())
#         database.add_user(user_id=user_id, user_name=name, user_phone_number=phone_number)
#         print(database.get_users())
#     else:
#         bot.send_message(user_id, "Raqamingizni tugma orqali yuboring")
#         bot.register_next_step_handler(message, get_number, name)
#     print(message.contact)
#
# def feedback_fc(message):
#     user_id = message.from_user.id
#     user_phone = message.from_user.phone_number
#     bot.send_message(-1001996929800, f"{message.text}\n"
#                                      f"Айди пользователя: {user_id}" f"Телефон номер: {user_phone}")
#


bot.infinity_polling()