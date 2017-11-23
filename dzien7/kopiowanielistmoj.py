nabial = ['jajka', 'mleko', 'twarog']
chemia = ['domestos', 'plyn do naczyn', 'proszek do prania']


zakupy_listopad = [nabial, chemia]

zakupy_grudzien = zakupy_listopad.copy()
zakupy_styczen = zakupy_listopad[:]

print(f'zakupy listopad:{zakupy_listopad}')
print(f'zakupy listopad:{zakupy_grudzien}')
print(f'zakupy listopad:{zakupy_styczen}')

zakupy_grudzien[0].append('maka')