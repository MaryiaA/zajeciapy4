from zajeciapy4.dzien9.monitorm import Monitor

monitor1 = Monitor("AOK", 19)

monitor1.przekatna = 'dwadziescia jeden'
print(f'Monitor1 {monitor1.producent} ma przekatna '
      f'{monitor1.przekatna} cali')

monitor1.kolor = 'czerwony'
print(monitor1.kolor)

monitor2 = Monitor("Asus", 24)
print(f'Monitor1 {monitor2.producent} ma przekatna '
      f'{monitor2.przekatna} cali')

print(monitor1)
print(monitor2)