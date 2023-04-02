class Media:
    def __init__(self, dast, name, k, ims, ul, du, ca):
        daste = dast
        name_media = name
        # kargardan
        director = k
        # emtiaz film 
        imdb_score = ims
        url = ul
        # time film
        duration = du  
        # bazigar 
        casts = ca

    def show_info(self):
        print("daste : ", self.daste, "name media : ", self.name_media, "kargardan : ", self.director, "IMDB score : ", self.imdb_score, end="")
        print("time media : ", self.duration)

    def download(self):
        ...

    def search_plus(self, time_1, time_2):
        if self.duration > time_1 and self.duration < time_2:
            self.show_info()

    def search_name(self, name):
        if name == self.name_media:
            self.show_info() 

    def search_kargardan(self, name):
         if name == self.director:
            self.show_info()    