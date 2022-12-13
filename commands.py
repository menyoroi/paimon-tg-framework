import os
from loader import STORAGE
import templates
import sqlite3

async def select_dir(arg): #dir "path"
    global STORAGE
    try:
        path = str(arg).split('"')[1]
        if os.path.exists(path):
            STORAGE._dir_ = path
        else:
            print('Error: This path does not exist!')
    except IndexError:
        print('Error: Specify the path to the folder to create the bot in " "')  # Указать путь в ""

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
                    open(fr'{path}\{namebot}\requirements.txt', 'w', encoding='utf-8').write('aiogram\norator\nrequests\n')
                    open(fr'{path}\{namebot}\handlers\__init__.py', 'w', encoding='utf-8').write(templates.readTemplates('handlers.init'))
                    open(fr'{path}\{namebot}\handlers\error.py', 'w', encoding='utf-8').write(templates.readTemplates('handlers.error'))
                    os.mkdir(fr'{path}\{namebot}\handlers\users')
                    open(fr'{path}\{namebot}\handlers\users\__init__.py', 'w', encoding='utf-8').write(templates.readTemplates('handlers.users.init'))
                    open(fr'{path}\{namebot}\handlers\users\start.py', 'w', encoding='utf-8').write(templates.readTemplates('handlers.users.start'))
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\keyboards')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\states')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\backend')
                    #######################################
                    os.mkdir(fr'{path}\{namebot}\backend\database')
                    open(fr'{path}\{namebot}\backend\database\__init__.py', 'w', encoding='utf-8').write(templates.readTemplates('backend.database.init'))
                    open(fr'{path}\{namebot}\backend\database\users.py', 'w', encoding='utf-8').write(templates.readTemplates('backend.database.users'))
                    open(fr'{path}\{namebot}\backend\database\bills.py', 'w', encoding='utf-8').write(templates.readTemplates('backend.database.bills'))
                    #######################################
                    open(fr'{path}\{namebot}\main.py', 'w', encoding='utf-8').write(templates.readTemplates('main'))
                    open(fr'{path}\{namebot}\loader.py', 'w', encoding='utf-8').write(templates.readTemplates('loader'))
                    open(fr'{path}\{namebot}\config.py', 'w', encoding='utf-8').write(templates.readTemplates('config'))
                    #######################################
                    open(fr'{path}\{namebot}\db.sqlite', 'w').write('')
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

