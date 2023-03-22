import telebot
import random
import gtts
import qrcode


bot = telebot.TeleBot(
	"TOKEN", parse_mode=None)


markup = telebot.types.ReplyKeyboardMarkup(row_width=7)
key_1 = telebot.types.KeyboardButton('/start')
key_2 = telebot.types.KeyboardButton('/help')
key_3 = telebot.types.KeyboardButton('/guess_number')
key_4 = telebot.types.KeyboardButton('/help')
key_5 = telebot.types.KeyboardButton('/guess number')
key_6 = telebot.types.KeyboardButton('/text_to_voice')
key_7 = telebot.types.KeyboardButton('/max')
key_8 = telebot.types.KeyboardButton('/argmax')
key_9 = telebot.types.KeyboardButton('/qrcode')
markup.add(key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "سلام به ربات من خوش اومدی ", reply_markup=markup)


@bot.message_handler(commands=['guess_number'])
def guess_number(message):
    secret_number = random.randint(1, 100)
    bot.send_message(
        message.chat.id, "I'm thinking of a number between 1 and 100. Can you guess what it is?")

    @bot.message_handler(func=lambda m: True)
    def handle_guess(message):
        try:
            guess = int(message.text)
            if guess == secret_number:
                bot.send_message(
                    message.chat.id, "Congratulations! You guessed my number.", reply_markup=markup)
                bot.remove_message_handler(handle_guess)
            elif guess < secret_number:
                bot.send_message(
                    message.chat.id, "Too low. Try again with a higher number.")
            else:
                bot.send_message(
                    message.chat.id, "Too high. Try again with a lower number.")
        except ValueError:
            bot.send_message(
                message.chat.id, "Please enter an integer between 1 and 100.")

    # Add this handler so that it listens for guesses until the correct answer is given
    bot.add_message_handler(handle_guess)


@bot.message_handler(commands=['text_to_voice'])
def convert_voice(message):
    bot.send_message(
        message.chat.id, "Please enter English text so that the robot can convert it into voice : ")

    @bot.message_handler(func=lambda m: True)
    def get_voice(message):
        try:
            voice = gtts.gTTS(message.text, lang="en", slow=False)
            bot.send_audio(message.chat_id, voice)
        except:
            bot.send_message(
            	message.chat.id, "An error occurred in the system. Please try again")


@bot.message_handler(commands=['max'])
def max_number(message):
    max_list = []
    bot.send_message(
    	message.chat.id, "Please enter the numbers one by one and when your list of numbers is finished, enter the word ##.")

    @bot.message_handler(func=lambda m: True)
    def enter_number(message):
        try:
            if message.text != '##':
                max_list.append(int(message.text))
                bot.add_message_handler(enter_number)
        except:
            print(" bug max number")
    maximom = max_list[0]
    for number in max_list:
        if maximom < number:
            maximom = number

    bot.send_message(
    	message.chat.id, f"big number is : {maximom}", reply_markup=markup)


@bot.message_handler(commands=['argmax'])
def max_numbers(message):
    max_lists = []
    bot.send_message(
    	message.chat.id, "Please enter the numbers one by one and when your list of numbers is finished, enter the word ##.")

    @bot.message_handler(func=lambda m: True)
    def enter_numbers(message):
        try:
            if message.text != '##':
                max_lists.append(int(message.text))
                bot.add_message_handler(enter_numbers)

        except:
            print(" bug max number andiss")
    maximom = max_lists[0]
    for number in len(max_lists):
        if maximom < max_lists[number]:
            maximom = max_lists[number]
            andiss = number

    bot.send_message(
    	message.chat.id, f"andiss number is : {andiss}", reply_markup=markup)


@bot.message_handler(commands=["qrcode"])
def qrcodes(message):
    bot.send_message(
    	message.chat.id, "Please enter the desired text so that the robot will convert it into a QR code")

    @bot.message_handler(func=lambda m: True)
    def make_qr(message):
        msg = message.text
        img = qrcode.make(msg)
        img.save("qrcode.png")
        f = open("qrcode.png", 'rb')
        bot.send_photo(message, f)


bot.infinity_polling()
