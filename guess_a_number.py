from random import randint
counter = 0

generate_number = randint(1, 100)
print(generate_number)
while True:
    while True:
        player_number = input("Guess the number from 1 to 100: ")
        try:
            number = int(player_number)
            if 1 <= number <= 100:
                break
            else:
                print("Enter valid number from 1 to 100")
        except ValueError:
            print("Enter valid an integer number (1 - 100)")

    counter += 1
    if int(player_number) < generate_number:
        print("Too Low!")
    elif int(player_number) > generate_number:
        print("Too High!")
    else:
        if counter == 1:
            print(f"You guessed it in {counter} try!")
        else:
            print(f"You guessed it in {counter} tries!")
        break
