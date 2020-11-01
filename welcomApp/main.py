from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (340, 600)

class LoginWindow(Screen):
    userName = ObjectProperty(None)
    lastName = ObjectProperty(None)
    hidden = ObjectProperty(None)
    def SubmitBtn(self):
        if (self.userName != '') & (self.lastName.text != ''):
            MainWindow.a = self.userName.text
            MainWindow.b = self.lastName.text
            wm.current = 'main'
            self.reset()
        else:
            self.hidden.text = 'no input'

    def reset(self):
        self.userName.text = ""
        self.lastName.text = ""
        self.hidden.text = ""


class MainWindow(Screen):
    fName = ObjectProperty(None)
    lName = ObjectProperty(None)
    a = ''
    b = ''

    def on_enter(self, *args):
        self.fName.text = self.a
        self.lName.text = self.b


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('welcom.kv')

wm = WindowManager()

screens = [LoginWindow(name = 'login'), MainWindow(name = 'main')]
for screen in screens:
    wm.add_widget(screen)

wm.current = 'login'

class welcomApp(App):
    def build(self):
        return wm

if __name__ == '__main__':
    welcomApp().run()