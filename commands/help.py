def help():
    print('\nAll commands:\n'
          '---------------------------------------------------------------------------------------------------------------\n'
          'dir "%path%" - Selecting the directory where the bot folder will be stored.\n'
          'bot_create -@ %namebot% - Creating a bot in the current directory.\n'
          'bot_settings -@ %namebot% --%parametr%=%value% - Configuring bot parameters. Available parameters: --token\n'
          'bot_run -@ %namebot% - Launching the bot.\n'
          'bot_payments -@ %namebot% --qiwi | --yoomoney | --crystalPay - Adding a payment module to the bot structure.\n'
          'bot_states.add -@ %namebot% --group:%namegroup%(%namestate%, %namestate%, ...) - Creating a state group.\n'
          'exit - Exiting the framework.\n'
          '---------------------------------------------------------------------------------------------------------------\n')