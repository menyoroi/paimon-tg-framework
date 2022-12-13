import os
from loader import STORAGE
import templates
import sqlite3
import asyncio

async def bot_settings(arg):
    global STORAGE
    namebot = None
    par = None
    value = None
    path = STORAGE._dir_
    if path != None:
        if os.path.exists(path):
            try:
                namebot = str(arg).split('-@ ')[1].split(' ')[0]
            except IndexError:
                print('Error: The name of the bot should be specified like this: -@ NAMEBOT')
                return
            if namebot.isalpha():
                if os.path.exists(fr'{path}\{namebot}') and os.path.isfile(fr'{path}\{namebot}\config.py'):
                    try:
                        par = str(arg).split('--')[1].split('=')[0]
                    except IndexError:
                        print('Error: The parameter is specified incorrectly. Specify the parameter after --')
                        return
                    try:
                        value = str(arg).split('--')[1].split('=')[1]
                    except IndexError:
                        print('Error: Parameter value not specified!')
                        return
                    if par == 'token' and value:
                        with open(fr'{path}\{namebot}\config.py', 'r', encoding='utf-8') as file:
                            config_lines = file.readlines()
                        with open(fr'{path}\{namebot}\config.py', 'r', encoding='utf-8') as file:
                            config_read = file.read()
                        for line in config_lines:
                            if 'bot_token =' in line:
                                new_config = config_read.replace(f'{line}', f'bot_token = "{value}"')
                                with open(fr'{path}\{namebot}\config.py', 'w', encoding='utf-8') as file:
                                    file.write(new_config)
                                break
                    else:
                        print('Error: This parameter is not supported or you have not specified the parameter value!')

                else:
                    print('Error: A bot with that name was not found!')
            else:
                print('Error: Do not specify symbols and other signs in the name !')
        else:
            print('Error: This path does not exist!')
    else:
        print('Error: The path to the folder for creating the bot has not yet been configured!')