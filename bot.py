from random import randint
from unittest import expectedFailure
import telebot

API_TOKEN = "Inserisci token Bot"

bot = telebot.TeleBot(API_TOKEN)

x = 0 #Variabile che prenderà il valore random

@bot.message_handler(commands=["start"])
def inizio_gioco(message):
    bot.send_message(message.chat.id, """\
Sto pensando a un numero da 1 a 10... 
Indovina qual è!
        """)
    bot.register_next_step_handler(message, indovina_numero())


def indovina_numero(message):
    x = randint(1,10)
    try:
        chat_id = message.chat.id
        input_text = message.text
    except Exception as e: 
        bot.send_message(chat_id, "C'è stato un errore!")

    if(str(input_text).isnumeric()):
        if(int(input_text) == x):
            bot.reply_to(message, "Hai indovinato!")
        else:
            bot.reply_to(message, "Non hai indovinato :( , il numero era " + str(x))
    else:
        bot.send_message(chat_id, "Non hai inviato un numero!")

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()


bot.polling(none_stop=True, interval=0)