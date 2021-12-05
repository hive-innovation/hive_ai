from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen 
from kivymd.app import MDApp 
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import utils

utils.load_kv("tab_one.kv")

class Signup():
    
    def build(self): 
        screen = MDScreen() 
        speed_dial = MDFloatingActionButtonSpeedDial() 
        speed_dial.data = self.data 
        speed_dial.root_button_anim = True 
        screen.add_widget(speed_dial) 
        return screen
