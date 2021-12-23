import telegram
import picamera


# Connect to our bot
bot = telegram.Bot("5063108285:AAEPiZjs0OL2dhkWh3vudSl5MHDhCzQ8kJ8")

# Sets the id for the active chat
chat_id= 5058934063

#Get the photo
camera=picamera.PiCamera()
camera.capture('/home/pi/Pictures/capture.jpg')
camera.close()

# Sends a message to the chat
bot.sendPhoto(chat_id=chat_id, photo=open('/home/pi/Pictures/capture.jpg', 'rb'))
