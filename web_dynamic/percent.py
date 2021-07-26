#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """
import os
import time

""" IMPORTS FILES """
import persistence
import mail

def porcentaje_btc_24():
    """ Calculates the porcentile variation of btc in 24hs """

    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_btc()
    nuevo = persistence.traer_ultimo_precio_btc()
    viejo = int(viejo)
    nuevo = int(nuevo)
    porcentaje = 100 * (nuevo - viejo) / viejo
    porcentaje = round(porcentaje, 2)
    return porcentaje

def porcentaje_doge_24():
    """ Calculates the porcentile variation of doge in 24hs """

    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_doge()
    nuevo = persistence.traer_ultimo_precio_doge()
    viejo = float(viejo)
    nuevo = float(nuevo)
    porcentaje = 100 * (nuevo - viejo) / viejo
    porcentaje = round(porcentaje, 2)
    return porcentaje

def porcentaje_eth_24():
    """ Calculates the porcentile variation of eth in 24hs """

    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_eth()
    nuevo = persistence.traer_ultimo_precio_eth()
    viejo = int(viejo)
    nuevo = int(nuevo)
    porcentaje = 100 * (nuevo - viejo) / viejo
    porcentaje = round(porcentaje, 2)
    return porcentaje

def calcular_porcentaje(viejo, nuevo):
    """ Recives two numbers and returns the diference in porcentaje """

    viejo = viejo
    nuevo = nuevo
    return 100 * (nuevo - viejo) / viejo

def detectar_constantes_btc():
    """ Looks for a constant variation in btc """

    ultimos_precios = persistence.traer_ultimos_precios_btc()
    prev = int(ultimos_precios[0])
    porcentaje = 0
    counter = 0
    for i in range(1,60):
        if prev < int(ultimos_precios[i]):
            counter = counter + 1
        elif prev > int(ultimos_precios[i]):
            counter = counter - 1
        prev = int(ultimos_precios[i])
    porcentaje = calcular_porcentaje(int(ultimos_precios[0]), int(ultimos_precios[i]))
    porcentaje = round(porcentaje, 2)
    if counter > 10 and porcentaje > 1:
        return porcentaje
    elif counter < -10 and porcentaje < -1:
        return porcentaje
    else:
        return 0

def detectar_constantes_doge():
    """ Looks for a constant variation in doge """

    ultimos_precios = persistence.traer_ultimos_precios_doge()
    prev = float(ultimos_precios[0])
    porcentaje = 0
    counter = 0
    for i in range(1,60):
        if prev < float(ultimos_precios[i]):
            counter = counter + 1
        elif prev > float(ultimos_precios[i]):
            counter = counter - 1
        prev = float(ultimos_precios[i])

    porcentaje = calcular_porcentaje(float(ultimos_precios[0]), float(ultimos_precios[i]))
    porcentaje = round(porcentaje, 2)
    if counter > 10 and porcentaje > 1:
        return porcentaje
    elif counter < -10 and porcentaje < -1:
        return porcentaje
    else:
        return 0

def detectar_constantes_eth():
    """ Looks for a constant variation in eth """

    ultimos_precios = persistence.traer_ultimos_precios_eth()
    prev = int(ultimos_precios[0])
    porcentaje = 0
    counter = 0
    for i in range(1,60):
        if prev < int(ultimos_precios[i]):
            counter = counter + 1
        elif prev > int(ultimos_precios[i]):
            counter = counter - 1
        prev = int(ultimos_precios[i])
    porcentaje = calcular_porcentaje(int(ultimos_precios[0]), int(ultimos_precios[i]))
    porcentaje = round(porcentaje, 2)
    if counter > 10 and porcentaje > 1:
        return porcentaje
    elif counter < -10 and porcentaje < -1:
        return porcentaje
    else:
        return 0

