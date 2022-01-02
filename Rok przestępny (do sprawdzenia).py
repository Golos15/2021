def czyPrzestepny(rok):
    if rok % 4 == 0 or rok % 100 == 0 and rok // 400 == 0:
        return True
    else:
        return False
    
rok = int(input("Dawaj jakąś liczbę"))
print(czyPrzestepny(rok))
