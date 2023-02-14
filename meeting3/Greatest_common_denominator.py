Divisor_1 = []
Divisor_2 = []
Divisor_3 = []

number_1 = int(input(" enter number 1 : "))
number_2 = int(input(" enter number 2 : "))



for i in range(1, number_1 + 1):
	if number_1 % i == 0:
		Divisor_1.append(i)

for i in range(1, number_2 + 1):
	if number_2 % i == 0:
		Divisor_2.append(i)


for p in range(len(Divisor_1)):
	for j in range(len(Divisor_2)):
		if Divisor_1[p] == Divisor_2[j]:
			Divisor_3.append(Divisor_1[p])

for	q in range(len(Divisor_3)):
	if Divisor_3[0] < Divisor_3[q]:
		Divisor_3[0] = Divisor_3[q]

print(" The greatest common denominator is equal to : ", Divisor_3[0])