def detectar_pico_btc():
    """ Looks for a significant variation in btc """

    ultimos_precios = persistence.traer_ultimos_precios_btc()
    prev = int(ultimos_precios[0])
    now = int(ultimos_precios[1])
    porcentaje = 0

    porcentaje = calcular_porcentaje(prev, now)
    porcentaje = round(porcentaje, 2)
    if porcentaje > 1.5 or porcentaje < -1.5:
        return porcentaje
    return 0

def detectar_pico_doge():
    """ Looks for a significant variation in doge """

    ultimos_precios = persistence.traer_ultimos_precios_doge()
    prev = float(ultimos_precios[0])
    now = float(ultimos_precios[1])
    porcentaje = 0

    porcentaje = calcular_porcentaje(prev, now)
    porcentaje = round(porcentaje, 2)
    if porcentaje > 1.5 or porcentaje < -1.5:
        return porcentaje
    return 0

def detectar_pico_eth():
    """ Looks for a significant variation in eth """

    ultimos_precios = persistence.traer_ultimos_precios_eth()
    prev = int(ultimos_precios[0])
    now = int(ultimos_precios[1])
    porcentaje = 0

    porcentaje = calcular_porcentaje(prev, now)
    porcentaje = round(porcentaje, 2)
    if porcentaje > 1.5 or porcentaje < -1.5:
        return porcentaje
    return 0

    
def chequear_movimientos(a):
    """ Checks what detectar_constantes_coin() returns """

    res = detectar_constantes_btc()
    if res != 0 and a != 3 and a != 7 and  a!= 8 and a != 12:
        mail.resumen_alerta_btc(res)
        a += 3

    res = detectar_constantes_doge()
    if res != 0 and a != 4 and a != 7 and a != 9 and a != 12:
        mail.resumen_alerta_doge(res)
        a += 4

    res = detectar_constantes_eth()
    if res != 0 and a != 5 and a != 9 and a != 8 and a != 12:
        mail.resumen_alerta_eth(res)
        a += 5
    return a


def detectar_picos(a):
    """ """

    res = detectar_pico_btc()
    if res != 0 and a != 3 and a != 7 and  a!= 8 and a != 12:
        mail.mail_pico_btc(res)
        a += 3
    
    res = detectar_pico_doge()
    if res != 0 and a != 4 and a != 7 and a != 9 and a != 12:
        mail.mail_pico_doge(res)
        a += 4

    res = detectar_pico_eth()
    if res != 0 and a != 5 and a != 9 and a != 8 and a != 12:
        mail.mail_pico_eth(res)
        a += 5
    
    return a


def insert_in_tendencias():
    """ Inserts information of the last hour in tendencias table """

    ultimos = persistence.traer_ultimos_precios_doge()
    average_doge = sum(ultimos) / len(ultimos)
    min_price_doge = min(ultimos)
    max_price_doge = max(ultimos)
    openprice = persistence.traer_masviejo_precio_doge()
    closeprice = persistence.traer_ultimo_precio_doge()
    persistence.insert_new_tendencia("DOGE", str(average_doge), str(min_price_doge), str(max_price_doge), str(openprice), str(closeprice))

    ultimos = persistence.traer_ultimos_precios_btc()
    average_btc = sum(ultimos) / len(ultimos)
    min_price_btc = min(ultimos)
    max_price_btc = max(ultimos)
    openprice = persistence.traer_masviejo_precio_btc()
    closeprice = persistence.traer_ultimo_precio_btc()
    persistence.insert_new_tendencia("BTC", str(average_btc), str(min_price_btc), str(max_price_btc), str(openprice), str(closeprice))

    ultimos = persistence.traer_ultimos_precios_eth()
    average_eth = sum(ultimos) / len(ultimos)
    min_price_eth = min(ultimos)
    max_price_eth = max(ultimos)
    openprice = persistence.traer_masviejo_precio_eth()
    closeprice = persistence.traer_ultimo_precio_eth()
    persistence.insert_new_tendencia("ETH", str(average_eth), str(min_price_eth), str(max_price_eth), str(openprice), str(closeprice))
