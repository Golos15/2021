def sprawdz():
    calosc = 0
    licznik = 0
    wiecejProduktow = True
    while wiecejProduktow:
        cenaTekst = input('Wpisz cenę produktu (Wpisz "koniec" kiedy skończysz): ')
        try:
            cenaLiczba = float(cenaTekst)
        except ValueError:
            if cenaTekst != "koniec":
                continue
            break
        if cenaLiczba < 0:
            print("Nie ma ujemnych cen!")
            continue
        elif cenaLiczba != 0:
            licznik = licznik + 1
            calosc = calosc + cenaLiczba
            print('Suma: PLN', calosc)          
        else:
            wiecejProduktow = False
    srednia = calosc / licznik
    print('Wszystkie produkty:', licznik)
    print('Suma: PLN', calosc)
    print('Średnia cena produktu: PLN', srednia)

sprawdz()
