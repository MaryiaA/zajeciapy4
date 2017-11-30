from zajeciapy4.dzien9.monitorm import Monitor

monitor1 = Monitor('Asus', 24)
monitor1.wlacz()

monitor2 = Monitor('Samsung', 27, '16:10')

print(monitor1.producent)
print(monitor1.przekatna)
print(monitor1.proporcje)
print(monitor1.kolor)
print(monitor1.wlaczony)

print('-------------------')
print(monitor2.producent)
print(monitor2.przekatna)
print(monitor2.proporcje)
print(monitor2.kolor)
print(monitor2.wlaczony)