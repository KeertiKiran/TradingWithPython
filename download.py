import requests
import os
from threading import *
from zipfile import ZipFile

def __write(filename:str , content:bytes):
    with open(filename.replace('\\' , '/') , 'wb') as data:
            data.write(content)

def __get(url:str , filename:str):
    r = requests.get(url , allow_redirects=True ,timeout=5.5)
    try:
        __write(filename , r.content)
    except FileNotFoundError:
        remove_file_name = filename.split('/')[-1]
        print(remove_file_name)
        dir_path = filename.replace(f'/{remove_file_name}' , '').replace('//' , '\\')
        os.makedirs(dir_path , exist_ok=True)
        print(dir_path)
        __write(filename , r.content)

def download(url:str , filename:str) -> str:
    """
    
    Will download the file from the url given and save it to given path.

    """
    d = Thread(target=lambda:__get(url, filename))
    d.start()