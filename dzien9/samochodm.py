class Samochod(object):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.jdzie = None
        self.silnik = None

    def rusza(self):
        self.jedzie = True
        print(f'{self.marka} ruszyl')

    def zatrzymaj(self):
        self.jedzie = False
        print(f'{self.marka} zatrzymal sie')
