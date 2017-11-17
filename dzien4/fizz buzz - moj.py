# fizz buzz

#wydrukowac 1-100, jesli/3, to wypisac fizz, jesli/5 - Buzz


zakres = range (1, 101)

for liczba in zakres:
    if liczba % 3 == 0 and liczba % 5 ==0:
        print("FizzBuzz")
    elif liczba % 5 == 0:
        print('Buzz')
    elif liczba % 3 == 0:
        print("Fizz")
    else: print(liczba)