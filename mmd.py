from Downloaders.pururindl import pururindl
from Downloaders.hentaiserdl import hentaiserdl
from time import sleep
# please don't change stuff unless you know what you're doing.
version = 1.0


def main():
    print('~Mass Manga Downloader~ Version ' + str(version))
    print('Select a Module')
    print('-- -- -- -- --')
    print('1 | Pururin (NSFW)')
    print('2 | Hentaiser (NSFW)')
    print('0 | ~Credits~')
    versel = input('>> ')
    ver = int(versel)
    if ver == 1:
        print('This Module Only Accepts Json Files, Continue?')
        entry = input('(y/n): ')
        if entry == 'y':
            pururindl()
        else:
            exit(1)
    elif ver == 2:
        print('This Module Only Accepts Txt Files, Continue?')
        entry = input('(y/n): ')
        if entry == 'y':
            hentaiserdl()
        else:
            exit(1)
    elif ver == 0:
        credits()
    else:
        print('Invalid Option Try Again.')
        sleep(3)
        main()

def credits():
    print('Made by Stefmmm')

if __name__ == '__main__':
    main()
