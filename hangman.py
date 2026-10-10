import random

# Five predefined words
words = ["python", "coding", "computer", "program", "developer"]

word = random.choice(words)
guessed = []
attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong attempts left:", attempts)

    if "_" not in display:
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)
