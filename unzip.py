from zipfile import ZipFile

def extract(filepath , extract_to):
    with ZipFile(filepath, 'r') as zip:
    # printing all the contents of the zip file
        zip.printdir()
        print('Extracting all the files now...')
        zip.extractall(extract_to)
        print('Done!')