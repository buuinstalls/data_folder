# Importing

import os
import time
import colorama
import webbrowser as wb
import ctypes
import random

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
toolcommands = ['ping', 'ipconfig', 'cls', 'saveinfo']
funcommands = ['vbucks', 'robux', 'indian_scammer']
################################
cmddesc = ['Displays Commands', 'Displays the tool dashboard']
cmddesco = ['Closes the program', 'Goes to homepage', 'Check for updates']
cmddesct = ['Pings an ip [DONT DO ping (args) i will implement arg detection soon]', 'Show your IPConfiguration', 'Clears the console', 'Stuff that you saved']
cmddescf = ['Gives ya vBucks, for free.', '/e free', 'Imitates a fake bank that scammers usually use']
version = "v1.01"
###############################
serverstatus = ["Up","Down","Unknown"]
x = random.choice(serverstatus)
x1 = random.choice(serverstatus)
x2 = random.choice(serverstatus)
x3 = random.choice(serverstatus)
x4 = random.choice(serverstatus)
x5 = random.choice(serverstatus)
x6 = random.choice(serverstatus)
###############################
# stuff that the user saves
# could be links, and stuff
savedinfo = ['bruh', 'lol', 'poop']

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

def saveinfoscript():
    print(green + '''
    .-.-.-..-..-..---. .-..---..--. 
    | | | | >  / | |-< | || | || \ |
    `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
            ''')
    cnotice("Displaying your saved data")
    scnotice("Would you like to display or input?")
    scnotice("display/input | show/save")
    showordisplay = input(green + ">> " + normal + "")
    if showordisplay == "display" or showordisplay == "show":
        print("    ----------------------------")
        print(savedinfo)
        cnotice("Enter new command below or type saveinfo again to save/display")
        cmdline()
    elif showordisplay == "input" or showordisplay == "save":
        cnotice("Type in a link, or directory below")
        inputorsave = input(green + ">> " + normal + "")
        savedinfo.insert(inputorsave, savedinfo)
        cnotice("Whatever you typed should've been inserted")
        scnotice("Enter new command below or type saveinfo again to save/display")
        cmdline()
    else:
        cerror("Error:")
        scerror("Did not type correct arguments")#@#

def pingerscript():
    print(green + '''
    .-.-.-..-..-..---. .-..---..--. 
    | | | | >  / | |-< | || | || \ |
    `-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
                    ''')
    cnotice("Establishing pinger")
    scnotice("Established!- Please input the website or IP address")
    webip = input(green + ">> " + normal + "")
    os.system("ping -a " + webip + "")
    cnotice("Would you like to re-run the IP Pinger? (y/n)")
    repeatpinger = input(green + ">> " + normal + "")
    if repeatpinger == "y":
        os.system("cls")
        pingerscript()
    elif repeatpinger == "n":
        os.system("cls")
        startupscript()
    else:
        cerror("Unknown Command.")
        cmdline()

def startupscript():
    os.system("cls")
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
    cmdline()

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
        scinfo(toolcommands[2] + " : " + cmddesct[2])
        scinfo(toolcommands[3] + " : " + cmddesct[3])
        print("    ----------------------------")
        scinfo(funcommands[0] + " : " + cmddescf[0])
        scinfo(funcommands[1] + " : " + cmddescf[1])
        scinfo(funcommands[2] + " : " + cmddescf[2])
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
        scinfo(toolcommands[0] + " : " + cmddesct[0])
        scinfo(toolcommands[1] + " : " + cmddesct[1])
        scinfo(toolcommands[2] + " : " + cmddesct[2])
        scinfo(toolcommands[3] + " : " + cmddesct[3])
        cmdline()
    elif cmdinput == othercommands[0]:
        os.system("cls")
        cerror("bye")
        time.sleep(.5)
    elif cmdinput == othercommands[1]:
        os.system("cls")
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
        # to make sure it loops i made it a function
        # lol
        pingerscript()
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
    elif cmdinput == toolcommands[2]:
        os.system("cls")
        cmdline()
    elif cmdinput == toolcommands[3]:
            cerror("yooooo this doesnt work cause")
            scerror("i cant figure out how to insert")
            scerror("your input to the save data table")
            saveinfoscript()
            cmdline()
    elif cmdinput == funcommands[0]:
        print(blue + '''
.-.-.-..-..-..---. .-..---..--. 
| | | | >  / | |-< | || | || \ |
`-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
        ''')
        cinfo("Preparing vBucks transfer")
        scinfo("Prepared, waiting for servers")
        os.system("ping -a epicgames.com")
        cerror("Error finding servers, ignoring.")
        scerror("nil")
        cnotice("Finding username from EpicGames Launcher")

        def filexists(filePathAndName):
            return os.path.exists(filePathAndName)

        if filexists("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"):
            time.sleep(1)
            os.startfile("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")
            wait(3)
            cnotice("Server1 : " + x)
            wait(0.02)
            cerror("Server2 : " + x1)
            wait(0.02)
            cerror("Server3 : " + x2)
            wait(0.02)
            cnotice("Server4 : " + x3)
            wait(0.02)
            cnotice("Server5 : " + x4)
            wait(0.02)
            cerror("Server6 : " + x5)
            wait(0.02)
            cnotice("Server7 : " + x6)
            wait(0.09)
            cprint("Transferred vBucks")
            wait(0.04)
            cmdline()
        else:
            cerror("EpicGames not found.")
            cmdline()
    elif cmdinput == funcommands[1]:
            print(red + '''
.-.-.-..-..-..---. .-..---..--. 
| | | | >  / | |-< | || | || \ |
`-'-'-' `-'  `-'`-'`-'`-^-'`-'-'
            ''')
            cinfo("Preparing Robux transfer")
            scinfo("Prepared, waiting for servers")
            os.system("ping -a roblox.com")
            cerror("Error finding servers, ignoring.")
            scerror("nil")
            cnotice("Finding username from https://roblox.com")
            wait(3)
            cnotice("Server1 : " + x)
            wait(0.02)
            cerror("Server2 : " + x1)
            wait(0.02)
            cerror("Server3 : " + x2)
            wait(0.02)
            cnotice("Server4 : " + x3)
            wait(0.02)
            cnotice("Server5 : " + x4)
            wait(0.02)
            cerror("Server6 : " + x5)
            wait(0.02)
            cnotice("Server7 : " + x6)
            wait(0.09)
            cprint("Transferred Robux")
            wait(0.04)
            cmdline()
    if cmdinput == funcommands[2]:
        print(blue + "# ONLINE CHASE REFUND SERVER #".center(120))
        print(blue + "Enter your amount")
        funds = input(">> ")
        cinfo("Connecting to server")
        cnotice("Server1 : " + x)
        wait(0.02)
        cerror("Server2 : " + x)
        wait(0.02)
        cerror("Server3 : " + x)
        wait(0.02)
        cnotice("Server4 : " + x)
        wait(0.02)
        cnotice("Server5 : " + x)
        wait(0.02)
        cerror("Server6 : " + x)
        wait(0.02)
        cnotice("Server7 : " + x)
        wait(0.09)
        print(blue + "Transferred " + funds)
        print("omg mam big mistake now let me steal ur money!1!!1")
        cmdline()
    else:
        cerror("Unknown Command.")
        cmdline()

def cmdline():
    mainscript()

mainscript()
