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
        bot.send_message(user_id, "Выберите действие", reply_markup=buttons.main_menu())
    elif language == "Uzb 🇺🇿":
        mm = bot.send_message(user_id, "Bosh menyu", reply_markup=types.ReplyKeyboardRemove())
        bot.delete_message(user_id, mm.message_id)
        check_user = database.check_users(user_id)
        bot.send_message(user_id, "Xarakatni tanlang",
                         reply_markup=buttons.main_menu())


def registration(message):
    user_id = message.from_user.id
    if message.text == "Русский язык 🇷🇺":
        language = "Rus"
        bot.send_message(user_id, "Напишите своё имя: ")
        bot.register_next_step_handler(message, get_name, language)
    elif message.text == "O'zbek tili 🇺🇿":
        language = "Uzb"
        bot.send_message(user_id, "Ismingizni kiriting: ")
        bot.register_next_step_handler(message, get_name_uz, language)
        # database.add_user(user_id, "uzb")
    # elif message.text ==
    #     mm = bot.send_message(user_id, "Bosh menyu", reply_markup=types.ReplyKeyboardRemove())
    #     bot.delete_message(user_id, mm.message_id)
    #     check_users = database.check_users(user_id)
    #     bot.send_message(user_id, "Xarakatni tanlang",
    #                      reply_markup=buttons.main_menu(check_users))
    else:
        bot.send_message(user_id, "Выберите язык из списка в меню / Tilni menudan tanlang",
                         reply_markup=buttons.language_kb())
        bot.register_next_step_handler(message, registration())

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

@bot.callback_query_handler(lambda call: call.data in ['Чирчик', 'ВВС Управление', 'Академия Вооруженных Сил', 'Центральный военный госпиталь',
                                                       'Chirchiq', 'Markaziy harbiy kasalxona', 'XHK Boshqarmasi', 'Qurolli Kuchlar Akademiyas'])
def get_work(call):
    user_id = call.message.chat.id
    work = call.data
    if users.get(user_id)[1] == "Rus":
        bot.send_message(user_id, "Отправьте свой номер телефона: ", reply_markup=buttons.get_phone_number())
        bot.register_next_step_handler(call.message, get_number, work)
    elif users.get(user_id)[1] == "Uzb":
        bot.send_message(user_id, "Telefon raqamingizni jo'nating: ", reply_markup=buttons.get_phone_number_uz())
        bot.register_next_step_handler(call.message, get_number_uz, work)
def get_number(message, work):
    user_id = message.from_user.id
    if user_id in users:
        if message.contact:
            phone_number = message.contact.phone_number
            bot.send_message(user_id, "Вы успешно зарегестрировались!", reply_markup=types.ReplyKeyboardRemove())
            database.add_user(user_id, users.get(user_id)[0], work, phone_number, users.get(user_id)[1])
            bot.send_message(-1001996929800, f"Новый курьер: \n"
                                             f"Имя: {users.get(user_id)[0]} \n"
                                             f"Локация: {work} \n"
                                             f"Контактный номер: {phone_number} \n"
                                             f"Аккаунт: @{message.from_user.username}", reply_markup=types.ReplyKeyboardRemove())
            users.pop(user_id)
            print(database.get_user_name(user_id))
            bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                           caption=f'Здравствуйте, дорогой {database.get_user_name(user_id)}! \n'
                                   f'Добро пожаловать в мясной интернет-магазин <Angus>! \n'
                                   f'Используйте нужные вам разделы:',
                           reply_markup=buttons.pay_feedback())
            print(database.get_users())
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
            database.add_user(user_id=user_id, user_name=users.get(user_id)[0],
                              user_phone_number=phone_number, user_work=work, language='users.get(user_id)[1]')
            bot.send_message(-1001996929800, f"Yangi kuryer: \n"
                                             f"Ismi: {users.get(user_id)[0]} \n"
                                             f"Lokatsiya: {work} \n"
                                             f"Telefon raqam: {phone_number} \n"
                                             f"Akkaunt: @{message.from_user.username}", reply_markup=types.ReplyKeyboardRemove())
            users.pop(user_id)
            database.get_users()
            bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                           caption=f"Assalomu aleykum, xurmatli {database.get_user_name(user_id)}! /n"
                                   f"<Angus> Onlayn go'sht do'koniga xush kelibsiz! /n"
                                   f"Sizga kerak bo'lgan bo'limlardan foydalaning:",
                           reply_markup=buttons.pay_feedback())
            print(users)
        else:
            bot.send_message(user_id, "Xatolik! Qayta urinib ko'ring")
    else:
        bot.send_message(user_id, "Telefon raqamingizni jo'nating")
        bot.register_next_step_handler(message, get_number, work)

