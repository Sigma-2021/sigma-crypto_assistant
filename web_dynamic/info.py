#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests
import time
from datetime import datetime

def consultar_precio_BTC(url):
    """ Requests BTC price from Binance API """

    query = "api/v3/ticker/price?symbol=BTCUSDT"
    r = requests.get(url + query)
    r = r.json()
    return int(float(r["price"]))

def consultar_precio_DOGE(url):
    """ Requests DOGE price from Binance API """

    query = "api/v3/ticker/price?symbol=DOGEUSDT"
    r = requests.get(url + query)
    r = r.json()
    return float(r["price"])

def consultar_precio_ETH(url):
    """ Requests ETH price from Binance API """

    query = "api/v3/ticker/price?symbol=ETHUSDT"
    r = requests.get(url + query)
    r = r.json()
    return int(float(r["price"]))
