# get azlaee mosalass
zele_1 = float(input(" enter zele 1 : "))
zele_2 = float(input(" enter zele 2 : "))
zele_3 = float(input(" enter zele 3 : "))

# barresy sehat mosalass
if zele_1 <= 0 or zele_2 <= 0 or zele_3 <= 0 :
    print(" mosalass nist ")
elif zele_1 + zele_2 < zele_3 or zele_3 + zele_2 < zele_1 or zele_1 + zele_3 < zele_2 : 
    print(" mosalass nist ")
else :
    print(" true ")

