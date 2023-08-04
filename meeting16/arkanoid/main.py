import random
import arcade


class Ball(arcade.Sprite):
    ...

class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__("bow.png")
        self.width = 100
        self.height = 20
        self.center_x = game.width // 2
        self.center_y = game.height // 8
        self.change_x = 0
        self.change_y = 0




class Enemy(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__()   
        self.width = (game.width - 100) // 8
        self.height = (game.width - 100) // 8
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        
class Enderman(Enemy):
    def __init__(self, game, x, y):
        super().__init__("enderman.jpg", game, x, y)


class Bow(Enemy):
    def __init__(self, game, x, y):
        super().__init__("bow.png", game, x, y)

class Octaopus(Enemy):
    def __init__(self, game, x, y):
        super().__init__("octaopus.jpg", game, x, y)

class Tnt(Enemy):
    def __init__(self, game, x, y):
        super().__init__("tnt.jpg", game, x, y)


class Game(arcade.Window):
    def __init__(self, width = 400, height = 800, title= 'arkanoid'):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.draw_enemy = 1
        self.tir = Rocket(self)
        self.bow = Bow(self, ..., ...)
        self.enderman = Enderman(self, ..., ...)
        self.octaopus = Octaopus(self, ..., ...)
        self.tnt = Tnt(self, ..., ...)
        self.enemy_list = [self.bow, self.enderman, self.octaopus, self.tnt]

    def on_update(self, delta_time: float):
        if self.draw_enemy == 1:
            self.draw_enemy = 0
            width_enemy = (self.width - 100) // 8
            y_list = [self.height - 100, self.height -
                      100 + width_enemy, self.height - 100 + width_enemy + width_enemy]
            for y in y_list:
                x = 50 + width_enemy // 2
                num_enemy = random.randint(4, 8)
                for i in range(num_enemy):
                    doshman = random.choice(self.enemy_list)
                    doshman(self, x, y)
                    doshman.draw()


    def on_draw(self):
        arcade.start_render()
        self.tir.draw()
        arcade.draw_rectangle_outline(self.width // 2,
                                      self.height // 2, self.width - 20,
                                      self.height - 20, arcade.color.DARK_GREEN, border_width=10)
        arcade.finish_render()



            

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if x > self.tir.width // 2 and x < self.width - self.tir.width // 2:
            self.tir.center_x = x


game = Game()
arcade.run()
