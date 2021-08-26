import datetime as dt
from threading import Thread

global black_listed_days
global months

black_listed_days = [
    'SAT',
    'SUN'
    ]

months = {
    1:'JAN',
    2:'FEB',
    3:'MAR',
    4:'APR',
    5:'MAY',
    6:'JUN',
    7:'JUL',
    8:'AUG',
    9:'SEP',
    10:'OCT',
    11:'NOV',
    12:'DEC',
    }

def create_download_link(date:int, month:str , year:int) -> str:
    link=f'https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month.upper()}/cm{date}{month.upper()}{year}bhav.csv.zip'
    print(link)
    return link

def run(func) -> None:
    t = Thread(target=func)
    t.start()

def create_link(date:int , month:int , year:int , console_output:bool=True) -> str:
    """returns a link for you to download from nseindia.com:\n\t
    IT WILL NOT DOWNLOAD IT!"""
    try:
        if (dt.date(year,month,date).strftime('%a')).upper() in black_listed_days:
            day= (dt.date(year,month,date).strftime('%A'))
            print(f'error: The date given refers to a week-end ( {date}-{month}-{year} is a {day} )')
        else:

            month = months[month]
            return run(func=lambda:create_download_link(date , month , year))
            if console_output == True:
                print(month)
            
    except ValueError:
        print(f'error: {month} is not a valid month number')
    except IndexError:
        print(f'error: {month} is not a valid month number')