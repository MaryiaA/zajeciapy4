nazwisko = input('Podaj nazwisko:\n ')

# print(type(nazwisko))

#usunac whitespace z pocztku i konca
nazwisko = nazwisko.strip()

#jesli w stringu sa cyfry, napisac komunikat
# i przerwac program
if not nazwisko.isalpha():
    print('Musza byc tylko litery')
    exit()




#zmienic wszystkie litery na duze
naz_czyste = nazwisko.upper()


...
print(naz_czyste)
if nazwisko [-1] == 'A':
    print('chyba jestes kobieta')

elif nazwisko.endswith ('ski'):
    print('chyba jestes mieszczyzna')

if nazwisko.isupper():
    print('chyba jestes zlosliwa ')
...



print('koniec progamu')