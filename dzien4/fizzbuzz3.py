zakres = range(1,101)

for liczba in zakres:
    if liczba % 3 == 0:
        print('Fizz', end= '')
    if liczba % 5 ==0:
        print("Buzz", end= '')
    if liczba % 3 != 0 and liczba % 5 != 0:
        print(liczba, end="")
    print ('\n', end='')
