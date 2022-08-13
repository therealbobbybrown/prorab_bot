#библиотеки, которые загружаем извне
import telebot
TOKEN = '5449464808:AAGjnK5OxwCUew1i9o6CYklpP-xZsH7J6Do'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("👷‍ Кто я такой")
	item2 = types.KeyboardButton("💸 Будешь должен")
	item3 = types.KeyboardButton("🕙 Определись уже")
	item4 = types.KeyboardButton("🧡 Репо моего раба")
	item5 = types.KeyboardButton("😋 Написать рабу")

	markup.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Здаров, это прораб. А ты, похоже -  {0.first_name} ... хм. \nТы там на кнопочки-то понажимай, только особо не шикуй!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':

		if message.text == '👷‍ Кто я такой':
			bot.send_message(message.chat.id, ' Так ты почитай 👉 http://www.aup.ru/docs/d2/78.htm')

		elif message.text == '💸 Будешь должен':
			bot.send_message(message.chat.id, 'Если договоримся - порвусь, но кандидата найду!')

		elif message.text == '🕙 Определись уже':
			bot.send_message(message.chat.id, 'Часики-то тикают - время убегает. Давай, по рукам и разбежались!')	

		elif message.text == '🧡 Репо моего раба':
			bot.send_message(message.chat.id, 'От сердца отрываю вот этого человечка https://github.com/therealbobbybrown')

		elif message.text == '😋 Написать рабу':
			bot.send_message(message.chat.id, 'Ты только скажи что от меня https://t.me/yuriustinov')

		else:
			bot.send_message(message.chat.id, 'Что-то моя твою не понимает... \n Давай-ка лучше хряпнем по сотке 🍶')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
