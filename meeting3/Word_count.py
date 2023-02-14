text = input(" enter text : ")

space = 1
for i in range(len(text)):
    if text[i] == " " and text[i - 1] != " ":
        space += 1


print(" The number of words in the sentence are : ", space)        