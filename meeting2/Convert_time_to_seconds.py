time = input(" Enter the time like this ( hh:mm:ss) : ")
second = 0
hour = int(time[0: 2])
min = int(time[3: 5])
sec = int(time[6: 9])

second = sec + (min * 60) + (hour * 3600)


print(" The time was converted into seconds and the answer is equal to: ", second)
