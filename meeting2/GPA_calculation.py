gpa = 0
Count = 0
while True:
    equal = input(" Enter the student's exam score : ")
    if str(equal) == "exit":
        break    

    else:
        number = float(equal)
        gpa = number + gpa
        Count += 1

print("GPA is : ",gpa / Count)        