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

screen1 = [
    [sg.Text('YOUR PASSWORD')],
    [sg.Input(key='password', password_char='*')],
    [sg.Button('Login')]
]


window1 = sg.Window('ZapBOT', layout = screen1)

while True:
    event, values = window1.read()