from telebot import *

web_url = "https://icafeorder.pythonanywhere.com/menu/2/"

bot = TeleBot("1895470821:AAGht_HFpTTBNZ4plfEykEmLS4cbky5B1W0")

@bot.message_handler(commands=['start'])
def Command_Start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Menu",web_app=types.WebAppInfo(web_url+str(message.from_user.id))))

    bot.send_message(message.from_user.id,"Assalomu aleykum:",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def CallBack(call):
    print(call.data)

bot.infinity_polling()