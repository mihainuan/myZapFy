import time # for Time
import os # for Windows
import openai # for ChatGPT
import requests # for API HTTP Requests

# For Browser (Chrome)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Keyboard

from time import sleep # for delay
from itertools import cycle # for infinite cycling through a list

import PySimpleGUI as sg # for UI

### API EditaCodigo ###
agent = { "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko GomezAgent 3.0) Chrome/56.0.2924.87 Safari/537.36' }
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/vELPO4F50i7QPz4OcUXPs2q42EWfiwts", headers = agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
token1 = api[0].strip()
token2 = api[1].strip()
token3 = api[2].strip()
ball_notification = api[3].strip()
contact_client = api[4].strip()
msg_box = api[5].strip()
msg_client = api[6].strip()
##--##

# First screen (password login)
screen1 = [
    [sg.Text('YOUR PASSWORD')],
    [sg.Input(key='password', password_char='*')],
    [sg.Button('Login')]
]

# Main screen (MyZapFy)
screen2 = [
    [sg.Text('Welcome to MyZapFy!')],
]

window1 = sg.Window('MyZapFy', layout = screen1)
window2 = sg.Window('MyZapFy', layout = screen2)

while True:
    event, values = window1.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Login':
        senha = values['password']
        if senha == token3:
            window1.close()
            event, values = window2.read()