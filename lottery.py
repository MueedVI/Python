# LOTTERY

from random import randint

print("\n" + "=" * 66)
print("🎰  WHO WANTS TO WIN A LOTTERY?  🎰".center(66))
print("=" * 66 + "\n")

while True:
    try:
        attempts = int(input("How many attempts do you want to yourself: "))
        if attempts <= 0:
            print("Forgot to enter a positive number?🤔")
            continue
        break
    except ValueError:
        print("\n" + "-" * 66)
        print("Oops!😬 You may want to enter a number instead!")
        print("-" * 66 + "\n")

for attempt in range(1, attempts + 1):

    while True:
        try:
            lottery = randint(1, 250)
            user_attempt = int(
                input(
                    f"Attempt: {attempt}/{attempts} - Please guess a number between 1 and 250: "
                )
            )
            break
        except ValueError:
            print("\n" + "-" * 66)
            print("Oops!😬 That's not a number. Try again!")
            print("-" * 66 + "\n")

    if user_attempt == lottery:
        print("\n" + "🎉" * 33)
        print("HEY!!! You have just won 10,000$! 💰")
        print("🎉" * 33 + "\n")
        break

    else:
        if attempt < attempts:
            print("-" * 66)
            print(f"❌ Try again! The lottery number was {lottery}".center(66))
            print("-" * 66)
        else:
            print("\n" + "=" * 66)
            print(f"GAME OVER!💀 The lottery number was {lottery}".center(66))
            print("=" * 66 + "\n")

if user_attempt == lottery:
    print(f"You guessed it in {attempt} attempt(s). Nice!")
elif user_attempt != lottery:
    print(f"You used {attempts} attempt(s). Better luck next time!😏\n")
