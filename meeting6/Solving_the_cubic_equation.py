from os import _exit
import math

print("\n\n Third degree equation solution program: With this program, you can find the roots of a third degree equation \n\n\n")
print(" a*x^3 + b*x^2 + c*x + d = 0")
a = int(input(" enter a : "))
b = int(input(" enter b : "))
c = int(input(" enter c : "))
d = int(input(" enter d : "))

if a == 0:
    print(" You have considered the variable number (a) to be zero, which is not a quadratic equation")
    exit()

p = b - (a^2)/3
q = ((2*a^3)/27) - (a*b/3) + c

delta = ((q**2)/4) + ((p**3)/27)
 

if delta > 0:
    x = math.pow((-q/2) + math.sqrt(delta), (1/3)) + math.pow(((-q/2) - math.sqrt(delta)), (1/3)) - a/3
elif delta == 0:
    ...
elif delta < 0:
    ...       