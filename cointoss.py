from random import choice

while True:
    try:
        coin_rounds = int(input("How many rounds of coin toss do you want? "))
        break
    except ValueError:
        print("Oops! You may want to enter a number instead!")

heads = 0
tails = 0

header = f"{'Round':^10} | {'Head':^10} | {'Tail':^10}"
border = "-" * len(header)

print(border)
print(header)
print(border)

for cround in range(coin_rounds):
    coin = choice(["heads", "tails"])
    if coin == "heads":
        heads += 1
    elif coin == "tails":
        tails += 1
    print(f"{cround+1:^10} | {heads:^10} | {tails:^10}")
print(border)

print(f"Rounds: {cround+1} | Heads: {heads} | Tails: {tails}\n")

