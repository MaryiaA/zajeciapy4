zakres = range (1, 101)

for liczba in zakres:
    if liczba % 15 == 0 :
        print("FizzBuzz")
    elif liczba % 5 == 0:
        print('Buzz')
    elif liczba % 3 == 0:
        print("Fizz")
    else: print(liczba)