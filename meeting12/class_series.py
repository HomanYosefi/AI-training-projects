from class_mdia import Media

class Series(Media):
    def __init__(self, dast, name, k, ims, ul, du, ca, ep):
        super().__init__(dast, name, k, ims, ul, du, ca)
        episode = ep
    
        