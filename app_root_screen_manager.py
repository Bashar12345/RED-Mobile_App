from kivy.uix.screenmanager import ScreenManager
from libs.baseclass.index_screen import IndexScreen

from libs.baseclass.home_screen import HomeScreen

from libs.baseclass.history import HistoryScreen

from libs.baseclass.quran_fact import Quran_factScreen

from libs.baseclass.haddits import HadditsScreen

from libs.baseclass.science import ScienceScreen

from libs.baseclass.desh import DeshScreen





#from kivy.factory import Factory 
# libs.baseclass.register_screen.ShrineRegisterScreen

PAGES = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import IndexScreen libs.baseclass.index_screen.IndexScreen
#:import HomeScreen libs.baseclass.home_screen.HomeScreen
#:import HistoryScreen libs.baseclass.history.HistoryScreen
#:import Quran_factScreen libs.baseclass.quran_fact.Quran_factScreen
#:import HadditsScreen libs.baseclass.haddits.HadditsScreen
#:import ScienceScreen libs.baseclass.science.ScienceScreen
#:import DeshScreen libs.baseclass.desh.DeshScreen

Page_manager:
    transition: FadeTransition()
    IndexScreen:
        name: "index"

    HomeScreen:
        name: "home"
    
    HistoryScreen:
        name: 'history'
    
    Quran_factScreen:
        name: 'quran_fact'
    
    HadditsScreen:
        name: 'haddits'
    
    ScienceScreen:
        name: 'science'
    
    DeshScreen:
        name: 'desh'

"""

class Page_manager(ScreenManager):
    """The Root (or Assembler) of the App."""
    pass

pages_manage = Page_manager()
pages_manage.add_widget(IndexScreen(name ="index"))
pages_manage.add_widget(HomeScreen(name="home"))
pages_manage.add_widget(HistoryScreen(name="history"))
pages_manage.add_widget(Quran_factScreen(name="quran_fact"))
pages_manage.add_widget(HadditsScreen(name="haddits"))
pages_manage.add_widget(ScienceScreen(name="science"))
pages_manage.add_widget(DeshScreen(name="desh"))

#pages_manage.current('')





