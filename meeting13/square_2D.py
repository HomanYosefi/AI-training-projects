import arcade

tool = 6
arz = 6


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Square's")        
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.size_circle = 25

    def on_draw(self):
        arcade.start_render()
        for i in range(arz):
            for j in range(tool):
                fasele_tool = (tool / 2) - j 
                fasele_arz = (arz / 2) - i
                if j % 2 == 0: 
                    if i % 2 == 0:
                        arcade.draw_circle_filled(
                            (self.width/2) - (fasele_tool * self.size_circle), (self.height/2) - (fasele_arz * self.size_circle), 10, (255, 0, 0))
                    else: 
                        arcade.draw_circle_filled(
                            (self.width/2) - (fasele_tool * self.size_circle), (self.height/2) - (fasele_arz * self.size_circle), 10, (0, 255, 0))
                else: 
                    if i % 2 != 0:
                        arcade.draw_circle_filled(
                            (self.width/2) - (fasele_tool * self.size_circle), (self.height/2) - (fasele_arz * self.size_circle), 10, (255, 0, 0))
                    else:
                        arcade.draw_circle_filled(
                            (self.width/2) - (fasele_tool * self.size_circle), (self.height/2) - (fasele_arz * self.size_circle), 10, (0, 255, 0))

        # arcade.draw_circle_filled(self.width/2, self.height/2, 10, (255, 0, 0))

window = Game()
arcade.run()