import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
    def on_touch_move(self, touch):
        print("on touch move")
    def on_touch_up(self, touch):
        print("RELEASE", touch)

class Board(Widget):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        with self.canvas:
            width = [0,70,140,210,280,350,420,490]
            height = [0,70,140,210,280,350,420,490]
            num = 0
            for y in height:
                for x in width:
                    if (num%2 == 0):
                        Color(0,0,.5,mode='hsv')
                        Rectangle(pos=(x,y), size=(70,70))
                    else:
                        Color(0,0,1,mode='rgb')
                        Rectangle(pos=(x,y), size=(70,70))
                    num += 1
                num -= 1

class Pieces(Board):
    def __init__(self, **kwargs):
        super(Pieces, self).__init__(**kwargs)
        with self.canvas:
            width = [0,70,140,210,280,350,420,490]

            L_white_rook = Image(source="Images/white_rook.png", pos=(0, 490), size=(70,70))
            L_white_knight = Image(source="Images/white_knight.png", pos=(70, 490), size=(70,70))
            L_white_bishop = Image(source="Images/white_bishop.png", pos=(140, 490), size=(70,70))
            white_king = Image(source="Images/white_king.png", pos=(210, 490), size=(70,70))
            white_queen = Image(source="Images/white_queen.png", pos=(280, 490), size=(70,70))
            R_white_bishop = Image(source="Images/white_bishop.png", pos=(350, 490), size=(70,70))
            R_white_knight = Image(source="Images/white_knight.png", pos=(420, 490), size=(70,70))
            R_white_rook = Image(source="Images/white_rook.png", pos=(490, 490), size=(70,70))
            d={}
            for x in width:
                d["white_pawn" + str(x)] = Image(source="Images/white_pawn.png", pos=(x, 420), size=(70,70))

            L_black_rook = Image(source="Images/black_rook.png", pos=(0, 0), size=(70,70))
            L_black_knight = Image(source="Images/black_knight.png", pos=(70, 0), size=(70,70))
            L_black_bishop = Image(source="Images/black_bishop.png", pos=(140, 0), size=(70,70))
            black_king = Image(source="Images/black_king.png", pos=(210, 0), size=(70,70))
            black_queen = Image(source="Images/black_queen.png", pos=(280, 0), size=(70,70))
            R_black_bishop = Image(source="Images/black_bishop.png", pos=(350, 0), size=(70,70))
            R_black_knight = Image(source="Images/black_knight.png", pos=(420, 0), size=(70,70))
            R_black_rook = Image(source="Images/black_rook.png", pos=(490, 0), size=(70,70))
            e={}
            for x in width:
                e["black_pawn" + str(x)] = Image(source="Images/black_pawn.png", pos=(x, 70), size=(70,70))

class MyApp(App):
    def build(self):
        Window.size = (560, 560)
        return Pieces()

if __name__ == '__main__':
    MyApp().run()
