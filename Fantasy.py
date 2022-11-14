inwentarz = {'sznur': 1, 'monety': 3, 'pochodnia': 5, 'miecz': 1}

def pokazInwentarz():
    for key, value in inwentarz.items():
        print(key, ':', value)
def sumaInwentarza():
    total = 0
    for value in inwentarz.values():
        total += value
    return total

pokazInwentarz()

print('Wszystkich przedmiotów: ',sumaInwentarza())