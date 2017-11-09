# po podaniu nazwy m-ca ilosc dni

miesiac = input("podaj nazwe miesiaca: ")

if miesiac == "kwiecien" or miesiac == "czerwiec" or miesiac == "wrzesien" or miesiac == 'listopad':
    print(f"Miesiac {miesiac} ma 30 dni")
elif miesiac == 'luty':
    print("Luty ma 28 lub 29 dni")
else:
    print(f'miesiac {miesiac} ma 31 dni')
