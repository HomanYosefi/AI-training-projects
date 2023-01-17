vazn = float(input(" enter vazn : "))
ghad = float(input(" enter ghad (metr): "))

bmi = vazn / (ghad * ghad)
print (bmi)
if bmi < 18.5 : 
    print(" underweght")
elif 18.5 <= bmi and bmi < 25:
    print(" Normal")
elif 25 <= bmi and bmi < 30:
    print(" Overweight")
elif 30 <= bmi and bmi < 35:
    print(" odesity")
elif 35 <= bmi and bmi < 40:
    print(" extreme obesity")