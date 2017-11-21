sciezka = 'tekst.txt'

tekst = 'to nowa linijka, ktora stworzyl python'

with open(sciezka, 'r+') as plik:
    plik.read()

    pozycja = plik.tell()
    plik.seek(pozycja - 1)

    ostatni_znak = plik.read()
    print(ostatni_znak)

    if ostatni_znak != '\n':
        plik.write('\n' + tekst + '\n')
    else:
        plik.write(tekst + '\n')