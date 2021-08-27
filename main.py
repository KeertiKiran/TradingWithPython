from download import *
from getlink import *
from naming import *

def multi_get(from_date, to_date):
    pass

def get(date , month , year):
    file_link = create_link(date=date , month=month , year=year)
    file_name = name(file_link)

download(url=create_link(26 , 12 , year=2017) , filename='o.zip')