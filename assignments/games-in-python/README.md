
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python that exercises string manipulation, loops, conditionals, and user input. Implement the game loop, guess handling, and clear win/lose outcomes.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a console-based Hangman game that randomly selects a secret word and lets a player guess letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly choose a secret word from an internal list of at least 10 words
- Display current progress after each guess in the `_ _ a _ _` format (spaces between placeholders)
- Accept single-letter guesses and ignore or warn about repeated guesses
- Track incorrect guesses and show remaining attempts (minimum 6 attempts)
- End the game with a clear win message when the word is guessed
- End the game with a clear lose message and reveal the secret word when attempts are exhausted
- Organize code using functions (for example: `choose_word()`, `display_progress()`, `process_guess()`)

### 🛠️ Optional Enhancements

#### Description
Add extra polish or features to improve playability and learning value.

#### Requirements
Completed program may include any of the following:

- Difficulty levels or a simple hint system
- Loading the word list from an external `words.txt` file
- ASCII-art hangman that updates with each wrong guess
- A scoring system and a replay option

## Example Play (short)

Player sees: `Word: _ _ _ _ _`
Player inputs: `a`
Program responds: `Nice! Word: _ a _ _ _ — Attempts left: 6`

Player inputs: `z`
Program responds: `Incorrect. Attempts left: 5`

When done, save your solution as `starter-code.py` in this folder and ensure it runs with `python3 starter-code.py`.

