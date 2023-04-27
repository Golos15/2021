def algorytm_Luhna(nr_nieruch):
    nr_nieruch = str(nr_nieruch)
    cyfry = [int(d) for d in nr_nieruch]

    suma1 = 0
    suma2 = 0

    for i, wartosc in enumerate(reversed(cyfry)):
        if i % 2 == 0:
            wartosc *= 2
            if len(str(wartosc)) > 1:
                for cyfra in str(wartosc):
                    suma1 += int(cyfra)
        else:
            suma1 += wartosc

    liczba_kontrolna = suma1 % 10
    print("Liczba kontrolna: " + str(liczba_kontrolna))

    cyfry.append(liczba_kontrolna)

    for i, wartosc in enumerate(reversed(cyfry)):
        if i % 2 == 0:
            wartosc *= 2
            if len(str(wartosc)) > 1:
                for cyfra in str(wartosc):
                    suma2 += int(cyfra)
        else:
            suma2 += wartosc
    if suma2 % 10:
        return True
    else:
        return False

if algorytm_Luhna(375069) == True:
    print("Jest okej")
else:
    print("Coś nie tak")
