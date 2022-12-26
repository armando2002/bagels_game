






import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.

    
    I'm thinking of a {} digit number with no repeated digits.
    Try to guess what the number is. Here are some clues:
    When I say:     That Means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.
    
    For example, if the secret number was 258 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        # store the number
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keep looking until a guess is found
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))

        # ask if player wants to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # create a list of digits 0 to 9.
    random.shuffle(numbers)

    # get the first NUM_DIGITS in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # a correct digit is in the incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # no correct digits
    else:
        # stort the clues into alphabetical order so their original order
        # does't give information away
        clues.sort()
        # mage a single string with the list of string clues
        return ' '.join(clues)


# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()