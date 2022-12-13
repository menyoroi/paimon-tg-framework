import os
from loader import STORAGE
import templates
import sqlite3

async def bot_create(arg):
    global STORAGE
    namebot = None
    path = STORAGE._dir_
    if path != None:
        if os.path.exists(path):
            try:
                namebot = str(arg).split('-@ ')[1]
            except IndexError:
                print('Error: The name of the bot should be specified like this: -@ NAMEBOT')
                return
            if namebot.isalpha():
                if os.path.exists(fr'{path}\{namebot}') == False:
                    os.mkdir(fr'{path}\{namebot}')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\handlers')
                    with open(fr'{path}\{namebot}\requirements.txt', 'w', encoding='utf-8') as file:
                        file.write('aiogram\norator\nrequests\n')
                    with open(fr'{path}\{namebot}\handlers\__init__.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('handlers.init'))
                    with open(fr'{path}\{namebot}\handlers\error.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('handlers.error'))
                    os.mkdir(fr'{path}\{namebot}\handlers\users')
                    with open(fr'{path}\{namebot}\handlers\users\__init__.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('handlers.users.init'))
                    with open(fr'{path}\{namebot}\handlers\users\start.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('handlers.users.start'))
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\keyboards')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\states')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\backend')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\backend\database')
                    with open(fr'{path}\{namebot}\backend\database\__init__.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('backend.database.init'))
                    with open(fr'{path}\{namebot}\backend\database\users.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('backend.database.users'))
                    with open(fr'{path}\{namebot}\backend\database\bills.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('backend.database.bills'))
                    #######################################
                    with open(fr'{path}\{namebot}\main.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('main'))
                    with open(fr'{path}\{namebot}\loader.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('loader'))
                    with open(fr'{path}\{namebot}\config.py', 'w', encoding='utf-8') as file:
                        file.write(templates.readTemplates('config'))
                    #######################################
                    with open(fr'{path}\{namebot}\db.sqlite', 'w') as file:
                        file.write('')
                    _db_ = sqlite3.connect(fr'{path}\{namebot}\db.sqlite')
                    _db_cur = _db_.cursor()
                    _db_cur.execute("""CREATE TABLE IF NOT EXISTS users(
                       user_id INT PRIMARY KEY,
                       username TEXT,
                       balance INT,
                       admins INT);
                    """)
                    _db_cur.execute("""CREATE TABLE IF NOT EXISTS bills(
                       bill_id INT PRIMARY KEY,
                       amount INT,
                       status TEXT,
                       created TEXT,
                       msg_id INT);
                    """)
                    _db_cur.execute("""CREATE TABLE IF NOT EXISTS secretKeys(
                        key TEXT PRIMARY KEY);
                    """)
                    _db_.commit()
                    #######################################
                else:
                    print('Error: Such a bot already exists!')
            else:
                print('Error: Do not specify symbols and other signs in the name !')
        else:
            print('Error: This path does not exist!')
    else:
        print('Error: The path to the folder for creating the bot has not yet been configured!')