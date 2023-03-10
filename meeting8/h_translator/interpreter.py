import os
import gtts

output = ""

def read_from_file():
    result = os.listdir("meeting\AI-training-projects\meeting8\h_translator")
    if "h_translate.txt" not in result:
        print(" not file translate ")
        exit(0)
    global words_bank
    f = open("meeting\AI-training-projects\meeting8\h_translator\h_translate.txt", "r")
    temp = f.read().split("\n")

    words_bank = []

    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i + 1]}
        words_bank.append(my_dict)

    f.close()

def english_to_farsi():
    user_text = input("enter your english text : ")
    

    user_words = user_text.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                # print(word["fa"], end=" ")
                output = output + word["fa"] + " "
                break
        else:
            # print(user_word, end=" ")
            output = output + user_word + " "

    print(output)  
    khondan("en")      


def farsi_to_english():
    user_text = input("enter your farsi text : ")

    user_words = user_text.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                # print(word["en"], end=" ")
                output = output + word["en"] + " "
                break
        else:
            # print(user_word, end=" ")
            output = output + user_word + " "

    print(output)
    khondan("ar")


def khondan(langeg):
    voice = gtts.gTTS(output, lang=langeg, slow=False)    
    voice.save("meeting\AI-training-projects\meeting8\h_translator\h_voice.mp3")


read_from_file()

print("[1]-- english to farsi")
print("[2]-- farsi to english ")

list_translate = int(input(" enter number of list : "))

if list_translate == 1:
    english_to_farsi()

elif list_translate == 2:
    farsi_to_english()