# wypisz liczby 1-10 poza liczbami podzielonymi na 7

for x in range(100):
    if x % 7 == 0:
        continue
    else:
        print(x)