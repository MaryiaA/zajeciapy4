def odwroc_string(zdanie):
    '''
    Zwraca odwrocony string. Jeski argument jet pustym. zwraca None
    :param zdanie:
    :return:
    '''
    if zdanie == '' or zdanie == None:
        return None
    return zdanie[::-1]



def main():
    imie = 'Ala'
    odwr_imie = odwroc_string(imie)
    spr_imie = imie[::1]
    if odwr_imie == reversed(imie):
        print(f'{imie} zostalo prawidlowo odwroceone na {odwr_imie}')
    else:
        print(f' Nieprawidlowo {spr_imie} != {odwr_imie}')


if __name__ == '__main__':
    main()