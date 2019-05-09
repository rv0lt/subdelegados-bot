#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
#   Bot programado usando la libreria de pyTelegramBot que se puede encontrar en
#   https://github.com/eternnoir/pyTelegramBotAPI
#
#  author: rv0lt
#  agradecimientos a Sarah por la idea

import telebot
import time
import random
# Escribir aqui el token que el botFather te ha generado
bot_token = "TOKEN"

bot = telebot.TeleBot(token=bot_token)


# lista con los cargos que se pueden generar
cargos = [
    "Perder el Juego",
    "Segundas Matriculas",
    "VOX",
    "Folios",
    "Asuntos Nazis",
    "Estudiantes",
    "Suspender",
    "la Vaselina",
    "la Desinformacion",
    "subdelegable",
    "sancionar(@LuisPla)",
    "'Error 404 subdelegado not found'",
    "la Delegacion",
    "Matar Patos",
    "la Realidad",
    "la Vida Moderna",
    "Machirulos",
    "la subdelegacion de subdelegados",
    "las Gemas del Infinito",
    "Bolis-DAUPM",
    "Murcia(Send Agua)",
    "Suspender",
    "Pingüinos",
    "Gatos",
    "Reclutamiento",
    "Etiquetas",
    "Dineros",
    "Desigualdad",
    "Cuñados",
    "Tizas",
    "el Inframundo",
    "Arbustos"

]
frases = [
    "La representación es a la ilusión como el grinch a la navidad, la diferencia es que el grinch se vuelve bueno al final"
    ,
    "Los perros son gatos que hacen pis en la calle",
    "Necesito un chupitazo para aguantar esta reunión",
    "Yo antes tenía vida, luego entre en representación",
    "La universidad me ha consumido"
]
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Consigue tu cargo de representación y podrás ser la envidia de CREUP")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "Para más info  https://t.me/SUBDELEGADODESUBDELEGADOS")
@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")

@bot.message_handler(commands=["cargo"])
def dar_cargo(message):
    sel=random.choice(cargos)
    texto="Subdelegado de " + sel
    bot.reply_to(message, texto)

@bot.message_handler(commands=["frase"])
def frase_motivadora(message):
    bot.reply_to(message, random.choice(frases))


@bot.message_handler(commands=["opinion"])
def sarahHater(message):
    video = open('/home/subdelegadosbot/hater.mp4', 'rb')
    bot.send_video_note(message.chat.id, video)



@bot.message_handler(commands=["sugerencias"])
def sugerencias(message):
    bot.reply_to(message, "Todas las sugerencias sobre el bot pueden hacermelas llegar, mi alias es @rv0lt")
# Lee todos y cada uno de los mensajes enviados y responde dependiendo de si se encuentra alguna determinada palabra
@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
    text = message.text
    at_text = find_at(text)
    if at_text is not None:
        bot.reply_to(message, at_text)


# Funcion que lee un array que contiene palabras en busca de una ocurrencia en concreto
def find_at(text):
    text = text.lower()

    if text.find("creup") != -1:
        return "caca"
    elif text.find("miau") != -1  or text.find("gato") != -1:
        return "gatito :) "
    elif text.find("perro") != -1 or text.find("guau")!=-1:
        return "Perros no, gracias"
    elif text.find("upm") != -1:
        return "Universidad de Puta Madre"
    elif text.find("revu") != -1:
        return "Álvaro Revuelta es el puto amo"
    elif text.find("macedonia") != -1:
        return "Sarah es una macedonia, ¡Bibah!"
    elif text.find("sarah") != -1 or text.find("inma") !=-1 or text.find("zule")!=-1:
        return "Agrogirl"
    elif text.find("daetsiinf") !=-1:
        return "dafi"
    elif text.find("pato") !=-1:
        return "cuac"

    else :
        return None


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)