import telebot
import wikipedia as w
w.set_lang('ru')

#print(w.summary('Сказка')[:200])

bot = telebot.TeleBot('5794007543:AAGwPfw8RCn6SyvgIdXVEluB5shZJD6D2CY')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Введите слово, которое хотите узнать")
    else:
        try:
            rez = w.search(message.text)
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            if len(rez) > 1:
                if message.text in rez:
                    rez.remove(message.text)
                for mess in rez:
                    btn1 = telebot.types.KeyboardButton(mess)
                    markup.add(btn1)
            bot.send_message(message.from_user.id, w.summary(message.text)[:200], reply_markup=markup)
        except Exception as e:
            print(e)
            bot.send_message(message.from_user.id, 'Я не нашёл такого в интернете')

bot.polling(none_stop = True, interval = 0)