async def bot_payments(arg):
    global STORAGE
    namebot = None
    name_system_payments = None
    path = STORAGE._dir_
    if path != None:
        if os.path.exists(path):
            try:
                namebot = str(arg).split('-@ ')[1].split(' ')[0].rstrip().strip()
            except IndexError:
                print('Error: The name of the bot should be specified like this: -@ NAMEBOT')
                return
            if os.path.exists(fr'{path}\{namebot}') and os.path.isfile(fr'{path}\{namebot}\config.py'):
                readconfig = open(fr'{path}\{namebot}\config.py', 'r', encoding='utf-8').read()
                try:
                    name_system_payments = str(arg).split(' --')[1].rstrip().strip()
                except IndexError:
                    pass
                if os.path.exists(fr'{path}\{namebot}\backend\payments') == False:
                    os.mkdir(fr'{path}\{namebot}\backend\payments')
                if name_system_payments == 'qiwi':
                    if 'class Qiwi_p2p:' not in readconfig:
                        #########CHANGE CONFIG
                        open(fr'{path}\{namebot}\config.py', 'a', encoding='utf-8').write(f'\n\n{templates.readTemplates("backend.payments.config.qiwi")}')
                        ##########ADD FILES AND BACKEND\PAYMENTS#############
                        os.mkdir(fr'{path}\{namebot}\backend\payments\qiwi_p2p')
                        open(fr'{path}\{namebot}\backend\payments\qiwi_p2p\__init__.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.qiwi.init"))
                        open(fr'{path}\{namebot}\backend\payments\qiwi_p2p\P2P.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.qiwi.p2p"))
                        open(fr'{path}\{namebot}\backend\payments\qiwi_p2p\P2P_Keys.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.qiwi.p2p_keys"))
                        #######################
                    else: print('Error: This type of payment has already been added to the bot modules!')
                elif name_system_payments == 'yoomoney':
                    if 'class Yoomoney:' not in readconfig:
                        #########CHANGE CONFIG
                        open(fr'{path}\{namebot}\config.py', 'a', encoding='utf-8').write(f'\n\n{templates.readTemplates("backend.payments.config.ymPay")}')
                        ##########ADD FILES AND BACKEND\PAYMENTS#############
                        os.mkdir(fr'{path}\{namebot}\backend\payments\ymPay')
                        open(fr'{path}\{namebot}\backend\payments\ymPay\__init__.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.ymPay.init"))
                        open(fr'{path}\{namebot}\backend\payments\ymPay\client.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.ymPay.client"))
                        open(fr'{path}\{namebot}\requirements.txt', 'a+', encoding='utf-8').write('yoomoney\n')
                        #######################
                    else: print('Error: This type of payment has already been added to the bot modules!')
                elif name_system_payments == 'crystalPay':
                    if 'class Crystal_Pay:' not in readconfig:
                        #########CHANGE CONFIG
                        open(fr'{path}\{namebot}\config.py', 'a', encoding='utf-8').write(f'\n\n{templates.readTemplates("backend.payments.config.crystalPay")}')
                        ##########ADD FILES AND BACKEND\PAYMENTS#############
                        os.mkdir(fr'{path}\{namebot}\backend\payments\crystalPay')
                        open(fr'{path}\{namebot}\backend\payments\crystalPay\__init__.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.crystalPay.init"))
                        open(fr'{path}\{namebot}\backend\payments\crystalPay\client.py', 'w', encoding='utf-8').write(templates.readTemplates("backend.payments.crystalPay.client"))
                        #######################
                    else: print('Error: This type of payment has already been added to the bot modules!')
                else:
                    print('Error: This type of payment module is not supported by the system!')
            else:
                print('Error: A bot with that name was not found!')

        else:
            print('Error: This path does not exist!')
    else:
        print('Error: The path to the folder for creating the bot has not yet been configured!')

async def bot_state_add(arg): #bot_states.add -@ NAMEBOT --group:admin(panel, enterData, enterPassword)
    global STORAGE
    namebot = None
    name_group = None
    _states = None
    path = STORAGE._dir_
    if path != None:
        if os.path.exists(path):
            try:
                namebot = str(arg).split('-@ ')[1].split(' ')[0].rstrip().strip()
            except IndexError:
                print('Error: The name of the bot should be specified like this: -@ NAMEBOT')
                return
            if os.path.exists(fr'{path}\{namebot}') and os.path.isfile(fr'{path}\{namebot}\config.py') and os.path.exists(fr'{path}\{namebot}\states'):
                if os.path.isfile(fr'{path}\{namebot}\states\__init__.py') == False:
                    open(fr'{path}\{namebot}\states\__init__.py', 'w', encoding='utf-8').write('')
                try:
                    name_group = str(arg).split(' --group:')[1].split('(')[0].strip().rstrip()
                    _states = str(arg).split('(')[1].split(')')[0].split(',')
                except IndexError:
                    print('Error: The name of the group and the name of the states should be specified as follows: --group:NAMEGROUP(state, state,state)')
                    return
                if name_group and name_group.isalpha():
                    if os.path.isfile(fr'{path}\{namebot}\states\state_{name_group}.py') == False:
                        status = True
                        for _state in _states:
                            _state = _state.rstrip().strip()
                            if _state.isalpha():
                                pass
                            else:
                                status = False
                                break
                        if status:
                            open(fr'{path}\{namebot}\states\__init__.py', 'a+', encoding='utf-8').write(f'from .state_{name_group} import state_{name_group}\n')
                            open(fr'{path}\{namebot}\states\state_{name_group}.py', 'w', encoding='utf-8').write\
(f"""from aiogram.dispatcher.filters.state import State, StatesGroup

class state_{name_group}(StatesGroup):""")
                            for _state in _states:
                                _state = _state.rstrip().strip()
                                open(fr'{path}\{namebot}\states\state_{name_group}.py', 'a+', encoding='utf-8').write(f'\n    {_state} = State()')
                            return
                    else:
                        print('Error: A state with this name is already in the bot!')
                    print('Error: There should be no special characters in the name of the group or states!')
            else:
                print('Error: A bot with that name was not found!')
        else:
            print('Error: This path does not exist!')
    else:
        print('Error: The path to the folder for creating the bot has not yet been configured!')

def help():
    print('\nAll commands:\n'
          '---------------------------------------------------------------------------------------------------------------\n'
          'dir "%path%" - Selecting the directory where the bot folder will be stored.\n'
          'bot_create -@ %namebot% - Creating a bot in the current directory.\n'
          'bot_payments -@ %namebot% --qiwi | --yoomoney | --crystalPay - Adding a payment module to the bot structure.\n'
          'bot_states.add -@ %namebot% --group:%namegroup%(%namestate%, %namestate%, ...) - Creating a state group.\n'
          'exit - Exiting the framework.\n'
          '---------------------------------------------------------------------------------------------------------------\n')

def c_exit():
    exit()