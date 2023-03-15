from random import randint
import telebot


bot = telebot.TeleBot("TOKEN", parse_mode=None)


markup = telebot.types.ReplyKeyboardMarkup(row_width=5)
key_1 = telebot.types.KeyboardButton('a')
key_2 = telebot.types.KeyboardButton('b')
key_3 = telebot.types.KeyboardButton('c')
key_4 = telebot.types.KeyboardButton('d')
key_5 = telebot.types.KeyboardButton('e')
key_6 = telebot.types.KeyboardButton('f')
markup.add(key_1, key_2, key_3, key_4, key_5, key_6)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "سلام دوست من به ربات من خوش اومدی 😃😃😃")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# bot.reply_to(message, "این یک پیان عادی است")
    if message.text == "سلام":
        bot.send_message(message.chat.id, "سلام دوست من ,من اماده خدمت رسانی به شما هستم")

    elif message.text == "خوبی؟":
        bot.send_message(message.chat.id, "من خوبم اگر شما خوب باشید")

    elif message.text == "دوستت دارم":
        bot.send_message(message.chat.id, "من هم شما را دوست دارم 🫂")

    else:
        bot.send_message(message.chat.id, "این پیام در دیتا بیس من وجود ندارد", reply_markup=markup)    


@bot.message_handler(commands=["guess_number"])
def beggin_game(message):
    global number 
    global number_of_guesses
    global user_number

    number = randint(0, 100)
    number_of_guesses = 1
    user_number = bot.send_message(message.chat.id, "بازی  حدس عدد شروع شد و  یک عدد از بین صفر تا صد انتخاب شده ... شما باید از ربات راهنمایی بخواهید تا بتوانید عدد را حدس بزنید")
    bot.register_next_step_handler()

def guess_number(message):
        
    if user_number < number:
        print(" choose a higher number ")
        number_of_guesses += 1



# photo = open('/tmp/photo.png', 'rb')
# tb.send_photo(chat_id, photo)



bot.infinity_polling()    