otworz = open('C:/Users/golos/Desktop/fantastycznie.txt', 'r')

linie = []
licznik = 0

with otworz as f:
    linie = f.readlines()
    for wiersz in otworz:
        licznik += 1
        wartosci = wiersz.split()
        komunikat = 'W', wartosci[0], 'średnia temperatura wynosiła ', wartosci[1], 'stopni Celsjusza, a emisja CO2 wynosiła', wartosci[2], 'gigaton.'
        print(f'Linijka nr. {licznik}') + komunikat
