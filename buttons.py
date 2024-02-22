from telebot import types


def get_phone_number():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_number = types.KeyboardButton(text='Поделиться контактом 📲', request_contact=True)
    kb.add(phone_number)
    return kb
def get_phone_number_uz():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_number = types.KeyboardButton(text="Nomerim jo'natish 📲", request_contact=True)
    kb.add(phone_number)
    return kb
def get_phone_number_uz():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_number = types.KeyboardButton(text="Telefon raqamingizni jo'nating 📲", request_contact=True)
    kb.add(phone_number)
    return kb
def main_menu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    main_menu = types.InlineKeyboardButton(text="Закрыть задолженность", callback_data='main_menu')
    feedback = types.InlineKeyboardButton(text="Оставьте отзыв", callback_data='feedback')
    kb.add(main_menu, feedback)
    return kb
def language_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rus = types.KeyboardButton("Русский язык 🇷🇺")
    uzb = types.KeyboardButton("O'zbek tili 🇺🇿")
    kb.add(rus, uzb)
    return kb
def work_kb():
    kb = types.InlineKeyboardMarkup(row_width=1)
    rayon1 = types.InlineKeyboardButton(text="Чирчик", callback_data = 'Чирчик')
    rayon3 = types.InlineKeyboardButton(text="ВВС Управление", callback_data= 'ВВС Управление')
    rayon4 = types.InlineKeyboardButton(text="Академия Вооруженных Сил", callback_data='Академия Вооруженных Сил')
    rayon2 = types.InlineKeyboardButton(text="Центральный военный госпиталь", callback_data='Центральный военный госпиталь')
    kb.add(rayon1, rayon2, rayon3, rayon4)
    return kb
def work_kb_uz():
    kb = types.InlineKeyboardMarkup(row_width=1)
    rayon1 = types.InlineKeyboardButton("Chirchiq", callback_data='Chirchiq')
    rayon2 = types.InlineKeyboardButton("Markaziy harbiy kasalxona", callback_data='Markaziy harbiy kasalxona')
    rayon3 = types.InlineKeyboardButton("XHK Boshqarmasi", callback_data='XHK Boshqarmasi')
    rayon4 = types.InlineKeyboardButton("Qurolli Kuchlar Akademiyas", callback_data='Qurolli Kuchlar Akademiyas')
    kb.add(rayon4, rayon1, rayon2, rayon3)
    return kb
def pay_feedback_uz():
    kb = types.InlineKeyboardMarkup(row_width=1)
    pay = types.InlineKeyboardButton('Qarzdorlikni yopish', callback_data='pay_uz')
    feedback = types.InlineKeyboardButton('Izoh qoldirish', callback_data='feedback_uz')
    kb.add(pay, feedback)
    return kb
def pay_feedback():
    kb = types.InlineKeyboardMarkup(row_width=1)
    pay = types.InlineKeyboardButton('Погасить долг', callback_data='pay')
    feedback = types.InlineKeyboardButton('Оставить отзыв', callback_data='feedback')
    kb.add(pay, feedback)
    return kb
def back():
    kb = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton('Назад', callback_data='back')
    kb.add(back)
    return kb
def back_uz():
    kb = types.InlineKeyboardMarkup(row_width=1)
    back = types.InlineKeyboardButton('Orqaga', callback_data='orqaga')
    kb.add(back)
    return kb
def payment():
    kb = types.InlineKeyboardMarkup(row_width=1)
    click = types.InlineKeyboardButton('Click', callback_data='click')
    payme = types.InlineKeyboardButton('Payme', callback_data='payme')
    paynet = types.InlineKeyboardButton('Paynet', callback_data='paynet')
    kb.add(click, payme, paynet)
    return kb
def payment_uz():
    kb = types.InlineKeyboardMarkup(row_width=1)
    click = types.InlineKeyboardButton('Click', callback_data='click_uz')
    payme = types.InlineKeyboardButton('Payme', callback_data='payme_uz')
    paynet = types.InlineKeyboardButton('Paynet', callback_data='paynet_uz')
    kb.add(click, payme, paynet)
    return kb
def oplata_otmen_uz():
    kb = types.InlineKeyboardMarkup(row_width=1)
    toladim = types.InlineKeyboardButton("To'ladim", callback_data="toladim")
    otmena = types.InlineKeyboardButton("Bekor qilish", callback_data="otmena")
    kb.add(toladim, otmena)
    return kb
def oplata_otmen():
    kb = types.InlineKeyboardMarkup(row_width=1)
    zaplatil = types.InlineKeyboardButton("Заплатил", callback_data="zaplatil")
    otmenit = types.InlineKeyboardButton("Отменить", callback_data="otmenit")
    kb.add(zaplatil, otmenit)
    return kb
def oplata_uz():
    kb = types.InlineKeyboardMarkup(row_width=1)
    toladim = types.InlineKeyboardButton("Tashladim", callback_data="tashladim")
    kb.add(toladim)
    return kb
def oplata():
    kb = types.InlineKeyboardMarkup(row_width=1)
    toladim = types.InlineKeyboardButton("Скинул", callback_data="skinul")
    kb.add(toladim)
    return kb