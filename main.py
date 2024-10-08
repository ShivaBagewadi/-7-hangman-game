import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

# TODO-1 - Randomly choose a random word from the word_list and assign it to a variable called chosen_word. Then point it.
print(logo)
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
placeholder  =""

for position in range(word_length):
    placeholder = placeholder + "_"
print(placeholder)

# TODO-2 - Ask the user to guess the letter and assign their answer to a variable called guess. make guess
game_over = False
correct_letter = []

while not game_over:

    print(f"********************{lives}/6 LIVES LEFT********************")

    guess = input("guess the letter: ").lower()
    # print(guess)

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letter in the chosen_word. print "right" if it is,
    #  "wrong" if it is not.

    if guess in correct_letter:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display = display + guess
            correct_letter.append(letter)
            # print(display)
        elif letter in correct_letter:
            display += letter

        else:
            display += "_"
            # print(display)

    print(display)



    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. you loss a life.")


        if lives == 0:
            game_over = True

            print(f"********************IT WAS {chosen_word}! YOU LOSE********************")


    if "_" not in display:
        game_over = True
        print("********************YOU WIN********************")


    print(stages[lives])



