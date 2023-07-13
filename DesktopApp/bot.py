from Desktop import webapi,init_sql,conf
import flet
from telebot import *

bot = TeleBot(conf.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def Command_Start(message):
	user = message.from_user.id
	start_text = init_sql.get_data()['start']
	webapi.start_user(user)
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Menyu",web_app=types.WebAppInfo(webapi.WEB_URL+str(user))))

	bot.send_message(user,start_text,reply_markup=markup,parse_mode='HTML')

@bot.message_handler(commands=['about'])
def Command_About(message):
	user = message.from_user.id
	about_text = init_sql.get_data()['about']
	webapi.start_user(user)

	bot.send_message(user,about_text,parse_mode='HTML')



@bot.callback_query_handler(func=lambda call: True)
def CallBack(call):
	print(call.data)


# bot.infinity_polling()
# bot.stop_polling()