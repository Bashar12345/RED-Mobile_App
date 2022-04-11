screens="""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import HomeScreen libs.uix.baseclass.home_screen.HomeScreen
#:import IndexScreen libs.uix.baseclass.index_screen.IndexScreen

ScreenManager:
    IndexScreen:
        name: "index"

    HomeScreen:
        name: "home"



<IndexScreen>:
    MDBoxLayout:
        MDLabel:
            text:"dsfknslkhfkjbsda"
            size_hint: None, None

<HomeScreen>:
    MDBoxLayout:
        MDLabel:
            text: "ajdhajkdjadjhjk"
            size_hint: None, None

"""