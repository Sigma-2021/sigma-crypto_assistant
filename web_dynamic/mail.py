#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """
import os
import time

""" IMPORTS FILES """
import persistence
import percent


def hacer_resumen():
    """ Stores the mail body to be send in resumen """

    resumen = "This is your compilation of relevant information about cryptocurrencies today.\n\n"
    """ add btc information """
    resumen += "BITCOIN INFORMATION:\n\n"
    resumen += "The current price of bitcoin at the time of this email is U$S "
    resumen += str(persistence.traer_ultimo_precio_btc()) + "\n"
    resumen += "in the last 24 hours its price has moved "
    resumen += str(percent.porcentaje_btc_24()) + "%\n"
    resumen += "and yesterday at this same time, the bitcoin cost U$S"
    resumen += str(persistence.traer_masviejo_precio_btc()) + "\n\n"
    """ add doge information"""
    resumen += "DOGECOIN INFORMATION:\n\n"
    resumen += "The current price of dogecoin at the time of this email is U$S "
    resumen += str(persistence.traer_ultimo_precio_doge()) + "\n"
    resumen += "in the last 24 hours its price has moved "
    resumen += str(percent.porcentaje_doge_24()) + "%\n"
    resumen += "and yesterday at this same time, the doge coin cost U$S "
    resumen += str(persistence.traer_masviejo_precio_doge()) + "\n\n"
    """ add eth information"""
    resumen += "ETHEREUM INFORMATION:\n\n"
    resumen += "The current price of ethereum at the time of this email is U$S "
    resumen += str(persistence.traer_ultimo_precio_eth()) + "\n"
    resumen += "in the last 24 hours its price has moved "
    resumen += str(percent.porcentaje_eth_24()) + "%\n"
    resumen += "and yesterday at this same time, the ethereum coin cost U$S "
    resumen += str(persistence.traer_masviejo_precio_eth()) + "\n\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    return str(resumen)

def daily_resume():
    """ Sends what hacer_resumen() writes adding the subject of the mail """

    resumen = hacer_resumen()
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Daily Resume\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")

def resumen_alerta_btc(porcentaje):
    """ Called by percent.chequear_movimientos() when a constant variations is detected to send an alert """

    if porcentaje > 0:
        resumen = "The price of BTC is on a constant raise, now at U$S "
    else:
        resumen = "The price of BTC is on a steady decent, now at U$S "
    resumen += str(persistence.traer_ultimo_precio_btc()) + " , take a look!\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/bitcoin\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Alert\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")


def resumen_alerta_doge(porcentaje):
    """ Called by percent.chequear_movimientos() when a constant variations is detected to send an alert """

    if porcentaje > 0:
        resumen = "The price of DOGE is on a constant raise, now at U$S "
    else:
        resumen = "The price of DOGE is on a steady decent, now at U$S "
    resumen += str(persistence.traer_ultimo_precio_doge()) + " , take a look!\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Alert\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")

def resumen_alerta_eth(porcentaje):
    """ Called by percent.chequear_movimientos() when a constant variations is detected to send an alert """

    if porcentaje > 0:
        resumen = "The price of ETH is on a constant raise, now at U$S "
    else:
        resumen = "The price of ETH is on a steady decent, now at U$S "
    resumen += str(persistence.traer_ultimo_precio_eth()) + " , take a look!\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Alert\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")

def mail_pico_btc(porcentaje):
    """ Called by detectar_picos() sendas a mail """

    if porcentaje > 0:
        resumen = "Bitcoin is on a quick rise, now at U$S "
    else:
        resumen = "Bitcoin is on a quick dip, now at U$S "
    resumen += str(persistence.traer_ultimo_precio_btc()) + " , take a look!\n\n\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Alert\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")

def mail_pico_doge(porcentaje):
    """ Called by detectar_picos() sendas a mail """

    if porcentaje > 0:
        resumen = "Dogecoin is on a quick rise, now at U$S "
    else:
        resumen = "Dogecoin is on a quick dip, now at U$S "
    resumen += str(persistence.traer_ultimo_precio_doge()) + " , take a look!\n\n\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Alert\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")

def mail_pico_eth(porcentaje):
    """ Called by detectar_picos() sendas a mail """

    if porcentaje > 0:
        resumen = "Ethereum is on a quick rise, now at U$S "
    else:
        resumen = "Ethereum is on a quick dip, now at U$S "
    resumen += str(persistence.traer_ultimo_precio_eth()) + " , take a look!\n\n\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: sigma.cryptocurrency.assistant@gmail.com\nSubject: Alert\nDear " + nombre + ",\n" + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")