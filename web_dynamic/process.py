#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """


""" IMPORTS EXTERN MODULES """
import time
from datetime import datetime
import os

""" IMPORTS FILES """
import persistence
import entities 
import mail
import info
import percent

""" In case url 1 is not working, changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i = 2
a = b = 0
cortarpicos = cortarconstantes = 0

while(i >= 0):
    btc_price = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc_price)
    eth_price = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth_price)
    doge_price = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge_price)
    a = percent.detectar_picos(a)
    if a != 0:
        cortarpicos = i + 180
    b = percent.chequear_movimientos(b)
    if b != 0:
        cortarconstantes = i + 180

    """ Save trends every hour """
    if i % 60 == 0:
        percent.insert_in_tendencias()
    """ Every 3 hours clear history of constants and peaks """
    if i == cortarpicos:
        a = 0
    if i == cortarconstantes:
        b = 0
    """Send daily summary """
    if i % 1440 == 0:
        mail.daily_resume()

    i += 1
    time.sleep(60)