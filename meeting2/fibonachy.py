number = int(input(" enter number : "))
num1 = 1
num2 = 1
print("1 , 1 , ",end='')
for i in range(2, number): 
    num3 = num1 + num2
    print(num3," , ", end='')
    num1 = num2
    num2 = num3


