#daj liste zawierajaca unikalne wartosci

lista_a = [10,20,332,23,234,10,435,35,234,20, 4938, 435]

unikalne = []

for element in lista_a:
    if element not in unikalne:
        unikalne.append(element)

posortowane = sorted(unikalne)
print(unikalne)
print(posortowane)

# print(sorted(unikalne))


