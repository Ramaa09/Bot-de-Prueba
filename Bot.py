import telebot
from telebot.types import ReplyKeyboardRemove # para eliminar botones
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import InlineKeyboardMarkup # para crear botones inline
from telebot.types import InlineKeyboardButton # para definir los botones inline
from telebot.types import ForceReply 
from telebot import types

usuario = {}

bot = telebot.TeleBot("5550557661:AAHstroLDYUrIlJVDDnEpzyWmyhOi-IyFTg")

@bot.message_handler(commands=["start", "inicio"])
def send_welcome(message):
	bot.reply_to(message, "Hola!, Soy el bot de prueba.\n Que queres ver hoy?\n /temas\n /ver_practicas\nSi queres ver el modelo de practica elegi /Jojo")

@bot.message_handler(commands=["temas"])
def send_message(message):
	bot.reply_to(message, "Este apartado no se encuentra disponible.\n Volver al inicio /start\n Ir a /ver_practicas ")


@bot.message_handler(commands=["ver_practicas"])
def send_message(message):
	bot.reply_to(message, "De que materia te gustaria ver?\n /general\n /pyoQ")

@bot.message_handler(commands=["general"])
def send_message(message):
	bot.reply_to(message, "Que practicas te gustaria ver?\n /soluciones\n /titulacion_Acido_Base")

#Aca irian las practicas de /soluciones y /titulacion_Acido_Base

@bot.message_handler(commands=["pyoQ"])
def send_message(message):
	bot.reply_to(message, "Que practicas te gustaria ver?\n /calorimetria\n /punto_de_fusion")

#Aca irian las practicas de /calorimetria y /punto_de_fusion


        #Aca va un modelo de practica
 
    
@bot.message_handler(commands=["Jojo"])
def command_practica_x_paso1(message):
        respuesta = "Miño Facha"
        cid = message.chat.id
        usuario[cid] = respuesta
        botones = ReplyKeyboardMarkup(input_field_placeholder="Elige una opción")
        botones.add("Miño Facha", "No se, soy de Boca")
        msg = bot.send_photo(message.chat.id, open("./imagenes/larva.jpg", "rb"), "Es una pregunta muy fácil, no te preocupes😁.\nSi te digo que tengo una solución(sc) de 470gr y un soluto(sto) de 125gr ¿Cual es la opcion correcta?", reply_markup = botones)
    
        # registramos la respuesta 
        bot.register_next_step_handler(msg, comprobacion_respuesta_1)

def comprobacion_respuesta_1(message):
    # Correccion
      cid = message.chat.id
      if message.text.isdigit():
         msg = bot.send_message(message.chat.id, "Error: elegí una de las opciones.")
         bot.register_next_step_handler(msg, comprobacion_respuesta_1)
      else:
         n = message.text
         if n != "Miño Facha" and "No se, soy de Boca" :
             msg = bot.send_message(message.chat.id, "Error: Opcion Incorrecta. ")
             bot.register_next_step_handler(msg, comprobacion_respuesta_1)
         else:
             if n == usuario[cid]:
                 markup = ReplyKeyboardRemove()
                 bot.reply_to(message, "Muy Bien!!!, pulsa /Jojo para continuar la practica", reply_markup = markup)
                 bot.register_next_step_handler(message, command_practica_x_paso2)
                 return

#Paso 2

def command_practica_x_paso2(message):
        respuesta_1 = "opcion_a"
        cid = message.chat.id
        usuario[cid] = respuesta_1
        botones = ReplyKeyboardMarkup(input_field_placeholder="Elige una opción")
        botones.add("opcion_a", "opcion_b")
        msg = bot.send_photo(message.chat.id, open("./imagenes/spidy.jpg", "rb"), "Es una pregunta muy fácil, no te preocupes😁.\nSi te digo que tengo una solución(sc) de 470gr y un soluto(sto) de 125gr ¿De que color es el caballo blanco de San Martin?", reply_markup = botones)
    
        # registramos la respuesta 
        bot.register_next_step_handler(msg, comprobacion_respuesta_2)

def comprobacion_respuesta_2(message):
    # Correccion
      cid = message.chat.id
      if message.text.isdigit():
         msg = bot.send_message(message.chat.id, "Error: elegí una de las opciones.")
         bot.register_next_step_handler(msg, comprobacion_respuesta_2)
      else:
         n = message.text
         if n != "opcion_a" and "opcion_b" :
             msg = bot.send_message(message.chat.id, "Error: Opcion Incorrecta. ")
             bot.register_next_step_handler(msg, comprobacion_respuesta_2)
         else:
             if n == usuario[cid]:
                 markup = ReplyKeyboardRemove()
                 bot.reply_to(message, "Muy Bien!!!, pulsa /Jojo para continuar la practica", reply_markup = markup)
                 bot.register_next_step_handler(message, command_practica_x_paso3)
                 return

#Paso 3

def command_practica_x_paso3(message):
        respuesta_2 = "opcion_a"
        cid = message.chat.id
        usuario[cid] = respuesta_2
        botones = ReplyKeyboardMarkup(input_field_placeholder="Elige una opción")
        botones.add("opcion_a", "opcion_b")
        msg = bot.send_photo(message.chat.id, open("./imagenes/roki.jpg", "rb"), "Es una pregunta muy fácil, no te preocupes😁.\nSi te digo que tengo una solución(sc) de 470gr y un soluto(sto) de 125gr ¿Quien es mas grande?", reply_markup = botones)
    
        # registramos la respuesta 
        bot.register_next_step_handler(msg, comprobacion_respuesta_3)

def comprobacion_respuesta_3(message):
    # Correccion
      cid = message.chat.id
      if message.text.isdigit():
         msg = bot.send_message(message.chat.id, "Error: elegí una de las opciones.")
         bot.register_next_step_handler(msg, comprobacion_respuesta_3)
      else:
         n = message.text
         if n != "opcion_a" and "opcion_b" :
             msg = bot.send_message(message.chat.id, "Error: Opcion Incorrecta. ")
             bot.register_next_step_handler(msg, comprobacion_respuesta_3)
         else:
             if n == usuario[cid]:
                 markup = ReplyKeyboardRemove()
                 bot.reply_to(message, "Muy Bien!!!\n Hasta aca llega la practica\n Aca va una conclusion\n Clickea /inicio para volver al inicio\n O /Jojo para volver a realizar esta practica", reply_markup = markup)
                 return

print('Iniciamos el bot')
bot.infinity_polling()
print('Bot iniciado')


# Desktop\Bot\Bot de Prueba