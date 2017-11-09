# oblicz czy rok jest przestepny

# podzielny przez 4, nie podzielny przez 100 podzielny przez 400


rok = input('Podaj rok: ')

rok = int(rok)

if rok % 400 == 0:
    print(f"Rok {rok} jest przestepny.")

if rok % 4 == 0 and rok % 100 != 0:
    print(f"Rok {rok} jest przestepny.")
else:
    print("Rok{rok} nie jest przestepny")