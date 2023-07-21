import random
import time
import arcade




class Pear(arcade.Sprite):
    def __init__(self, game):
        super().__init__("golaby.jpg")
        self.width = 30
        self.height = 30
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(0, game.width)
        self.center_y = random.randint(0, game.height)
        self.show = 0


class Shet(arcade.Sprite):
    def __init__(self, game):
        super().__init__("shet.png")
        self.width = 30
        self.height = 30
        self.change_x = 0
        self.change_y = 0
        self.center_x = random.randint(0, game.width)
        self.center_y = random.randint(0, game.height)
        self.show = 0

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("free-apple.png")
        self.width = 30
        self.height = 30
        self.change_x = 0
        self.change_y = 0
        self.list_sib_w = []
        for i in range (0, game.width, 15):
            self.list_sib_w.append(i)

        self.list_sib_h = []
        for i in range (0, game.height, 15):
            self.list_sib_h.append(i)

        self.center_x = random.choice(self.list_sib_w)
        self.center_y = random.choice(self.list_sib_h)

class Finish(arcade.Sprite):
    def __init__(self, game):
        super().__init__("game_over.png")
        self.width = game.width
        self.height = game.height
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.show = 0




class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 15
        self.height = 15
        self.list_snake_w = []
        for i in range(0, game.width, 15):
            self.list_snake_w.append(i)

        self.list_snake_h = []
        for i in range(0, game.height, 15):
            self.list_snake_h.append(i)
        self.center_x = self.list_snake_w[len(self.list_snake_w) // 2]
        self.center_y = self.list_snake_h[len(self.list_snake_h) // 2]
        self.color_face = arcade.color.GREEN 
        self.color_body_1 = arcade.color.BABY_BLUE
        self.color_body_2 = arcade.color.APPLE_GREEN
        self.color_b = 0
        self.change_x = 0
        self.change_y = 0
        self.speed = 15
        self.score = 1
        self.body = []

    def test_body(self, x, y):
        for part in self.body:
            if part["x"] == x and part["y"] == y:
                return 0
        return 1
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color_face)
        for part in self.body:
            if self.color_b % 2 == 0:
                arcade.draw_rectangle_filled(part["x"], part["y"], self.width, self.height, self.color_body_1)

            else:
                arcade.draw_rectangle_filled(
                    part["x"], part["y"], self.width, self.height, self.color_body_2)

            self.color_b += 1        

    def move(self):
        self.body.append(
            {"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)    
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
            

    def eat(self, mive):
        if mive == 1:
            self.score += 1
        elif mive == 0:
            self.score += 2    
        #else: 
            #self.score -= 1      

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500, height= 500, title = "snake 🐍 v : 1.0.0")
        arcade.set_background_color(arcade.color.LIGHT_KHAKI)
        self.sib = Apple(self)
        self.golaby = Pear(self)
        self.goh = Shet(self)
        self.snake = Snake(self)
        self.finish = Finish(self)

    def on_draw(self):
        arcade.start_render()
        self.sib.draw()
        if self.golaby.show == 1:
            self.golaby.draw()
        if self.goh.show == 1:
            self.goh.draw()
        if self.finish.show == 1:
            self.finish.draw()
        self.snake.draw()
        arcade.finish_render()   

    def on_update(self, delta_time: float):
        if self.snake.center_x < self.sib.center_x and self.snake.test_body(self.snake.center_x + self.snake.speed, self.snake.center_y):
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()

        elif self.snake.center_y < self.sib.center_y and self.snake.test_body(self.snake.center_x, self.snake.center_y + self.snake.speed):
            self.snake.change_x = 0
            self.snake.change_y = 1
            self.snake.move()

        elif self.snake.center_x > self.sib.center_x and self.snake.test_body(self.snake.center_x - self.snake.speed, self.snake.center_y):
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()


        elif self.snake.center_y > self.sib.center_y and self.snake.test_body(self.snake.center_x, self.snake.center_y - self.snake.speed):
            self.snake.change_x = 0
            self.snake.change_y = -1
            self.snake.move()

        if arcade.check_for_collision(self.snake, self.sib):
            self.fruit_counter = "apple"
            self.snake.eat(self)
            self.sib = Apple(self)

        self.snake.move()
        #if self.snake.center_x < 0 or self.snake.center_x > self.width or self.snake.center_y < 0 or self.snake.center_y > self.height:
        #    self.finish.show = 1

        if self.snake.score == -1:
            ...
            #self.finish.show = 1
        elif arcade.check_for_collision(self.snake, self.golaby):
            self.snake.eat(0)
            self.golaby.show = 0
            del self.golaby
            self.golaby = Pear(self)
            print("score : ", self.snake.score)

        elif arcade.check_for_collision(self.snake, self.goh):
            self.snake.eat(2)
            self.goh.show = 0
            del self.goh
            self.goh = Shet(self)
            print("score : ", self.snake.score)

        if arcade.check_for_collision(self.snake, self.sib):
            self.snake.eat(1)
            print("score : ", self.snake.score)
            del self.sib
            self.sib = Apple(self)
            if random.randint(0, 5) == 1:
                self.goh.show = 1
            else: 
                self.goh.show = 0

            if random.randint(0, 10) == 1:
                self.golaby.show = 1
            else:
                self.golaby.show = 0
        
        time.sleep(0.13)        
            




if __name__ == "__main__":
    game = Game()
    arcade.run()