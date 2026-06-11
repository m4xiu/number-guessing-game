# Number Guessing Game

guess = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_guess = int(input('Enter your guess: '))
    guess_count += 1
    if user_guess == guess:
        print('You win!')
        break
else:
    print('Sorry, you failed!')