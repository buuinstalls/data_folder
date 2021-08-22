# Importing

import os
import time
import colorama
import webbrowser as wb
import ctypes

# Variables

normal = "\u001b[0m"

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

# Function

def cprint(string):
    print(yellow + ":: " + normal + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    - " + normal + string)
# ---------------------------------------------
def cerror(string):
    print(red + "#: " + normal + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    #- " + normal + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "?> " + normal + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    ?> " + normal + string)
# ---------------------------------------------
def cnotice(string):
    print(green + "!> " + normal + string)
# ---------------------------------------------
def scnotice(string):
    print(green + "    !> " + normal + string)
# ---------------------------------------------
def cinput(string):
    input(yellow + ":: " + normal + string)
# ---------------------------------------------
def scinput(string):
    input(yellow + "    - " + normal + string)
# ---------------------------------------------
def cmdinput(string):
    input(green + ">> " + normal + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)

# Check

def get_user():
    return os.getenv('USER', os.getenv('USERNAME', 'user'))

# Stuff



# Script Function



# Thingy

os.system("cls")
cprint("Hello, " + get_user())
time.sleep(.3)
os.system("cls")

commands = ['cmds', 'tools']
othercommands = ['close', 'home', 'updatecheck']
toolcommands = ['ping', 'ipconfig']
################################
cmddesc = ['Displays Commands', 'Displays the tool dashboard']
cmddesco = ['Closes the program', 'Goes to homepage', 'Check for updates']
cmddesct = ['Pings an ip [DONT DO ping (args) i will implement arg detection soon]', 'Show your IPConfiguration']
version = "v1.01"

# Descriptions are sorted by order

wait(.3)
print(red + '''
        .-.-.-..-..-..---. .-..---..--. 
        | | | | >  / | |-< | || | || \ |
        `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        b
''')
wait(.08)
os.system("cls")
print(green + '''
        .-.-.-..-..-..---. .-..---..--. 
        | | | | >  / | |-< | || | || \ |
        `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        u
''')
wait(.08)
os.system("cls")
print(blue + '''
        .-.-.-..-..-..---. .-..---..--. 
        | | | | >  / | |-< | || | || \ |
        `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        u
''')
wait(.08)
os.system("cls")
print(yellow + '''
        .-.-.-..-..-..---. .-..---..--. 
        | | | | >  / | |-< | || | || \ |
        `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        ''' + version + '''
        Made by buu#1662
'''.center(80))
cinfo("Make sure to say 'cmds' for the commands")
scinfo("a fully operating useless cmd console")
scinfo("myriad console | buu#1662")

# Main

def mainscript():
    cmdinput = input(green + ">> " + normal + "")
    os.system("cls")
    if cmdinput == commands[0]:
        os.system("cls")
        print(yellow + '''
        .-.-.-..-..-..---. .-..---..--. 
        | | | | >  / | |-< | || | || \ |
        `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        ''' + version + '''
        Made by buu#1662
        '''.center(80))

        cinfo('''
    Heres a list of the commands:
    -----------------------------
        ''')
        scinfo(commands[0] + " : " + cmddesc[0])
        scinfo(commands[1] + " : " + cmddesc[1])
        print("    ----------------------------")
        scinfo(othercommands[0] + " : " + cmddesco[0])
        scinfo(othercommands[1] + " : " + cmddesco[1])
        scinfo(othercommands[2] + " : " + cmddesco[2])
        print("    ----------------------------")
        scinfo(toolcommands[0] + " : " + cmddesct[0])
        scinfo(toolcommands[1] + " : " + cmddesct[1])
        print("    ----------------------------")
        scinfo("If the commands don't work")
        scinfo("It's either bugged or being")
        scinfo("Worked on.")
        cmdline()
    elif cmdinput == commands[1]:
        os.system("cls")
        print(yellow + '''
        h
        ''')
        cinfo("Attempting to execute")
        scinfo("TOOLS - v1.00 (debug)")
        print("      ----------------------")
        scinfo(toolcommands[0] + " : idk")
        cmdline()
    elif cmdinput == othercommands[0]:
        os.system("cls")
        cerror("bye")
        time.sleep(.5)
    elif cmdinput == othercommands[1]:
        os.system("cls")
        print(yellow + '''
        .-.-.-..-..-..---. .-..---..--. 
        | | | | >  / | |-< | || | || \ |
        `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        ''' + version + '''
        Made by buu#1662
        '''.center(80))
        cinfo("Make sure to say 'cmds' for the commands")
        scinfo("a fully operating useless cmd console")
        scinfo("myriad console | buu#1662")
        cmdline()
    elif cmdinput == othercommands[2]:
        print(blue + '''
.-.-.-..-..-..---. .-..---..--. 
| | | | >  / | |-< | || | || \ |
`-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        ''')
        cinfo("Checking for updates")
        scinfo("This command is unfinished")
        scinfo("soz")
        cmdline()
    elif cmdinput == toolcommands[0]:
        print(green + '''
.-.-.-..-..-..---. .-..---..--. 
| | | | >  / | |-< | || | || \ |
`-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
                ''')
        cnotice("Establishing pinger")
        scnotice("Established!- Please input the website or IP address")
        webip = input(green + ">> " + normal + "")
        os.system("ping -a " + webip + "")
        cnotice("Enter new command below - type ping to ping again")
        cmdline()
    elif cmdinput == toolcommands[1]:
        print(green + '''
.-.-.-..-..-..---. .-..---..--. 
| | | | >  / | |-< | || | || \ |
`-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        ''')
        cnotice("Are you sure you want to show [ipconfig]? (y/n)")
        sipc = input(green + ">> " + normal + "")
        if sipc == "y":
            os.system('ipconfig')
            cnotice("Enter new command below")
            cmdline()
        else:
            cnotice("Enter new command below")
            cmdline()
    else:
        cerror("Unknown Command.")
        cmdline()

def cmdline():
    mainscript()

mainscript()
