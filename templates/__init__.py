def readTemplates(name:str):
    response = None
    #####ROOT BOT FILES######
    if name == 'config':
        with open('templates/config.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'main':
        with open('templates/main.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'loader':
        with open('templates/loader.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    ##########################

    ##############DB_MODULES#########
    elif name == 'backend.database.init':
        with open('templates/backend/database/__init__.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.database.bills':
        with open('templates/backend/database/bills.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.database.users':
        with open('templates/backend/database/users.txt', 'r', encoding='utf-8') as file:
            response = file.read()

    ##########HANDLERS############
    elif name == 'handlers.init':
        with open('templates/handlers/__init__.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'handlers.error':
        with open('templates/handlers/error.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'handlers.users.init':
        with open('templates/handlers/users/__init__.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'handlers.users.start':
        with open('templates/handlers/users/start.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    ##########PAYMENTS##############
    #CONFIGS
    elif name == 'backend.payments.config.qiwi':
        with open('templates/backend/payments/config/qiwi.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.payments.config.ymPay':
        with open('templates/backend/payments/config/yoomoney.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.payments.config.crystalPay':
        with open('templates/backend/payments/config/crystalPay.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    #QIWIP2P
    elif name == 'backend.payments.qiwi.init':
        with open('templates/backend/payments/qiwi_p2p/__init__.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.payments.qiwi.p2p':
        with open('templates/backend/payments/qiwi_p2p/P2P.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.payments.qiwi.p2p_keys':
        with open('templates/backend/payments/qiwi_p2p/P2P_Keys.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    #CRYSTALPAY
    elif name == 'backend.payments.crystalPay.init':
        with open('templates/backend/payments/crystalPay/__init__.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.payments.crystalPay.client':
        with open('templates/backend/payments/crystalPay/client.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    #YMPAY
    elif name == 'backend.payments.ymPay.init':
        with open('templates/backend/payments/ymPay/__init__.txt', 'r', encoding='utf-8') as file:
            response = file.read()
    elif name == 'backend.payments.ymPay.client':
        with open('templates/backend/payments/ymPay/client.txt', 'r', encoding='utf-8') as file:
            response = file.read()

    return response