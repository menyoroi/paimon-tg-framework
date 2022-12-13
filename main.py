import asyncio
from utils import lexer
from loader import STORAGE



async def main():
    while True:
        global STORAGE
        stroke = input(f'paimon-tg-framework@{STORAGE._dir_}: ')
        await lexer(stroke)

if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
