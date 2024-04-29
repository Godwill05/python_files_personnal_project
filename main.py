import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10

        self.lbl_name = Label(text="Nom:")
        self.add_widget(self.lbl_name)

        self.txt_name = TextInput()
        self.add_widget(self.txt_name)

        self.lbl_lastname = Label(text="Prénom:")
        self.add_widget(self.lbl_lastname)

        self.txt_lastname = TextInput()
        self.add_widget(self.txt_lastname)

        self.btn_login = Button(text="Login", on_press=self.login)
        self.add_widget(self.btn_login)

    def login(self, instance):
        name = self.txt_name.text
        lastname = self.txt_lastname.text
        self.clear_widgets()
        self.add_widget(Label(text="Bienvenue, {} {}!".format(name, lastname)))


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
