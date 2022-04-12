import os
import sys
import platform
from pathlib import Path
from kivy.lang import Builder
from kivymd.app import MDApp
from app_root_screen_manager import PAGES



#from kivy.factory import Factory  # NOQA: E402
#from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.screenmanager import Screen,ScreenManager


# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

#Window.size = (300, 500)

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["RED_Mobile_App_ROOT"] = sys._MEIPASS
else:
    os.environ["RED_Mobile_App_ROOT"] = str(Path(__file__).parent)

#__version__ = "1.0"


KV_DIR = f"{os.environ['RED_Mobile_App_ROOT']}/libs/kv"
print(KV_DIR)

for kv_file in os.listdir(KV_DIR):
    print(kv_file)
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())


class RED_Mobile_App(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(RED_Mobile_App, self).__init__(**kwargs)
        self.title = "RED"
        self.icon = f"{os.environ['RED_Mobile_App_ROOT']}/assets/images/05.jpg"

        Window.soft_input_mode = "below_target"
        self.title = "ReD_App"

        #self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Dark"

    def build(self):
        #view_css = Builder.load_string(KV)
        #Uix = Builder.load_file(pages)
        Uix = Builder.load_string(PAGES)
        return Uix


RED_Mobile_App().run()


    # def on_start(self):
    #     styles = {
    #         "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
    #     }
    #     for style in styles.keys():
    #         self.Root.home_screen.ids.home_layout.add_widget(
    #             DataCard(
    #                 line_color=(0.2, 0.2, 0.2, 0.8),
    #                 style=style,
    #                 text=style.capitalize(),
    #                 md_bg_color=get_color_from_hex(styles[style]),
    #             )
    #         )



