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
        print('Error: Specify the path to the folder to create the bot in " "')