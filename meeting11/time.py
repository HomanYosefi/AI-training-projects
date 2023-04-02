class Time:
    def __init__(self, hh, mm, ss):
        self.h = hh
        self.m = mm
        self.s = ss

    def to_secend(self):
        result = (self.h * 3600) + (self.m * 60) + self.s
        return result

    @staticmethod
    def to_time(secend):
        hh, mm = 0, 0
        while True:
            if secend >= 3600: 
                hh += 1
                secend -= 3600
            
            else:
                break
        
        while True:
            if secend >= 60:
                mm += 1
                secend -= 60

            else:
                break

        result = Time(hh, mm, secend)
        return result

    def fix(self):
        help_box = self.to_secend()
        result = Time.to_time(help_box)
        self.h = result.h
        self.m = result.m
        self.s = result.s

    def show(self):
        print(self.h, ":", self.m, ":", self.s)  

    def minez(self, time2):
        secend_1 = self.to_secend()
        secend_2 = time2.to_secend()
        if secend_1 > secend_2:
            help_box = secend_1 - secend_2
            result = Time.to_time(help_box)
            return result

        else:
            print("zaman manfi vojod nadarad :| ")    

    def plus(self, time2):
        secend_1 = self.to_secend()
        secend_2 = time2.to_secend()
        help_box = secend_1 + secend_2
        result = Time.to_time(help_box)
        return result

    def to_gmt(self):
        self.h += 3
        self.m += 30


a = Time(5, 20, 17)
b = Time(2, 14, 27)

c = a.minez(b)

c.show()

