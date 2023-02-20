import qrcode

datasss = []

name = input(" enter your name : ")
number = int(input(" enter phone number : "))

datasss.append(name)
datasss.append(number)

img = qrcode.make(datasss)

img.save("data.png")
