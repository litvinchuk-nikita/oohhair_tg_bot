import sqlite3

def create_table_db():
    try:
        conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        # cur.execute('CREATE TABLE theory(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR(15))')
        # cur.execute('CREATE TABLE practice(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR(15))')
        # cur.execute('CREATE TABLE polirovka(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR(15))')
        # cur.execute('CREATE TABLE smm(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR(15))')
        cur.execute('CREATE TABLE promotion(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id VARCHAR(15))')
        conn.commit()
        print("Таблица SQLite создана")
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def insert_theory(user_id):
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('INSERT INTO theory(user_id)'
                    ' VALUES ("%s")' % (user_id))
        print("Данные в таблицу добавлены")
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при добавлении данных в sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def select_theory_id():
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('SELECT user_id FROM theory')
        print("Данные получены")
        user_id = cur.fetchall()
        cur.close()
        user_id_list = []
        for id in user_id:
            user_id_list.append(int(id[0]))
        return user_id_list
    except sqlite3.Error as error:
        print("Ошибка при получении данных из sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def insert_practice(user_id):
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('INSERT INTO practice(user_id)'
                    ' VALUES ("%s")' % (user_id))
        print("Данные в таблицу добавлены")
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при добавлении данных в sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def select_practice_id():
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('SELECT user_id FROM practice')
        print("Данные получены")
        user_id = cur.fetchall()
        cur.close()
        user_id_list = []
        for id in user_id:
            user_id_list.append(int(id[0]))
        return user_id_list
    except sqlite3.Error as error:
        print("Ошибка при получении данных из sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def insert_polirovka(user_id):
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('INSERT INTO polirovka(user_id)'
                    ' VALUES ("%s")' % (user_id))
        print("Данные в таблицу добавлены")
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при добавлении данных в sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def select_polirovka_id():
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('SELECT user_id FROM polirovka')
        print("Данные получены")
        user_id = cur.fetchall()
        cur.close()
        user_id_list = []
        for id in user_id:
            user_id_list.append(int(id[0]))
        return user_id_list
    except sqlite3.Error as error:
        print("Ошибка при получении данных из sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def insert_smm(user_id):
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('INSERT INTO smm(user_id)'
                    ' VALUES ("%s")' % (user_id))
        print("Данные в таблицу добавлены")
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при добавлении данных в sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def select_smm_id():
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('SELECT user_id FROM smm')
        print("Данные получены")
        user_id = cur.fetchall()
        cur.close()
        user_id_list = []
        for id in user_id:
            user_id_list.append(int(id[0]))
        return user_id_list
    except sqlite3.Error as error:
        print("Ошибка при получении данных из sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def insert_promotion(user_id):
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('INSERT INTO promotion(user_id)'
                    ' VALUES ("%s")' % (user_id))
        print("Данные в таблицу добавлены")
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при добавлении данных в sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")


def select_promotion_id():
    try:
        conn = sqlite3.connect('/home/nikita/oohhair_tg_bot/db.sql', timeout=20)
        # conn = sqlite3.connect('oohhair_bot/db.sql')
        cur = conn.cursor()
        print("База данных подключена к SQLite")
        cur.execute('SELECT user_id FROM promotion')
        print("Данные получены")
        user_id = cur.fetchall()
        cur.close()
        user_id_list = []
        for id in user_id:
            user_id_list.append(int(id[0]))
        return user_id_list
    except sqlite3.Error as error:
        print("Ошибка при получении данных из sqlite", error.__class__, error)
    finally:
        if (conn):
            conn.close()
            print("Соединение с SQLite закрыто")

# создаем шаблон заполнения словаря с пользователями для теории
user_dict_template_theory: dict = {'less': 1}

# создаем шаблон заполнения словаря с пользователями для практики
user_dict_template_practice: dict = {'practice': 1}

# создаем шаблон заполнения словаря с пользователями для повышения
user_dict_template_promotion: dict = {'promotion': 1}

# инициализируем "базу данных" для теории
users_db: dict = {}

# инициализируем "базу данных" для практики
users_db_pr: dict = {}

# инициализируем "базу данных" для повышения
users_db_prom: dict = {}
