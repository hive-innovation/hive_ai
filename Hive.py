import os
import sys
import kivy
from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, OptionProperty, StringProperty
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.scrollview import ScrollView
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.list import OneLineAvatarIconListItem

from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.uix.widget import Widget
root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

import json  # NOQA: E402
import traceback  # NOQA: E402

from kivy.factory import Factory  # NOQA: E402

Window.size=(310,580)
__version__ = "1.0"
class Hive(MDApp):
    def build(self):
        screen_manager=ScreenManager()
        screen_manager.add_widget(Builder.load_file("kivy/front_end/main.kv"))
        screen_manager.add_widget(Builder.load_file("kivy/front_end/login.kv"))
        screen_manager.add_widget(Builder.load_file("kivy/front_end/signup.kv"))
        self.url  = "https://loginsetup-14858.firebaseio.com/.json"
        
        return screen_manager
        auth = '0QjlZHsBsviGEbNRPNPdMZwq5UDBI1B0qdg9Ogvd'
    
    

    def login(self):
        loginEmail = self.load_file("kivy/front_end/login.kv").ids.login_email.text
        loginPassword = self.load_file("kivy/front_end/login.kv").ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        emails= set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check=True
            self.strng.get_screen('main').manager.current = 'main'
        else:
            print("user no longer exists")


if __name__ == "__main__":
    
    Hive().run()