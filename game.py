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
            pass

class Pieces(Board):
    def __init__(self, **kwargs):
        super(Pieces, self).__init__(**kwargs)
        with self.canvas:
            pass

class MyApp(App):
    def build(self):
        Window.size = (560, 560)
        return Pieces()

if __name__ == '__main__':
    MyApp().run()
