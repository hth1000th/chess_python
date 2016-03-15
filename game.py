import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    MyApp().run()
