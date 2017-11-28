file_path = 'dane.txt'

#try:
#   with open(file_path) as file:
#        print(file.read())

#except FileNotFoundError:
#    print('podany plik nie istnieje')

#except Exception as e:
#    print('uups, nastapil blad', e)

#finally:
#    print('ta funkcja zawsze sie wykona')


try:
    print('to jest blok try')
    raise ValueError('Sam tworze wyjatek! typ ValueError')
except ValueError as e:
    print('Zlapalem wyjatek', e)

finally:
    print('zawsze sie wykonam')