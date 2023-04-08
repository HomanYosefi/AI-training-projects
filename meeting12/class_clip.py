from class_mdia import Media

class Clip(Media):
    def __init__(self, dast, name, k, ims, ul, du, ca, like):
        super().__init__(dast, name, k, ims, ul, du, ca)
        number_like = like 