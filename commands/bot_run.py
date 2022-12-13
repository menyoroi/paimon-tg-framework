import os
from loader import STORAGE
import templates
import sqlite3
import asyncio

async def bot_run(arg):
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
                if os.path.exists(fr'{path}\{namebot}') and os.path.isfile(fr'{path}\{namebot}\main.py'):
                    print('The bot is running!')
                    os.startfile(fr'{path}\{namebot}\main.py')
                else:
                    print('Error: A bot with that name was not found!')
            else:
                print('Error: Do not specify symbols and other signs in the name !')
        else:
            print('Error: This path does not exist!')
    else:
        print('Error: The path to the folder for creating the bot has not yet been configured!')