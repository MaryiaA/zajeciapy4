sciezka = "tekst.txt"

with open(sciezka) as plik:
    linijka = plik.readline()
    pozycja = plik.tell()
    print(f"kursor znajduje sie w pozycji {pozycja}")

    print(linijka, end = '')
    print(plik.readline())
    print('Kolejna linijka')
    print(plik.read())


plik.seek(3)