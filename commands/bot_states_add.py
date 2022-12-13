import os
from loader import STORAGE
import templates
import sqlite3

async def bot_states_add(arg): #bot_states.add -@ NAMEBOT --group:admin(panel, enterData, enterPassword)
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
                    with open(fr'{path}\{namebot}\states\__init__.py', 'w', encoding='utf-8') as file:
                        file.write('')
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
                            with open(fr'{path}\{namebot}\states\__init__.py', 'a+', encoding='utf-8') as file:
                                file.write(f'from .state_{name_group} import state_{name_group}\n')
                            with open(fr'{path}\{namebot}\states\state_{name_group}.py', 'w', encoding='utf-8') as file:
                                file.write\
(f"""from aiogram.dispatcher.filters.state import State, StatesGroup

class state_{name_group}(StatesGroup):""")
                            for _state in _states:
                                _state = _state.rstrip().strip()
                                with open(fr'{path}\{namebot}\states\state_{name_group}.py', 'a+', encoding='utf-8') as file:
                                    file.write(f'\n    {_state} = State()')
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