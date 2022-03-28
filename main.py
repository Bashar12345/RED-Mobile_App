from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window

Window.size = (300, 500)

class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


MainApp().run()