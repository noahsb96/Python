import random
from hangman_words import word_list
from hangman_art import stages, logo
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed = []

print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display.append("_")
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()
    guessed.append(guess)
    print(guessed)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print("That's the cream of the crop, bruthuuuurrr")
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print("That ain't it bruthuuuurr")
        if lives == 0:
            print("You couldn't crack it. I'll see you in the cage, bruthuuuur")
            break

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        print("You solved it bruthuuuurrrr")
    print(stages[lives])
