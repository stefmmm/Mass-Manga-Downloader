import requests
import json
import zipfile
import os
import time
import shutil

config = open('Downloaders/Configs/hentaiserconfig.json', 'r')
readconf = json.load(config)
headers = readconf['headers']
imgheaders = readconf['imgheaders']
img2headers = readconf['img2headers']
DefaultFile = readconf['conf']['Default-File']

def hentaiserdl():

    failcount = 0
    if os.path.exists('Downloaders/Hentaiser-Temp/'):
        shutil.rmtree('Downloaders/Hentaiser-Temp/')
    with open(DefaultFile) as fileIn:
        for line in fileIn.readlines():
            trueline = line.replace("\n", "")
            mangaurl = 'https://api.hentaiser.com/1.2/book/' + trueline
            urlreq = requests.get(url=mangaurl, headers=headers, allow_redirects=False)
            mdata = json.loads(urlreq.text)
            manganame = mdata['title']
            archive_name = manganame + '.zip'
            newarc = archive_name.replace("\\", "-").replace("/", "-").replace(":", "").replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')

            # image grabber
            img = 'https://api.hentaiser.com/1.2/book/images/' + trueline
            req = requests.get(url=img, headers=headers, allow_redirects=False)
            if req.status_code != 200:
                print('welp something went wrong here')
                failcount += 1
                continue
            data = json.loads(req.text)
            num = 0
            os.makedirs(os.path.dirname('Library/Hentaiser/'), exist_ok=True)
            os.makedirs(os.path.dirname('Downloaders/Hentaiser-Temp/'), exist_ok=True)

            if not os.path.exists('Library/Hentaiser/' + newarc):
                createzip = zipfile.ZipFile('Library/Hentaiser/' + newarc, 'w')
                with createzip:
                    for images in data:

                        createzip.close()
                        num += 1
                        realnum = format(num, '03')
                        imgurl = images['url']
                        hentaiurl = 'https://media.hentaiser.com' + imgurl
                        reqimg = requests.get(url=hentaiurl, headers=imgheaders, allow_redirects=False)
                        if reqimg.status_code == 302:
                            hentaiurl2 = 'https://media2.hentaiser.com' + imgurl
                            reqimg = requests.get(url=hentaiurl2, headers=img2headers, allow_redirects=False)

                        print(reqimg.url)
                        print(newarc + ' PAGE: ' + realnum)
                        f = open(f'Downloaders/Hentaiser-Temp/{realnum}.jpg', 'wb')
                        f.write(reqimg.content)
                        f.close()
                        with zipfile.ZipFile('Library/Hentaiser/' + newarc, 'a') as file:
                            file.write(f'Downloaders/Hentaiser-Temp/{realnum}.jpg', f'{realnum}.jpg')
                time.sleep(0.5)

                if os.path.exists('Downloaders/Hentaiser-Temp/'):
                    shutil.rmtree('Downloaders/Hentaiser-Temp/')
            else:
                print('ZIP Already Exists, Skipping...')
    print('Stuff that failed: ' + str(failcount))


if __name__ == '__main__':
    hentaiserdl()
