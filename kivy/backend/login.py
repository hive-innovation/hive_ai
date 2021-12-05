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

utils.load_kv("login.kv")

class login():
        def build(self):
    self.strng = Builder.load_string(help_str)
    self.url  = "https://loginsetup-14858.firebaseio.com/.json"
    return self.strng
    auth = '0QjlZHsBsviGEbNRPNPdMZwq5UDBI1B0qdg9Ogvd'
    def login(self):
        loginEmail = self.strng.get_screen('login').ids.login_email.text
        loginPassword = self.strng.get_screen('login').ids.login_password.text

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
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")
