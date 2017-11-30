from zajeciapy4.dzien9.samochodm import Samochod
from zajeciapy4.dzien9.silnikm import Silnik

silnik_v4 = Silnik(1998, 'benzyna')
print(silnik_v4.paliwo)

beemka = Samochod('BMW', "3")
beemka.silnik = silnik_v4



print(beemka)
print(beemka.silnik)
print(beemka.marka)