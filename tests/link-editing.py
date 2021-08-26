def create_link(date:int , year:int , month:str) -> str:
    # https://archives.nseindia.com/content/historical/EQUITIES/2021/AUG/cm25AUG2021bhav.csv.zip
    # https://archives.nseindia.com/content/historical/EQUITIES/2015/AUG/cm10AUG2015bhav.csv.zip
    # https://archives.nseindia.com/content/historical/EQUITIES/2020/AUG/cm1AUG2020bhav.csv.zip
    link=f'https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{date}{month}{year}bhav.csv.zip'
    print(link)
    return link

create_link(2 , 2021 , 'aug')