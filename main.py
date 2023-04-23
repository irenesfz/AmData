from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import telebot

from config import TELEGRAM_TOKEN


bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])

def enviar(message):
    bot.reply_to(message, "Hola wenasss")

@bot.message_handler(commands=["avisar"])

def enviar(message):
    bot.reply_to(message, "avisar")


bot.polling()

    # add your user agent 
    # HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})

    # # The webpage URL
    # URL = "https://www.amazon.es/Turtle-Beach-Stealth-600-Gen/dp/B08D46V1TK/?_encoding=UTF8&pd_rd_w=F0iaW&content-id=amzn1.sym.330da5a0-7bde-4e91-b5d4-068d6e2dd007&pf_rd_p=330da5a0-7bde-4e91-b5d4-068d6e2dd007&pf_rd_r=VTJR1DA705C04KYCXQG5&pd_rd_wg=4NpwL&pd_rd_r=70c64cf7-1e23-49fd-ac77-dbe8a401b206&ref_=pd_gw_gcx_gw_dyn_m_md23"

    # # HTTP Request
    # webpage = requests.get(URL, headers=HEADERS)

    # # Soup Object containing all data
    # soup = BeautifulSoup(webpage.content, "html.parser")

    # price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip().replace("€","").replace(",",".")

    # print(price)