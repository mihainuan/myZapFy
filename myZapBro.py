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


dir_path = os.getcwd()
opt = Options()
opt.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(options=opt)
driver.get("https://web.whatsapp.com/")

###API EditaCodigo
agent = { "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko GomezAgent 3.0) Chrome/56.0.2924.87 Safari/537.36' }
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/vELPO4F50i7QPz4OcUXPs2q42EWfiwts", headers = agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
ball_notification = api[3].strip()
contact_client = api[4].strip()
msg_box = api[5].strip()
msg_client = api[6].strip()
#####

client_q = 'pergunta ao cliente:'
client_a = 'Por favor, responda a mensagem do cliente com base no próximo texto'
client_copy = 'Os clientes que comprarem nesse mês de junho só paga a primeira Mensal Em agosto, aproveitem a promoção, agende uma visita 719 8451 5414'
question = client_q + client_a + client_copy

print(opt.arguments)
time.sleep(10)

def zapBot():
    try:
        # 1) Getting Notifications and Double-Clicking in notified contact
        green_icon_unread = driver.find_element(By.CLASS_NAME, ball_notification)
        green_icon_unread = driver.find_elements(By.CLASS_NAME, ball_notification)
        
        # 1.1) Points into the last notification
        last_icon_unread = green_icon_unread[-1]
        action_unread = webdriver.common.action_chains.ActionChains(driver)
        action_unread.move_to_element_with_offset(last_icon_unread, 0, -20)
        
        # 1.2) Double-click it
        action_unread.click()
        action_unread.perform()
        action_unread.click()
        action_unread.perform()

        # 2) Messages Received
        all_msgs = driver.find_elements(By.CLASS_NAME, msg_client)
        all_msgs_txt = [e.text for e in all_msgs]
        last_msg = all_msgs_txt[-1] # Gets Last message
        
        # 3) Process Messages with API (ChatGPT)
        openai.api_key = "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"
        response = openai.Completion.create(
        model="text-davinci-003",
        # prompt=question,
        prompt=last_msg,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        answer = response['choices'][0]['text']
        print(answer)
        time.sleep(3)

        # 4) Replies Message to WhatsApp
        text_field = driver.find_element(By.XPATH, msg_box)
        text_field.click()
        time.sleep(3)
        text_field.send_keys(answer, Keys.ENTER)

        # 5) Close the conversation with the contact
        time.sleep(2)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        print("New notification:\n")
        print(last_msg)
        sleep(3) # three seconds

    except:
        print("Waiting for notifications...")
        # loading()
while True:
    zapBot()