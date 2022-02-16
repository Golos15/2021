def dajOcene(ocena):
    try:
        ocena = int(ocena)
    except:
        return "Wpisz liczbę!"
    finally:
        if ocena >= 101:
            return "Za wysoko!"
        elif ocena > 90:
            return "Uczeń dostał 5."
        elif ocena >= 80:
            return "Uczeń dostał 4."
        elif ocena >= 70:
            return "Uczeń dostał 3."
        elif ocena >= 50:
            return "Uczeń dostał 2."
        elif ocena >= 0:
            return "Uczeń dostał 1."
        else:
            return "Nie kłam!"


ocena = input("Ile punktów dostał uczeń?")
print(dajOcene(ocena))
