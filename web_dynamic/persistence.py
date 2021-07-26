#!/usr/bin/python3
""" Made by Facundo Diaz, Tomas De Castro and Tadeo Grach to Holberton School 2021 """

import MySQLdb
import time
from datetime import datetime

MY_H = "localhost"
MY_U = "root"
MY_P = "betty"
MY_D = "sigma"






""" BTC FUNCTIONS """

def save_price_bitcoin(price):
    """ This function checks how many prices are saved.
        If there are less than 1440 (previous 24 hours) it inserts a new one.
        If there are more than 1440 it deletes the last one and then it inserts.
        This is the way to always keep the prices of the last 24 hours saved"""

    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT count(*) FROM history_coin WHERE name='BTC';")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 1440:
        insertar_btc(str(price))
    else:
        borrar_ultimo_btc(str(price))

def insertar_btc(price):
    """ This function adds a new price """

    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_coin (name, price) VALUES ('BTC', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_btc(price):
    """ This function finds the id of the last price and then calls the delete function
        and passes it as an argument the id to be deleted """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT id FROM history_coin WHERE name='BTC' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item_btc(id, str(price))

def borrar_item_btc(id, price):
    """ This function deletes a price per id """

    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_coin WHERE id ="+ id)
    nuevaxd.commit()
    insertar_btc(str(price))

def traer_ultimo_precio_btc():
    """ This function returns the most current price saved """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY id DESC LIMIT 1;")
    resultado = consulta.fetchall()
    price = 1
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_ultimos_precios_btc():
    """ This function returns a list with the prices of the last hour (60 prices) """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY id DESC LIMIT 60;")
    resultado = consulta.fetchall()
    arr_precios = []
    for i in resultado:
        for i2 in i:
            i2 = int(i2)
            arr_precios.append(i2)
    return arr_precios

def traer_masviejo_precio_btc():
    """ This function returns the oldest price in the table that corresponds to the one 24 hours ago """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    price = 1
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_mayor_24_btc():
    """ This function returns the highest price of the last 24 hours """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY price DESC LIMIT 1;")
    resultado = consulta.fetchall()
    res = 1
    for i in resultado:
        for i2 in i:
            res = i2
    return res

def traer_menor_24_btc():
    """ This function returns the smallest price of the last 24 hours """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY price ASC LIMIT 1;")
    resultado = consulta.fetchall()
    res = 1
    for i in resultado:
        for i2 in i:
            res = i2
    return res







""" DOGE FUNCTIONS """

def save_price_doge(price):
    """ This function checks how many prices are saved.
    If there are less than 1440 (previous 24 hours) it inserts a new one.
    If there are more than 1440 it deletes the last one and then it inserts.
    This is the way to always keep the prices of the last 24 hours saved"""

    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT COUNT(*) FROM history_coin WHERE name='DOGE';")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 1440:
        insertar_doge(str(price))
    else:
        borrar_ultimo_doge(str(price))

def insertar_doge(price):
    """ This function adds a new price """

    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_coin (name, price) VALUES ('DOGE', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_doge(price):
    """ This function finds the id of the last price and then calls the delete function
        and passes it as an argument the id to be deleted """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT id FROM history_coin WHERE name='DOGE' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item_doge(id, str(price))

def borrar_item_doge(id, price):
    """ This function deletes a price per id """

    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_coin WHERE id ="+ id)
    nuevaxd.commit()
    insertar_doge(str(price))

def traer_ultimo_precio_doge():
    """ This function returns the most current price saved """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY id DESC LIMIT 1;")
    resultado = consulta.fetchall()
    price = 1
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_ultimos_precios_doge():
    """ This function returns a list with the prices of the last hour (60 prices) """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY id DESC LIMIT 60;")
    resultado = consulta.fetchall()
    arr_precios = []
    for i in resultado:
        for i2 in i:
            i2 = float(i2)
            arr_precios.append(i2)
    return arr_precios
            
def traer_masviejo_precio_doge():
    """ This function returns the oldest price in the table that corresponds to the one 24 hours ago """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    price = 1
    for i in resultado:
        for i2 in i:
            price = float(i2)
    return price

def traer_mayor_24_doge():
    """ This function returns the highest price of the last 24 hours """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY price DESC LIMIT 1;")
    resultado = consulta.fetchall()
    res = 1
    for i in resultado:
        for i2 in i:
            res = float(i2)
    return res

def traer_menor_24_doge():
    """ This function returns the smallest price of the last 24 hours """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY price ASC LIMIT 1;")
    resultado = consulta.fetchall()
    res = 1
    for i in resultado:
        for i2 in i:
            res = float(i2)
    return res







""" ETH FUNCTIONS """

def save_price_ethereum(price):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT COUNT(*) FROM history_coin WHERE name='ETH';")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 1440:
        insertar_eth(str(price))
    else:
        borrar_ultimo_eth(str(price))

def insertar_eth(price):
    """ This function adds a new price """

    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_coin (name, price) VALUES ('ETH', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_eth(price):
    """ This function finds the id of the last price and then calls the delete function
        and passes it as an argument the id to be deleted """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT id FROM history_coin WHERE name='ETH' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item_eth(id, str(price))

def borrar_item_eth(id, price):
    """ This function deletes a price per id """

    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_coin WHERE id ="+ id)
    nuevaxd.commit()
    insertar_eth(str(price))

def traer_ultimo_precio_eth():
    """ This function returns the most current price saved """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY id DESC LIMIT 1;")
    resultado = consulta.fetchall()
    price = 1
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_ultimos_precios_eth():
    """ This function returns a list with the prices of the last hour (60 prices) """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY id DESC LIMIT 60;")
    resultado = consulta.fetchall()
    arr_precios = []
    for i in resultado:
        for i2 in i:
            i2 = int(i2)
            arr_precios.append(i2)
    return arr_precios
            
def traer_masviejo_precio_eth():
    """ This function returns the oldest price in the table that corresponds to the one 24 hours ago """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    price = 1
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_mayor_24_eth():
    """ This function returns the highest price of the last 24 hours """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY price DESC LIMIT 1;")
    resultado = consulta.fetchall()
    res = 1
    for i in resultado:
        for i2 in i:
            res = i2
    return res

def traer_menor_24_eth():
    """ This function returns the smallest price of the last 24 hours """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY price ASC LIMIT 1;")
    resultado = consulta.fetchall()
    res = 1
    for i in resultado:
        for i2 in i:
            res = i2
    return res


""" TENDENCIAS """

def insert_new_tendencia(name, average, min_price, max_price, openprice, closeprice):
    """ This function makes an insert to the trends table with 
        the average, minimum and maximum price of the last hour """

    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    format_time = "%Y-%m-%d %H:%M:%S"
    date = datetime.now().strftime(format_time)
    consulta.execute("INSERT INTO tendencias (name, average, max, min, open, close, date) VALUES ('" + name  +"', '" + average +"', '" + max_price + "', '" + min_price + "', '" + openprice + "', '" + closeprice + "','" + date + "');")
    nuevaconexion.commit()

""" USERS INSERTS """

def insert_new_user(name, mail):
    """ This function inserts a new user to the database """

    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("INSERT INTO users_sigma (name, mail) VALUES ('" + name  +"', '" + mail +"');")
    nuevaconexion.commit()

def traer_users():
    """ This function return a list with name and mail of all the users that we have saved in the database """

    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT name, mail FROM users_sigma;")
    resultado = consulta.fetchall()
    arr_correos = []
    for i in resultado:
        for i2 in i:
            arr_correos.append(i2)
    return arr_correos
