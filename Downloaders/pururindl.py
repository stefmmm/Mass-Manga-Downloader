import requests
import json
import os
import zipfile
import time
import shutil
import re

config = open('Downloaders/Configs/pururinconfig.json', 'r')
readconf = json.load(config)
DefaultFile = readconf['conf']['Default-File']
LibraryLoc = readconf['conf']['Library-Location']


def pururindl():
    if os.path.exists('Downloaders/Pururin-Temp'):
        shutil.rmtree('Downloaders/Pururin-Temp')
    count = 0
    errors = 0
    dupes = 0
    fj = open(DefaultFile)
    data = fj.readlines()
    for i in data:
        count += 1
        expr = re.compile("[0-9]+")
        lol = re.search(expr, i)
        theid = lol[0]

        url = "https://pururin.to/api/gallery"
        data = {
            "id": theid,
        }
        headers = {
            "Content-type": "application/json",
        }
        req = requests.post(url=url, data=json.dumps(data), headers=headers)
        data = json.loads(req.text)
        if data['status'] == False:
            print(theid + ' = !!404!!')
            errors += 1
            continue

        galid = data['results']['id']
        mangadir = data['results']['full_title']
        totalpages = data['results']['total_pages']
        thename = mangadir.replace("\\", "-").replace("/", "-").replace(":", "").replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
        archive_name = f'{thename}.zip'
        fj.close()
        print(theid + ' = ' + archive_name)
        os.makedirs(os.path.dirname(LibraryLoc), exist_ok=True)
        if not os.path.exists(LibraryLoc + archive_name):
            createzip = zipfile.ZipFile(LibraryLoc + archive_name, 'w')
            with createzip:

                for x in range(1, totalpages + 1):
                    createzip.close()
                    filenum = format(x, '03')
                    fileurl = 'https://cdn.pururin.to/assets/images/data/' + str(galid) + f'/{x}.jpg'

                    getfile = requests.get(fileurl, allow_redirects=False)
                    os.makedirs(os.path.dirname('Downloaders/Pururin-Temp/'), exist_ok=True)
                    file_name = archive_name
                    f = open(f'Downloaders/Pururin-Temp/{filenum}.jpg', 'wb')

                    f.write(getfile.content)
                    f.close()
                    with zipfile.ZipFile(LibraryLoc + file_name, 'a') as file:
                        file.write(f'Downloaders/Pururin-Temp/{filenum}.jpg', f'{filenum}.jpg')
                    with zipfile.ZipFile(LibraryLoc + file_name, 'r') as file:
                        print(file.namelist())
        else:
            print('ZIP Already Exists, Skipping...')
            dupes += 1

        time.sleep(0.5)
        if os.path.exists('Downloaders/Pururin-Temp'):
            shutil.rmtree('Downloaders/Pururin-Temp')
        else:
            continue
    print('Total Count:' + str(count))
    print('Errors:' + str(errors))
    print('Possible Dupes:' + str(dupes))


if __name__ == '__main__':
    pururindl()