@bot.callback_query_handler(lambda call: call.data in ['pay', 'feedback', 'click', 'payme', 'paynet', 'zaplatil', 'otmenit', 'skinul',
                                                       'pay_uz', 'feedback_uz', 'click_uz', 'payme_uz', 'paynet_uz', 'zaplatil_uz', 'otmena', 'tashladim', 'toladim', 'back'])
def pay_answer(call):
    user_id = call.message.chat.id
    if call.data == 'pay':
        bot.send_message(user_id, "Введите сумму которую заплатите:\n"
                                  "В виде: 100.000 сум", reply_markup=buttons.back())
        bot.register_next_step_handler(call.message, choosing_payment)
    elif call.data == 'feedback':
        bot.send_message(user_id, "Оставьте свой отзыв или письмо админу: ", reply_markup=buttons.back())
        bot.register_next_step_handler(call.message, feedback_fc)
    elif call.data == 'click':
        bot.send_message(user_id, f'''
        Ваше имя: {database.get_user_name(user_id)};
Скиньте сумму {users.get(user_id)[0]} в этот кошелёк:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen())
    elif call.data == 'payme':
        bot.send_message(user_id, f'''Ваше имя: {database.get_user_name(user_id)};
Скиньте сумму {users.get(user_id)[0]} в этот кошелёк:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen())
    elif call.data == 'paynet':
        bot.send_message(user_id, f'''Ваше имя: {database.get_user_name(user_id)};
Скиньте сумму {call.message} в этот кошелёк:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen())
    elif call.data == 'zaplatil':
        bot.send_message(user_id, "Скиньте чек оплаты сюда: @adminangus", reply_markup=buttons.oplata())
    elif call.data == 'otmenit':
        bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                       caption=f'Здравствуйте, дорогой {database.get_user_name(user_id)}! \n'
                               f'Добро пожаловать в мясной интернет-магазин <Angus>!\n'
                               f'Используйте нужные вам разделы:',
                       reply_markup=buttons.pay_feedback())
        bot.register_next_step_handler(call.data, feedback_fc)
    elif call.data == 'skinul':
        bot.send_message(user_id, "Спасибо за платёж!")
        bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                       caption=f'Здравствуйте, дорогой {database.get_user_name(user_id)}! \n'
                            f'Добро пожаловать в мясной интернет-магазин <Angus>! \n'
                            f'Используйте нужные вам разделы:',
                       reply_markup=buttons.pay_feedback())
        bot.send_message(-1001996929800, f''' Заплата за долг: {users.get(user_id)[0]}
Имя: {database.get_user_name(user_id)}
Телефонный номер: {database.get_number(user_id)}
Район: {database.get_location(user_id)}''')
    elif call.data == 'pay_uz':
        bot.send_message(user_id, "Siz to'laydigan miqdorni kiriting::\n"
                                  "Shakli: 100.000 so'm", reply_markup=buttons.back())
        bot.register_next_step_handler(call.message, choosing_payment_uz)
    elif call.data == 'feedback_uz':
        bot.send_message(user_id, "O'z izohinggizni qoldirishinggiz mumkun: ", reply_markup=buttons.back())
        bot.register_next_step_handler(call.message, feedback_fc)
    elif call.data == 'click_uz':
        bot.send_message(user_id, f'''
        Ismingiz: {database.get_user_name(user_id)};
{users.get(user_id)[0]} miqdorni ushbu hamyonga o'tkazing:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen_uz())
    elif call.data == 'payme_uz':
        bot.send_message(user_id, f'''Ismingiz: {database.get_user_name(user_id)};
{users.get(user_id)[0]} miqdorni ushbu hamyonga o'tkazing:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen_uz())
    elif call.data == 'paynet_uz':
        bot.send_message(user_id, f'''Ismingiz: {database.get_user_name(user_id)};
{call.message} miqdorni ushbu hamyonga o'tkazing:
1234 5678 1234 5678
Palonchiev''', reply_markup=buttons.oplata_otmen_uz())
    elif call.data == 'toladim':
        bot.send_message(user_id, text="To'lov chekini ushbu adminga yuboring: @adminangus",
                         reply_markup=buttons.oplata_uz())
    elif call.data == 'otmena':
        bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                       caption=f"Assalomu aleykum, xurmatli {database.get_user_name(user_id)}! \n"
                               f"<Angus> Onlayn go'sht do'koniga xush kelibsiz! \n"
                               f"Sizga kerak bo'lgan bo'limlardan foydalaning:",
                       reply_markup=buttons.pay_feedback())
        bot.register_next_step_handler(call.data, feedback_fc)
    elif call.data == 'tashladim':
        bot.send_message(user_id, "To'lov uchun rahmat!")
        bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                       caption=f"Assalomu aleykum, xurmatli {database.get_user_name(user_id)}! \n"
                               f"<Angus> Onlayn go'sht do'koniga xush kelibsiz! \n"
                               f"Sizga kerak bo'lgan bo'limlardan foydalaning:",
                       reply_markup=buttons.pay_feedback())
        bot.send_message(-1001996929800, f'''Заплата за долг: {users.get(user_id)[0]}
Имя: {database.get_user_name(user_id)}
Телефонный номер: {database.get_number(user_id)}
Район: {database.get_location(user_id)}''')
    elif call.data =='back':
        bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'),
                           caption=f'Здравствуйте, дорогой {database.get_user_name(user_id)}! \n'
                                   f'Добро пожаловать в мясной интернет-магазин <Angus>! \n'
                                   f'Используйте нужные вам разделы:', reply_markup=buttons.main_menu())

@bot.message_handler(content_types=['text'])
def choosing_payment(message):
    user_id = message.from_user.id
    lend = [message.text]
    users[user_id] = lend
    print(users)
    bot.send_message(user_id, "Через какую платформу хотите заплатить?", reply_markup=buttons.payment())
@bot.message_handler(content_types=['text'])
def choosing_payment_uz(message):
    user_id = message.from_user.id
    lend = [message.text]
    users[user_id] = lend
    print(users)
    bot.send_message(user_id, "Qaysi platforma orqali pul to'lamoxchisiz?", reply_markup=buttons.payment_uz())

def feedback_fc(message):
    user_id = message.from_user.id
    bot.send_message(-1001996929800, f" Отзыв: {message.text}\n"
                                     f"Айди пользователя: {user_id}" f"Телефон номер: {database.get_number(user_id)}")
    bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'), caption=f'Здравствуйте, дорогой {database.get_user_name(user_id)[0]}! \n'
                                                                                       f'Добро пожаловать в мясной интернет-магазин <Angus>! \n'
                                                                                       f'Используйте нужные вам разделы:',
                   reply_markup=buttons.pay_feedback())
    # bot.register_next_step_handler(message, main_menu())

def main_menu(message):
    user_id = message.from_user.id
    bot.send_photo(user_id, photo=open('photo_2024-02-20_23-47-23.jpg', 'rb'), caption=f'Здравствуйте, дорогой {database.get_user_name(user_id)[0]}! \n'
                                                                                       f'Добро пожаловать в мясной интернет-магазин <Angus>! \n'
                                                                                       f'Используйте нужные вам разделы:')





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
#
#


bot.infinity_polling()