from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('testing')
bot.set_trainer(ListTrainer)
for _file in os.listdir('conversations'):
    conv =  open('conversations/' + _file, 'r').readlines()
    bot.train(conv)
while True:
    request = input('You : ')
    response = bot.get_response(request)
    print('Bot : ', response)
    if response == 'take care':
        break
