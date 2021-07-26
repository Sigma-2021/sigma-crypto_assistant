#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """


""" IMPORTS FILES """
import persistence
import entities 
import percent


btc = entities.Coin("BTC")
btc.refresh_coin(btc.name)
doge = entities.Coin("DOGE")
doge.refresh_coin(doge.name)
eth = entities.Coin("ETH")
eth.refresh_coin(eth.name)