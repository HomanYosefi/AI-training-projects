from class_mdia import Media

class Actor(Media):
    def __init__(self, dast, name, k, ims, ul, du, ca, n, ag, last, jens, character):
        super().__init__(dast, name, k, ims, ul, du, ca)
        name_actor = n
        age = ag
        last_name = last
        jensiat = jens
        shakhsiat = character # bad , good , npc

    def show_actor(self):
        print("name : ", self.name_actor, "lastname : ", self.last_name, "age : ", self.age, "jensiat : ", self.jensiat, "naghsh to film : ", self.shakhsiat)
    