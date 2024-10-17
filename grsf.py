import random

total_games = 3

print("Laipni lūdzam spēlē 'Uzmini numuru'!")
print(f"Varat spēlēt {total_games} reizes.")

for game in range(total_games):
    secret_number = random.randint(1, 100)
    attempts = 5

    print(f"\nSpēle {game + 1}: jums ir {attempts} mēģinājumi uzminēt skaitli no 1 līdz 100.")

    while attempts > 0:
        try:
            guess = int(input("Ievadiet savu numuru: "))
            
            if guess < 1:
                guess = 1
                print("Jūs ievadījāt skaitli, kas ir mazāks par 1. Tas tiek automātiski aizstāts ar 1.")
            elif guess > 100:
                guess = 100
                print("Jūs ievadījāt skaitli, kas ir lielāks par 100. Tas tiek automātiski aizstāts ar 100.")

            if guess == secret_number:
                print("Apsveicam! Jūs uzminējāt skaitli!")
                break
            elif abs(guess - secret_number) <= 5:
                if guess < secret_number:
                    print("Jūs esat tuvu risinājumam! Slēptais skaitlis ir nedaudz lielāks.")
                else:
                    print("Jūs esat tuvu risinājumam! Slēptais skaitlis ir nedaudz mazāks.")
            elif guess < secret_number:
                print("Slēptais skaitlis ir lielāks.")
            else:
                print("Slēptais skaitlis ir mazāks.")
            
            attempts -= 1
            print(f"Atlikuši mēģinājumi: {attempts}")

        except ValueError:
            print("Lūdzu, ievadiet derīgu numuru.")

    if attempts == 0:
        print(f"Jūs esat zaudējis. Slēptais numurs bija: {secret_number}")

    if game < total_games - 1:
        play_again = input(f"\nVai vēlaties spēlēt vēlreiz? (y/n): ").lower()
        if play_again != 'y':
            break

print("Spēle beigusies. Paldies par dalību!")
