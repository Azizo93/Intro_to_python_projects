secret_number = 5
guesses = 3
max_guesses = 0

while guesses > max_guesses:
    guess = int(input("Guess the secret number?: "))
    guesses -= 1
    print (f'Guesses remaining: {guesses}')
    if guess == secret_number:
        print("You guessed it!")
        break
else:
    print("GAME OVER!")








