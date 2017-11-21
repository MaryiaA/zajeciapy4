sciezka = 'tekst.txt'

tekst = """to jest tekst.
to jest kolejna linijka
i jeszcze jedna"""

with open(sciezka, 'r+') as plik:
    print(plik.tell())
    #plik.write(tekst)
    plik.seek(0)
    plik.read()
