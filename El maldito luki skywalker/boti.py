import telebot
from telebot.types import ReplyKeyboardRemove # para eliminar botones
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import InlineKeyboardMarkup # para crear botones inline
from telebot.types import InlineKeyboardButton # para definir los botones inline
from telebot.types import ForceReply 
from telebot import types

usuario = {}

bot = telebot.TeleBot("5550557661:AAHstroLDYUrIlJVDDnEpzyWmyhOi-IyFTg")

@bot.message_handler(commands=["start", "help", "inicio, aqui"])
def send_welcome(message):
	bot.reply_to(message, "Hola!, Soy el bot de prueba.\n Que queres ver hoy?\n /temas\n /ver_practicas \n Hacer una /Consulta_Especifica \nSi queres ver el modelo de practica elegi /Jojo")

@bot.message_handler(commands=["temas"])
def send_message(message):
	bot.reply_to(message, "Este apartado no se encuentra disponible.\n Volver al inicio /start \n Ir a /ver_practicas \n Hacer una /Consulta_Especifica")

#----------------------------------------------------CONSULTAS ESPECIFICAS----------------------------------------------------#

@bot.message_handler(commands=["Consultas_Especificas"])
def send_message(message):
	bot.reply_to(message, "Okey! ¿Que te gustaria consultar?\n /Quimica_General \n /Quimica_Organica \n /Quimica_Inorganica \n /pyoQ \n Si te confundiste quedate tranquilo que puedes volver al inicio /start")

#Consultas especificas de Quimica General

@bot.message_handler(commands=["Quimica_General"])
def send_message(message):
	bot.reply_to(message, "¿Cuales son tus dudas? \n /¿Que_es_nashe? \n /¿Que_es_god? \n /¿Que_es_eneazi? \n /¿Que_es_eso? \n /¿Que_es_queso?")

@bot.message_handler(commands=["¿Que_es_nashe?"])
def send_message(message):
	bot.reply_to(message, "Nashe es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_General otra vez")

@bot.message_handler(commands=["¿Que_es_god?"])
def send_message(message):
	bot.reply_to(message, "god es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_General otra vez")

@bot.message_handler(commands=["¿Que_es_eneazi?"])
def send_message(message):
	bot.reply_to(message, "eneazi es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_General otra vez")

@bot.message_handler(commands=["¿Que_es_eso?"])
def send_message(message):
	bot.reply_to(message, "eso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_General otra vez")

@bot.message_handler(commands=["¿Que_es_queso?"])
def send_message(message):
	bot.reply_to(message, "Queso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_General otra vez")

#Consultas Especificas Quimica Organica

@bot.message_handler(commands=["Quimica_Organica, Quimica_Organica_otra_vez"])
def send_message(message):
	bot.reply_to(message, "¿Cuales son tus dudas? \n /¿Que_es_nashe? \n /¿Que_es_god? \n /¿Que_es_eneazi? \n /¿Que_es_eso? \n /¿Que_es_queso?")

@bot.message_handler(commands=["¿Que_es_nashe?"])
def send_message(message):
	bot.reply_to(message, "Nashe es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Organica otra vez")

@bot.message_handler(commands=["¿Que_es_god?"])
def send_message(message):
	bot.reply_to(message, "god es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Organica otra vez")

@bot.message_handler(commands=["¿Que_es_eneazi?"])
def send_message(message):
	bot.reply_to(message, "eneazi es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Organica otra vez")

@bot.message_handler(commands=["¿Que_es_eso?"])
def send_message(message):
	bot.reply_to(message, "eso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Organica otra zez")

@bot.message_handler(commands=["¿Que_es_queso?"])
def send_message(message):
	bot.reply_to(message, "Queso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Organica otra vez")

#Consultas especificas Quimica Inorganica

@bot.message_handler(commands=["Quimica_Organica, Quimica_Inorganica_otra_vez"])
def send_message(message):
	bot.reply_to(message, "¿Cuales son tus dudas? \n /¿Que_es_nashe? \n /¿Que_es_god? \n /¿Que_es_eneazi? \n /¿Que_es_eso? \n /¿Que_es_queso?")

@bot.message_handler(commands=["¿Que_es_nashe?"])
def send_message(message):
	bot.reply_to(message, "Nashe es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica Inorganica otra vez")

@bot.message_handler(commands=["¿Que_es_god?"])
def send_message(message):
	bot.reply_to(message, "god es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Inorganica otra vez")

@bot.message_handler(commands=["¿Que_es_eneazi?"])
def send_message(message):
	bot.reply_to(message, "eneazi es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Inorganica otra vez")

@bot.message_handler(commands=["¿Que_es_eso?"])
def send_message(message):
	bot.reply_to(message, "eso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Inorganica otra vez")
@bot.message_handler(commands=["¿Que_es_queso?"])

def send_message(message):
	bot.reply_to(message, "Queso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /Quimica_Inorganica otra vez")

#Consultas Especificas pyoQ

@bot.message_handler(commands=["Quimica_Organica, pyoQ_otra_vez"])
def send_message(message):
	bot.reply_to(message, "¿Cuales son tus dudas? \n /¿Que_es_nashe? \n /¿Que_es_god? \n /¿Que_es_eneazi? \n /¿Que_es_eso? \n /¿Que_es_queso?")

@bot.message_handler(commands=["¿Que_es_nashe?"])
def send_message(message):
	bot.reply_to(message, "Nashe es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /pyoQ otra vez")

@bot.message_handler(commands=["¿Que_es_god?"])
def send_message(message):
	bot.reply_to(message, "god es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /pyoQ otra vez")

@bot.message_handler(commands=["¿Que_es_eneazi?"])
def send_message(message):
	bot.reply_to(message, "eneazi es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /pyoQ otra vez")

@bot.message_handler(commands=["¿Que_es_eso?"])
def send_message(message):
	bot.reply_to(message, "eso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /pyoQ otra vez")

@bot.message_handler(commands=["¿Que_es_queso?"])
def send_message(message):
	bot.reply_to(message, "Queso es.... \n Si tus dudas fueron resuelta puesdes volver al inicio /start \n Hacer otra /Consulta_Especifica \n O puedes consultar sobre /pyoQ otra vez")
