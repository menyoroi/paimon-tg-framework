import os
from loader import STORAGE
import templates
import sqlite3

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
                        with open(fr'{path}\{namebot}\config.py', 'a', encoding='utf-8') as file:
                            file.write(f'\n\n{templates.readTemplates("backend.payments.config.qiwi")}')
                        ##########ADD FILES AND BACKEND\PAYMENTS#############
                        os.mkdir(fr'{path}\{namebot}\backend\payments\qiwi_p2p')
                        with open(fr'{path}\{namebot}\backend\payments\qiwi_p2p\__init__.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.qiwi.init"))
                        with open(fr'{path}\{namebot}\backend\payments\qiwi_p2p\P2P.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.qiwi.p2p"))
                        with open(fr'{path}\{namebot}\backend\payments\qiwi_p2p\P2P_Keys.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.qiwi.p2p_keys"))
                        #######################
                    else: print('Error: This type of payment has already been added to the bot modules!')
                elif name_system_payments == 'yoomoney':
                    if 'class Yoomoney:' not in readconfig:
                        #########CHANGE CONFIG
                        with open(fr'{path}\{namebot}\config.py', 'a', encoding='utf-8') as file:
                            file.write(f'\n\n{templates.readTemplates("backend.payments.config.ymPay")}')
                        ##########ADD FILES AND BACKEND\PAYMENTS#############
                        os.mkdir(fr'{path}\{namebot}\backend\payments\ymPay')
                        with open(fr'{path}\{namebot}\backend\payments\ymPay\__init__.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.ymPay.init"))
                        with open(fr'{path}\{namebot}\backend\payments\ymPay\client.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.ymPay.client"))
                        with open(fr'{path}\{namebot}\requirements.txt', 'a+', encoding='utf-8') as file:
                            file.write('yoomoney\n')
                        #######################
                    else: print('Error: This type of payment has already been added to the bot modules!')
                elif name_system_payments == 'crystalPay':
                    if 'class Crystal_Pay:' not in readconfig:
                        #########CHANGE CONFIG
                        with open(fr'{path}\{namebot}\config.py', 'a', encoding='utf-8') as file:
                            file.write(f'\n\n{templates.readTemplates("backend.payments.config.crystalPay")}')
                        ##########ADD FILES AND BACKEND\PAYMENTS#############
                        os.mkdir(fr'{path}\{namebot}\backend\payments\crystalPay')
                        with open(fr'{path}\{namebot}\backend\payments\crystalPay\__init__.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.crystalPay.init"))
                        with open(fr'{path}\{namebot}\backend\payments\crystalPay\client.py', 'w', encoding='utf-8') as file:
                            file.write(templates.readTemplates("backend.payments.crystalPay.client"))
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