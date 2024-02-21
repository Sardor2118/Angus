import sqlite3
from datetime import datetime

connection = sqlite3.connect("baza_dannix.db")
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT, work TEXT,'
            'phone_number TEXT, language TEXT, reg_date DATETIME);')
sql.execute('CREATE TABLE IF NOT EXISTS work (user_id INTEGER, rayon1 TEXT, rayon2 TEXT,'
            'rayon3 TEXT, rayon4 TEXT);')

def add_user(user_id, user_name, user_phone_number, user_work, language):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    sql.execute('INSERT INTO users (user_id, name, phone_number, work, language, reg_date) VALUES (?, ?, ?, ?, ?, ?);',
                (user_id, user_name, user_phone_number, user_work, language, datetime.now()))
    
def get_users():
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    users = sql.execute('SELECT * FROM users;').fetchall()
    return users
def check_users(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    checker = sql.execute('SELECT user_id FROM users WHERE user_id = ?;',(user_id, )).fetchone()
    if checker:
        return True
    else:
        return False
def check_language(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT language FROM users WHERE user_id = ?;", (user_id,))
    if checker.fetchone() == ("uzb",):
        return "uzb"
    elif checker.fetchone() == ("rus",):
        return "rus"
    return False
def work(user_id, rayon1='Район 1', rayon2='Район 2', rayon3='Район 3', rayon4='Район 4'):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO work (user_id, rayon1, rayon2, rayon3, rayon4) VALUES (?, ?, ?, ?);", (user_id, rayon1,
                                                                                                    rayon2, rayon3, rayon4))
    connection.commit()
def from_work(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    sql.execute('SELECT * FROM work WHERE user_id = ?;', (user_id, )).fetchone()
def get_user_name(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    sql.execute('SELECT name FROM users WHERE user_id = ?;', (user_id, )).fetchone()
    result = sql.fetchone()
    return result
def get_location(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    sql.execute('SELECT work FROM users WHERE user_id = ?;', (user_id, )).fetchone()
    result = sql.fetchone()
    return result
def get_number(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    sql.execute('SELECT phone_number FROM users WHERE user_id = ?;', (user_id, )).fetchone()
    result = sql.fetchone()
    return result
