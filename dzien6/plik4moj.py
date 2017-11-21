sciezka = 'tekst.txt'

with open(sciezka, 'a') as plik:
    print(plik.tell())

    plik.seek(0)

    plik.write('Moja kolejna linijka')

