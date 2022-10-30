def tax (income):
    incomeCap = {100000:0.40,30000:0.25,10000:0.10}
    total = 0
    for value in incomeCap:
        if income >= value:
            taxPercent = incomeCap.get(value)
            sumToTaxFrom = income - value
            total += (sumToTaxFrom * taxPercent)
            income -= sumToTaxFrom
            break
    return int(total)

income = float(input("Wpisz kwotę do opodatkowania: "))
print("Twój podatek wynosi: " + str((tax(income))))
