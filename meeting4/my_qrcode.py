import qrcode


datasss = []

name = input(" enter your name : ")
number = int(input(" enter phone number : "))

# data = (f" name is : {name}  phone number : {number}")
datasss.append(name)
datasss.append(number)

img = qrcode.make(datasss)

img.save("data.png")
