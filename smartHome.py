
# coding: utf-8

# In[31]:

import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

import shoppingList
import camera
import sys
#sys.path.insert(0, '/path/to/application/app/folder')
import re


# In[73]:

def handle(msg):
    chat_id = msg['chat']['id']
    
    #print msg['text']
    a_text = msg['text'].split(" ")
    command = a_text[0]
    
    print 'Got command: %s' % command
    
    msg = ""
    found_bool = False
    #check command name
    for module in all_commands.keys():
        if command in all_commands[module].keys():
            a_text.pop(0)
            module_name = getattr(sys.modules[__name__] ,module)
            method_to_run = getattr(module_name, all_commands[module][command]["method"])
            msg = method_to_run(a_text)
            found_bool = True

    if(not found_bool):
        msg = "Insert a correct command name.\n"
        for module in all_commands.keys():   
            msg = msg + "In case is "+str(module)+" then the commands are:\n"
            for command in all_commands[module].keys():
                msg = str(msg) + str(command)+": "+ all_commands[module][command]["notes"]+ "\n"
            msg = msg + "\n"

    bot.sendMessage(chat_id, msg["text"])
    if "photo" in msg.keys():
        bot.sendPhoto(chat_id, msg["photo"])

all_commands = {}
all_commands["shoppingList"] = shoppingList.get_my_commands()
all_commands["camera"] = camera.get_my_commands()
token = '217399231:AAEH7BKYl07svmbCnqyiEVQTYYM40o_vv0w'
bot = telepot.Bot(token)

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)


# In[ ]:



