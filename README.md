# Paimon-tg-framework
Framework for creating a telegram bot structure. This framework was created to facilitate working with telegram bot structures. 
You can create a full-fledged structure for a bot in just a couple of lines.
# What is needed for the framework to work?
* Only Python 3.8 and higher.

# Commands for manage framework
```
dir "%path%" - Selecting the directory where the bot folder will be stored.
bot_create -@ %namebot% - Creating a bot in the current directory.
bot_settings -@ %namebot% --%parametr%=%value% - Configuring bot parameters. Available parameters: --token
bot_run -@ %namebot% - Launching the bot.
bot_payments -@ %namebot% --qiwi | --yoomoney | --crystalPay - Adding a payment module to the bot structure.
bot_states.add -@ %namebot% --group:%namegroup%(%namestate%, %namestate%, ...) - Creating a state group.
help - Help with commands.
exit - Exiting the framework.
```

# Creating your first bot through the framework
To begin with, open the framework via the terminal using the command:
```
cd paimon-tg-framework
python main.py
```
After that, we specify the directory to create a subdirectory with the bot structure:
```
paimon-tg-framework@None: dir "A:/"
paimon-tg-framework@A:/: 
```
The next step is to create a subdirectory with the bot structure:
```
paimon-tg-framework@A:/: bot_create -@ TEST #Specify the name of the subdirectory after -@.
paimon-tg-framework@A:/:
```
Excellent. Our bot has been created. Now we will specify our token in the settings and launch the bot:
```
paimon-tg-framework@A:/: bot_settings -@ TEST --token=your_token
paimon-tg-framework@A:/: bot_run -@ TEST
The bot is running!
```
Pre-install all the necessary libraries specified in the file requirements.txt.
