import commands


async def lexer(c):
    lex=''
    arg=''
    l=True
    for i in c:
        if i==' ' and l:
            l=False
        elif l:
            lex+=i
        else:
            arg+=i
    return await execute(lex,arg)


async def execute(lex, arg):
    if lex == 'dir':
        await commands.select_dir(arg)
    elif lex == 'bot_create':
        await commands.bot_create(arg)
    elif lex == 'bot_payments':
        await commands.bot_payments(arg)
    elif lex == 'bot_states.add':
        await commands.bot_state_add(arg)
    elif lex == 'help':
        commands.help()
    elif lex == 'exit':
        commands.c_exit()
    else:
        print('Command not found!')