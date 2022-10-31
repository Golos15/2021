import random


def wez_wynik(player, computer):
    print("komputer: ", computer)
    print("gracz: ", player)
    gracz_idx = choices.index(player)
    komp_idx = choices.index(computer)

    if gracz_idx > komp_idx and abs(gracz_idx - komp_idx) == 1 or gracz_idx == 0 and komp_idx == 2:
        return "Wygrałeś!"
    elif gracz_idx == komp_idx:
        return "Remis!"
    else:
        return "Przegrałeś!"

zakonczyc_program = False

while not zakonczyc_program:
    choices = ["kamień","papier","nożyce"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("kamień, papier, czy nożyce?: ").lower()

    print(wez_wynik(player, computer))

    while True:
        jeszcze_raz = input("Chcesz zagrać jeszcze raz? (tak/nie): ").lower()
        if jeszcze_raz == "nie":
            zakonczyc_program = True
            break
        elif jeszcze_raz == "tak":
            break

print("Na razie!")

