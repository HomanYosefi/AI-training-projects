class Kasr: 
    def __init__(self, s, m):
        self.sorat = s
        self.makhraj = m

    def xarb(self, kasr2):
        result_s = (self.sorat * kasr2.sorat)
        result_m = self.makhraj * kasr2.makhraj
        result = Kasr(result_s, result_m)
        return result

    def jame(self, kasr2):
        result_s = (self.sorat * kasr2.makhraj) + (kasr2.sorat * self.makhraj)
        result_m = self.makhraj * kasr2.makhraj
        result = Kasr(result_s, result_m)
        return result

    def tafrigh(self, kasr2):
        result_s = (self.sorat * kasr2.makhraj) - (kasr2.sorat * self.makhraj)
        result_m = self.makhraj * kasr2.makhraj
        result = Kasr(result_s, result_m)
        return result

    def taghsim(self, kasr2):
        result_s = (self.sorat * kasr2.makhraj)
        result_m = self.makhraj * kasr2.sorat
        result = Kasr(result_s, result_m)
        return result

    def sade_kon(self):
        if self.sorat > self.makhraj:
            min = self.makhraj

        else:
            min = self.sorat

        for i in range(min, 1, -1):
            if (self.sorat % i == 0) and (self.makhraj % i == 0):
                self.sorat = self.sorat / i
                self.makhraj = self.makhraj / i
                break
            else:
                print("kasr sade nemishavad")

    def show(self):
        print(self.sorat, "/", self.makhraj)

    def convert_to_number(self):
        result = self.sorat / self.makhraj
        return result    




a = Kasr(3, 4)      
b = Kasr(2, 3)  
c = a.xarb(b)
c.show()