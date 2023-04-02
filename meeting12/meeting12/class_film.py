from class_mdia import Media 

class Film(Media):
    def __init__(self, dast, name, k, ims, ul, du, ca, age, si, zhan, date):
        super().__init__(dast, name, k, ims, ul, du, ca)
        age_of_viewers = age
        silent = si  # true or false
        zhanr = zhan
        date_of_release = date
        
    def show(self):
        print("\n\n\n\nname media : ", self.name_media)
        print("director : ", self.director)
        print("imdb_score : ", self.imdb_score)
        print("duration : ", self.duration)
        print("casts : ", self.casts)
        print("age_of_viewers : ", self.age_of_viewers)
        print("silent : ", self.silent)
        print("zhanr : ", self.zhanr)
        print("date_of_release : ", self.date_of_release)


    # def         

