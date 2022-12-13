def readTemplates(name:str):
    response = None
    #####ROOT BOT FILES######
    if name == 'config':
        response = open('templates/config.txt', 'r', encoding='utf-8').read()
    elif name == 'main':
        response = open('templates/main.txt', 'r', encoding='utf-8').read()
    elif name == 'loader':
        response = open('templates/loader.txt', 'r', encoding='utf-8').read()
    ##########################

    ##############DB_MODULES#########
    elif name == 'backend.database.init':
        response = open('templates/backend/database/__init__.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.database.bills':
        response = open('templates/backend/database/bills.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.database.users':
        response = open('templates/backend/database/users.txt', 'r', encoding='utf-8').read()

    ##########HANDLERS############
    elif name == 'handlers.init':
        response = open('templates/handlers/__init__.txt', 'r', encoding='utf-8').read()
    elif name == 'handlers.error':
        response = open('templates/handlers/error.txt', 'r', encoding='utf-8').read()
    elif name == 'handlers.users.init':
        response = open('templates/handlers/users/__init__.txt', 'r', encoding='utf-8').read()
    elif name == 'handlers.users.start':
        response = open('templates/handlers/users/start.txt', 'r', encoding='utf-8').read()
    ##########PAYMENTS##############
    #CONFIGS
    elif name == 'backend.payments.config.qiwi':
        response = open('templates/backend/payments/config/qiwi.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.payments.config.ymPay':
        response = open('templates/backend/payments/config/yoomoney.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.payments.config.crystalPay':
        response = open('templates/backend/payments/config/crystalPay.txt', 'r', encoding='utf-8').read()
    #QIWIP2P
    elif name == 'backend.payments.qiwi.init':
        response = open('templates/backend/payments/qiwi_p2p/__init__.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.payments.qiwi.p2p':
        response = open('templates/backend/payments/qiwi_p2p/P2P.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.payments.qiwi.p2p_keys':
        response = open('templates/backend/payments/qiwi_p2p/P2P_Keys.txt', 'r', encoding='utf-8').read()
    #CRYSTALPAY
    elif name == 'backend.payments.crystalPay.init':
        response = open('templates/backend/payments/crystalPay/__init__.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.payments.crystalPay.client':
        response = open('templates/backend/payments/crystalPay/client.txt', 'r', encoding='utf-8').read()
    #YMPAY
    elif name == 'backend.payments.ymPay.init':
        response = open('templates/backend/payments/ymPay/__init__.txt', 'r', encoding='utf-8').read()
    elif name == 'backend.payments.ymPay.client':
        response = open('templates/backend/payments/ymPay/client.txt', 'r', encoding='utf-8').read()

    return response