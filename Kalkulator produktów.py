def sprawdz():
    calosc = 0
    licznik = 0
    wiecejProduktow = True
    while wiecejProduktow:
        cena = float(input('Wpisz cenę produktu (0 kiedy skończysz): '))
        if cena < 0:
            print("Nie ma ujemnych cen!")
            continue
        elif cena != 0:
            licznik = licznik + 1
            calosc = calosc + cena
            print('Suma: PLN', calosc)          
        else:
            wiecejProduktow = False
    srednia = calosc / licznik
    print('Wszystkie produkty:', licznik)
    print('Suma: PLN', calosc)
    print('Średnia cena produktu: PLN', srednia)

sprawdz()
