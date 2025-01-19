import random
import os

words_bank = ["table", "windows", "laptop", "screen", "python", "mobile", "mouse", "keyboard", "water", "country"]
spaces = ["-"]
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


# Create function to replace user input  with empty spaces

