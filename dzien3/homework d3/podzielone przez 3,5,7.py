# 3. czy liczba jest podzielna przez 3, 5, 7

cyfra = input("Podaj_cyfre")
cyfra = int(cyfra)

denominator = input('Podzielone przez')

if cyfra % 3 == 0:
    print("podzielona przez 3")
else:
    print("nie podzielona przez 3")
if cyfra % 5 == 0:
    print("podzielona przez 5")
else:
    print("nie podzielona przez 5")
if cyfra % 7 == 0:
    print("podzielona przez 7")
else:
    print("nie podzielona przez 7")