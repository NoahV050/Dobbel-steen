import random

score = 0

while True:
    input("Druk op Enter om te gooien...")
    worp = random.randint(1, 6)
    print(f"Je gooide: {worp}")
    score += worp
    print(f"Totaalscore: {score}\n")
