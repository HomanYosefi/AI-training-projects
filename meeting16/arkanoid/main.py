import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__("ball.png")
        self.width = 30
        self.height = 30
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.key_pass = 0
        self.speed = 8

    def move(self, game):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed








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
        

class Enderman(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__("enderman.jpg")
        self.width = (game.width - 100) // 8
        self.height = (game.width - 100) // 8
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0



class Bow(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__("enderman.jpg")
        self.width = (game.width - 100) // 8
        self.height = (game.width - 100) // 8
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0



class Octaopus(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__("octaopus.jpg")
        self.width = (game.width - 100) // 8
        self.height = (game.width - 100) // 8
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0


class Tnt(arcade.Sprite):
    def __init__(self, game, x, y):
        super().__init__("tnt.jpg")
        self.width = (game.width - 100) // 8
        self.height = (game.width - 100) // 8
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0


class Game(arcade.Window):
    def __init__(self, width = 400, height = 800, title= 'arkanoid'):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.draw_enemy = 0
        self.w_enemy = (self.width - 100) // 8
        self.h_enemy = [self.height - 100, self.height - 100 - self.w_enemy,
                         self.height - 100 - (self.w_enemy * 2)]
        self.tir = Rocket(self)
        self.toop = Ball(self, self.tir.center_x, self.tir.center_y)
        self.bow = Bow(self, 50 + self.w_enemy // 2, self.h_enemy[0])
        self.enderman = Enderman(
            self, 50 + self.w_enemy // 2 + (self.w_enemy), self.h_enemy[0])
        self.octaopus = Octaopus(
            self, 50 + self.w_enemy // 2 + (self.w_enemy * 2), self.h_enemy[0])
        self.tnt = Tnt(self, 50 + self.w_enemy // 2 +
                       (self.w_enemy * 3), self.h_enemy[0])
        self.enemy_list = [self.bow, self.enderman, self.octaopus, self.tnt]
        self.enemy_show = []
        self.debog = 0
        self.score = 0

    def on_update(self, delta_time: float):
        if arcade.check_for_collision(self.tir, self.toop):
            self.toop.change_y *= -1

        if self.toop.key_pass == 0 :
            self.debog = 1
            self.toop.center_x = self.tir.center_x
            self.toop.center_y = self.tir.center_y + 20
        else: 
            if self.debog == 1:
                self.debog = 0
                self.toop.change_y = 1
            self.toop.move(self)


        if self.toop.center_y > self.height:
            self.toop.change_y *= -1
            self.toop.change_x = random.choice([1, -1])

        if self.toop.center_x > self.width or self.toop.center_x < 0:
            self.toop.change_x *= -1

        if self.toop.center_y < 0:
            del self.toop
            self.toop = Ball(self, self.tir.center_x, self.tir.center_y)
            self.score -= 1



        item = 0
        while item < len(self.enemy_list):
            if arcade.check_for_collision(self.toop, self.enemy_list[item]):
                del self.enemy_list[item]
            else:
                item += 1

        if len(self.enemy_list) == 0: 
            self.draw_enemy = 1


        if self.draw_enemy == 1:
            self.draw_enemy = 0
            # self.enemy_list = [
            #     self.bow, self.enderman, self.octaopus, self.tnt]
            # for y in self.h_enemy:
            #     x = 50 + self.w_enemy // 2
            #     num_enemy = random.randint(4, 8)
            #     for i in range(num_enemy):
            #         doshman = random.choice(self.enemy_list)
            #         doshman(self, x, y)
            #         x += self.w_enemy
            #         doshman.draw()
            for i in range(self.w_enemy,  50 + self.w_enemy // 2 +
                           (self.w_enemy * 7), self.w_enemy):
                           for i in self.h_enemy:
                                    self.bow = Bow(self, 50 + self.w_enemy // 2, self.h_enemy[0])
                                    self.enderman = Enderman(
                                    self, 50 + self.w_enemy // 2 + (self.w_enemy), self.h_enemy[0])
                                    self.octaopus = Octaopus(
                                    self, 50 + self.w_enemy // 2 + (self.w_enemy * 2), self.h_enemy[0])
                                    self.tnt = Tnt(self, 50 + self.w_enemy // 2 +
                                            (self.w_enemy * 3), self.h_enemy[0])



    def on_draw(self):
        arcade.start_render()
        self.toop.draw()
        self.tir.draw()
        for i in self.enemy_list:
            i.draw()
        arcade.draw_rectangle_outline(self.width // 2,
                                      self.height // 2, self.width - 20,
                                      self.height - 20, arcade.color.DARK_GREEN, border_width=10)
        arcade.finish_render()



            

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if x > self.tir.width // 2 and x < self.width - self.tir.width // 2:
            self.tir.center_x = x

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.toop.key_pass = 1

        

game = Game()
arcade.run()
