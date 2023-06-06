from telebot import *

web_url = "https://6f5e-185-139-137-101.ngrok-free.app/menu/2/"

bot = TeleBot("1895470821:AAGht_HFpTTBNZ4plfEykEmLS4cbky5B1W0")

@bot.message_handler(commands=['start'])
def Command_Start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Menu",web_app=types.WebAppInfo(web_url)))

    bot.send_message(message.from_user.id,"WebApp here:",reply_markup=markup)

bot.infinity_polling()