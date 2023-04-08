from class_mdia import Media

class Documentary(Media):
    def __init__(self, dast, name, k, ims, ul, du, ca, sub):
        super().__init__(dast, name, k, ims, ul, du, ca)
        subject = sub