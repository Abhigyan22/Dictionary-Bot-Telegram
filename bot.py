import telebot
import os
from dict import *
bot = telebot.TeleBot(os.environ.get('DICT_BOT_API_KEY'))
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.reply_to(message, f"""Hello {message.chat.first_name} I am Dictionary Bot :) You can send me any English word and I will send you its meaning. Thanks For Using :)""")

@bot.message_handler(commands=["about"])
def start_command(message):
    bot.reply_to(message, f"""For now I can only give you the meanings of words but I am being constantly updated bu @Zoldyck_kil :)""")

@bot.message_handler(func=lambda msg: len(msg.text.split(" "))>=2)
def invalid_message(message):
    bot.reply_to(message, "Please send me ONLY ONE valid english word at a time")

@bot.message_handler(func=lambda msg : len(msg.text.split(" "))==1)
def get_meaning_of_word(message):
    meaning = get_meaning(message.text)
    if meaning:
        bot.reply_to(message, meaning)

    else:
        bot.reply_to(message, "Sorry but I could not find its meaning. Maybe you have a spelling mistake, please recheck")

bot.polling()
