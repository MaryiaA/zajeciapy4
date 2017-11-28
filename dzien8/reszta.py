#program wydajacy reszte

#zakupy - wartosc, place banknotem
# wydac z monetami o nominalach od 5 do 0,1
# jak najmniej monet wydac

monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

wartosc_zak = 11.30

banknot = 20


reszta = banknot - wartosc_zak

print(f'wydaj:{reszta}')

if reszta < 0:
    print('Za mala wartosc banknotu')
    quit()

elif reszta == 0:
    print('Bez reszty.')
    quit()

for moneta in  monety.keys():
    if reszta >= moneta:
        ilosc = reszta //moneta
        monety[moneta] = ilosc
        reszta = round(reszta - (moneta * ilosc), 2)
        print('tyle reszty jeszcze jeszcze jest:', reszta)

print('wydac:')
for moneta, ilosc in monety.items():
    print(f'moneta:{moneta:>4} - {ilosc:>4} sztuk')



