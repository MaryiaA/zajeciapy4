nieprawidlowe = False


while nieprawidlowe:
    nazwisko = input('Podaj nazwisko drukowanymi literami')

    if nazwisko.upper() == '0':
        print('Do widzenia.')
        quit()
        if nazwisko.isupper():
            nieprawidlowe = False
    elif nazwisko.isalpha():
        if nazwisko.isupper():
            nieprawidlowe = True


print('Gratulacje, jestes zarejestrowany')