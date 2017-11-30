class Monitor(object):
    '''monitor komputerowy'''
    def __init__(self, prod, przek, proporcje='16:9'):
        '''tworzy instancje objektu typy monitor
        :param prod: str - producent
        :param przek: int - przekatna ekranu w calach
        :param proporcje: str - proporcje ekranu, defaultowo 16:9
        '''
        self.producent = prod
        self.przekatna = przek
        self.kolor = None
        self.proporcje = proporcje
        self.wlaczony = False


    def wlacz(self):
        if not self.wlaczony:
            self.wlaczony = True
            print(f'Monitor {self.producent} zostal wlaczany')

    def wylacz(self):
        if self.wlaczony:
            self.wlaczony = False
            print(f'Monitor {self.producent} jest wylaczany')
        else:
            print('juz jest wylaczany')

    def __str__(self):
        return f'Monitor producent: {self.producent}\n' \
               f'        przekatna: {self.przekatna}\n' \
               f'        proporcje: {self.proporcje}\n' \
