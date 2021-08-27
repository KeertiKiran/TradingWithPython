def name(link:str):
    """Will name a file based on the link given"""
    name = link.split('/')[-1]
    return name