import random
import os

words_bank = ["table", "windows", "laptop", "screen", "python", "mobile", "mouse", "keyboard", "water", "country"]
spaces = ["-"]
letter_guessed  = []
lives = 6
# Create Clear Function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Create function to peck a random Word
def peck_word(words):
    return random.choice(words)

# Create function to generate empty spaces
def empty_spaces(choose_word):
    return spaces * len(choose_word)

# Create function to check the use guess
def guess_letter(user_guess, choose_word):
    letter_index = choose_word.index(user_guess)
    return letter_index

# Create function to replace user input  with empty spaces
def replace_space(letter_index, answer, user_guess):
    answer[letter_index] = user_guess
    return answer

# game logic:
word_to_guess = peck_word(words_bank)
print(word_to_guess)
word_as_spaces = empty_spaces(word_to_guess)

while "-" in word_as_spaces:

    print("".join(word_as_spaces))
    guess = input("Guess a letter: ").lower()
    if lives > 0 :
        if guess in word_to_guess:
            index = guess_letter(guess, word_to_guess)
            replace_space(index, word_as_spaces, guess)

        elif guess in letter_guessed:
            print("You already guessed this letter, Try another one")
            print(f"You have {lives} remaining")

        else:
            lives -= 1
            letter_guessed.append(guess)
            print(f"You have {lives} remaining")
    else:
        break

if lives > 0:
    print("You win")
else:
    print("You lose")

