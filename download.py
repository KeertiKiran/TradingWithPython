import requests
import os
from threading import *
from zipfile import ZipFile

def __getcurrent(thread_id:Thread):
    while True:
        if thread_id.is_alive() == False:
            return True

def __write(filename:str , content:bytes):
    with open(filename.replace('\\' , '/') , 'wb') as data:
            data.write(content)

def download(url:str , filename:str):
    """
    
    Will download the file from the url given and save it to given path.

    """
    try:
        r = requests.get(url , allow_redirects=True ,timeout=5.5)
    except requests.exceptions.ReadTimeout:
        pass
    try:
        __write(filename , r.content)
    except FileNotFoundError:
        _extracted_from_download_10(filename, r)
    except UnboundLocalError:
        pass

# TODO Rename this here and in `download`
def _extracted_from_download_10(filename, r):
    remove_file_name = filename.split('/')[-1]
    print(remove_file_name)
    dir_path = filename.replace(f'/{remove_file_name}' , '').replace('//' , '\\')
    os.makedirs(dir_path , exist_ok=True)
    print(dir_path)
    __write(filename , r.content)