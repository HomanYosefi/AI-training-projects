import arcade


class Ball(arcade.Sprite):
    ...


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
        self.height = 60
        self.speed = 4
        self.score = 0

    def move(self):
        ...    


class Game(arcade.Window):
    def __init__(self, width = 800, height = 300, title = 'Ping Pong 🏓🏓🏓'):
        super().__init__()
        arcade.set_background_color(arcade.color.GREEN_YELLOW)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width // 2,
                                      self.height // 2, self.width - 20,
                                     self.height - 20, arcade.color.DARK_GREEN, border_width= 10)
        arcade.draw_line(self.width // 2, 30,
                         self.width // 2 , self.height - 30, color= arcade.color.BLACK,
                            line_width= 10)                             
        arcade.finish_render()      

game = Game()
arcade.run()            