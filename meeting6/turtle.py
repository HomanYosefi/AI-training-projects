import turtle

size_big = 10
sizes = 5

turtle.bgcolor('grey')
pet = turtle.Pen()

turtle.bgcolor("black")
pet.width(3)
pet.left(150)
pet.pencolor('green')
for i in range(3, 12):
    hight = (((i - 2) * 180) / i) - 180
    pet.pencolor('green')
    for j in range(i):
        pet.forward(41 + size_big)
        pet.right(hight)
    pet.pencolor('black')
    pet.right(110)
    pet.forward(12.5 + sizes)
    pet.left(110)
    size_big += 15
    sizes += 5



turtle.done()