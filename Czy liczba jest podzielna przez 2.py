def czyjest_podzielna(n):
    if n % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        n = float(input("Wpisz jakąś liczbę:"))
        break
    except ValueError:
        print("To nie jest liczba!")


if czyjest_podzielna(n) == True:
    print("Podana liczba jest podzielna.")
else:
    print("Podana liczba jest niepodzielna.")
