class Mokhtalet():
    def __init__(self, r, i):
        self.real = r
        self.image = i

    def pluss(self, m2):
        new_real = self.real + m2.real
        new_image = self.image + m2.image
        result = Mokhtalet(new_real, new_image)
        return result

    def subs(self, m2):
        r = self.real - m2.real
        mi = self.image - m2.image
        result = Mokhtalet(r, mi)
        return result

    def mulss(self, m2):
        n = self.real * m2.real - self.image * m2.image
        mi = self.real * m2.image + self.image * m2.real
        result = Mokhtalet(n, mi)
        return result
          
    def show(self):
        print(self.real, "+", self.image, "i")