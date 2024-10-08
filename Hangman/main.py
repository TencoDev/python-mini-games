import random
from wordlist import word_list

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def get_word(): # To fetch a word from list
    word = random.choice(word_list)
    return word.upper()

def play(word):
    tries = 6
    word_completion = "_" * len(word) # To display the length of word chosen as underscores
    guessed = False
    guessed_letters = []
    guessed_words = []
    print("Welcome to HANGMAN!! 💀")
    print("Will you be able to save a life by guessing the right word???")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("So.. what letter or word you think is here..? ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("🤨 You already guessed this letter", guess)
            elif guess not in word:
                print("Oops, INCORRECT!! BAHAHA 😈 ")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Oh.. your guess {guess} is correct and in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("🤨 You already guessed this aword", guess)
            elif guess != word:
                print("BAHAHAH wrong word")
                tries -= 1
                guessed_words.append(guessed_words)
                print(guessed_words)
            else:
                guessed= True
                word_completion = word
        else:
            print("🤨 Are you serious, it is an invalid guess")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("ARRRR! You guessed it and you saved a life.. enjoy while you can")
        print("\n")
    else:
        print("😈 Say Farewell, you ran out of tries.. the word is ", word)
        
def main():
    word = get_word()
    play(word)
    while input("You wanna bet again kid? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
    
    


    