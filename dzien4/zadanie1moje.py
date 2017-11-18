#obl. ilosc parzystych inieparzystych w zakresie

zakres = range(23746)


parzyste = 0
nieparzyste = 0


for i in zakres:
    print(i%2 == 0)