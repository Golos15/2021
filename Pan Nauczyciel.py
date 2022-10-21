def dajOcene(ocena):
    try:
        ocena = int(ocena)
        if ocena >= 101:
            return "Za wysoko!"
        elif ocena > 80:
            return "Uczeń dostał 5."
        elif ocena >= 70:
            return "Uczeń dostał 4."
        elif ocena >= 60:
            return "Uczeń dostał 3."
        elif ocena >= 40:
            return "Uczeń dostał 2."
        elif ocena >= 0:
            return "Uczeń dostał 1."
        else:
            return "Nie kłam!"
    except:
        return "Wpisz liczbę!"
        
ocena = input("Ile punktów dostał uczeń? ")
print(dajOcene(ocena))
