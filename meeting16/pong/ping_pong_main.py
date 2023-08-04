import random
import arcade
import time 



class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__("ball.png")
        self.width = 35
        self.height = 35
        #self.change_angle = 0
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 8

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed



class Rocket(arcade.Sprite):
    def __init__(self, x, y, c, name):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = name
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 100
        self.speed = 4
        self.score = 0


    def move(self,game, ball):
        if ball.center_x > game.width // 2 :
            if self.center_y >= ball.center_y:
                self.change_y = -1 

            if self.center_y < ball.center_y:
                self.change_y = 1

            self.center_y += self.change_y * self.speed     

            if self.center_y < 30 : 
                self.center_y = 30 

            elif self.center_y > game.height - 30 :
                self.center_y = game.height - 30


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, 
                                        self.height, self.color)


class Game(arcade.Window):
    def __init__(self, width = 800, height = 300, title = 'Ping Pong 🏓🏓🏓'):
        super().__init__()
        arcade.set_background_color(arcade.color.GREEN_YELLOW)
        self.player_1 = Rocket(40, self.height // 2, arcade.color.DARK_RED, "homan")
        self.player_2 = Rocket(self.width - 40, self.height // 2, arcade.color.DARK_POWDER_BLUE, "sadegh")
        self.toop = Ball(self)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"score player 1 : {self.player_1.score}", self.width // 2 - 100, self.height -
                         50, arcade.color.BLACK_BEAN, font_size=15, anchor_x="center")
        arcade.draw_text(f"score PC : {self.player_2.score}", self.width // 2 + 100, self.height -
                         50, arcade.color.BLACK_BEAN, font_size=15, anchor_x="center")
        arcade.draw_rectangle_outline(self.width // 2,
                                      self.height // 2, self.width - 20,
                                     self.height - 20, arcade.color.DARK_GREEN, border_width= 10)
        arcade.draw_line(self.width // 2, 30,
                         self.width // 2 , self.height - 30, color= arcade.color.BLACK,
                            line_width= 10)    
        self.player_1.draw()
        self.player_2.draw()         
        self.toop.draw()
        arcade.finish_render()    

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if y > self.player_1.height // 2 and y < self.height - self.player_1.height // 2:
            self.player_1.center_y = y

    def on_update(self, delta_time: float):
        self.toop.move()
        self.player_2.move(self, self.toop)
        if 5 < self.player_1.score < 10:
            self.toop.speed = 6
        elif 10 <= self.player_1.score < 15:
            self.toop.speed = 5


        if self.toop.center_y < self.toop.height or self.toop.center_y > self.height - self.toop.height:
            self.toop.change_y *= -1
        if self.toop.center_x < self.toop.width:
            self.player_2.score += 1
            print("score player 2 : ", self.player_2.score)
            time.sleep(1)
            del self.toop
            self.toop = Ball(self)


        elif self.toop.center_x > self.width - self.toop.width: 
            self.player_1.score += 1
            print("score player 1 : ", self.player_1.score)
            time.sleep(1)
            del self.toop
            self.toop = Ball(self)

        if arcade.check_for_collision(self.player_1, self.toop) or arcade.check_for_collision(self.player_2, self.toop):
            self.toop.change_x *= -1


            
                


game = Game()
arcade.run()            