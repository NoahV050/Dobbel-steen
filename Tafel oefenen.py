import random

tafel = int(input("Welke tafel wil je oefenen? (bijv. 3): "))

while True:
    getal = random.randint(1, 10)
    antwoord = input(f"Wat is {tafel} x {getal}? ")
    if antwoord == "stop":
        print("Gestopt met oefenen.")
        break
    if antwoord.isdigit() and int(antwoord) == tafel * getal:
        print("Goed!\n")
    else:
        print(f"Fout. Het juiste antwoord is {tafel * getal}.\n")

