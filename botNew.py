#!/usr/bin/python
import telepot, time

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		print ('Got command: %s' % command)

		if  'Información del sensor' in command:
			bot.sendMessage(chat_id, "Hola tu sensor sirve")

# Creates a bot using the token provided by BotFather
bot = telepot.Bot('378950281:AAH_r7rhTFX2NwdMl9fDrUw48A0MZ4gjXXA')

# Add the handle function to be called every new received message
bot.message_loop(handle)

# Wait for new messages
while 1:
	time.sleep(20)
    