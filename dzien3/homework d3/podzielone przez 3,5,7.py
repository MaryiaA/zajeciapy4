# 3. czy liczba jest podzielna przez 3, 5, 7

cyfra = input("Podaj_cyfre")
cyfra = int(cyfra)

denominator = input('Podzielone przez')
denominator = int(denominator)

if cyfra % denominator == 0:
    print(f"podzielona przez {denominator}")

else:
    print(f"nie podzielona przez {denominator}")
