from sre_constants import SUCCESS
from download import *
from getlink import *
from naming import *
from unzip import *
from zipfile import ZipFile


# Defining things
global __none

desktop_path = str(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')).replace('\\' , '/')
__none = '$None$'
__output_dir = desktop_path.__add__('/py~outfile')

def extract(filepath , extract_to):
    with ZipFile(filepath, 'r') as zip:
    # printing all the contents of the zip file
        zip.printdir()
        print('Extracting all the files now...')
        try:
            zip.extractall(extract_to)
        except FileExistsError:
            pass
        
        print('Done!')


def multi_get(from_date:tuple, to_date):
    pass

def get(date:int, month:int, year:int , output_dir:str=__none) -> None:
    """Will download the file with the given date. and unzip in `output_dir`...\n
    if `output_dir` is not provided, then it will be in `~/desktop/py~outfile`"""
    
    file_link = create_link(date=date , month=month , year=year)
    if output_dir.replace('\\' , '/') !=__none:
        output_folder = output_dir.replace('\\' , '/')
    else:
        tmp = name(file_link).replace('.zip' , '')
        output_folder = __output_dir
        del tmp
    
    file_name = f'./cache/{name(file_link)}'

    download(url=create_link(date , month , year) , filename=file_name)
    extract(file_name , output_folder)

get(26 , 12 , 2017)