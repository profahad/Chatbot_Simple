from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
bot.set_trainer(ListTrainer)
for _file in os.listdir('conversations'):
    conv =  open('conversations/' + _file, 'r').readlines()
    bot.train(conv)
while True:
    request = input('You : ')
    if request.strip() != 'Bye':
        response = bot.get_response(request)
        print('Bot : ', response)
    elif request.strip() == 'Bye':
        print('Bot : ', 'Bye')
        break
