
# coding: utf-8

# In[31]:

import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import sys
import glob
import importlib.util
import re

#TELEGRAM BOT PARAMS
TOKEN = '713108177:AAGGYJjhB_Pvftffz-F13xz-k5KG3XLlJGo'
BOTNAME = '/TripleVBot'

# Get file paths of all modules.
MODULES_PATH = glob.glob('modules/*.py')


def handle(msg):
    chat_id = msg['chat']['id']

    #print msg['text']
    a_text = msg['text'].split(" ")
    command = a_text[0]
    if a_text[0] == BOTNAME:
        a_text.pop(0)
        if len(a_text) > 0:
            command = a_text[0]

    print('Got command: %s' % command)

    msg = ""
    found_bool = False
    #check command name
    for module in all_commands.keys():
        if all_commands[module] != None:
            if command in all_commands[module].keys():
                a_text.pop(0)
                module_name = getattr(sys.modules[__name__] ,module)
                method_to_run = getattr(module_name, all_commands[module][command]["method"])
                msg = method_to_run(a_text)
                found_bool = True
                break

    if(not found_bool):
        msg = "Chiedi una delle seguenti cose:\n"
        for module in all_commands.keys():
            if all_commands[module] != None:
                for command in all_commands[module].keys():
                    msg = str(msg) + str(command)+": "+ all_commands[module][command]["notes"]+ "\n"
                msg = msg + "\n"

    bot.sendMessage(chat_id, msg)


all_commands = {}
for m in MODULES_PATH:
    url = 'modules/'
    m_name = re.sub('modules/', '', m)
    m_name = re.sub('.py','', m_name)
    spec = importlib.util.spec_from_file_location(m_name, m)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    all_commands[m] = foo.get_my_commands()

bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)


# In[ ]:
