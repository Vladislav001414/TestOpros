from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window




#Window.size = (720,1280)
Window.size =(480, 852)
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


class Container(FloatLayout):
     pass


class MyTest(App):
    def build(self):
        
         return Container()


if __name__ == '__main__':
    MyTest().run()