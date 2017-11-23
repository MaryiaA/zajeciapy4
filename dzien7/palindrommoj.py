
import dzien7.podfolder.odwracaczmoj


def czy_palindrom(wyraz):
    '''Sprawdz czy podany strin jest palindromem
    str ->bool '''

    wyraz = wyraz.upper()
    odwrocony = dzien7.podfolder.odwracaczmoj.odwroc_string(wyraz)

    if wyraz == odwrocony:
        return True
    else:
        return False

print(czy_palindrom("kajak"))