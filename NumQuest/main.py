import random

NUM_DIGITS = 3 # Constant for number of digits generated to guess
MAX_GUESSES = 10 # Constant for max number of attempts

def get_secret_code(): # Function to generate a secret code 🤫
    """Generate a secret NUM_DIGITS number with unique digits."""
    digits = random.sample(range(10), NUM_DIGITS)  # Get unique digits
    secret_code = ''.join(map(str, digits))  # Convert to string
    return secret_code

def get_clue(guess, secret_code): # Function to return clues based on the guess
    if guess == secret_code: # If the guess is right
        return "Congratulations! You have completed the quest 🎉"
    
    clues = [] # List to keep track of clues
    
    for i in range(NUM_DIGITS):
        if guess[i] == secret_code[i]:
            clues.append("🟢") # Guessed digit in correct position
        elif guess[i] in secret_code:
            clues.append("🔵") # Guessed digit exists but in incorrect position
    
    if not clues:
        return "🔴" * NUM_DIGITS # No Correct Digits
    else:
        return ''.join(clues)
    
def start_quest():
    """Main logic for NumQuest"""
    
    print("Welcome to NumQuest, the Number Guessing Game!")
    
    secret_code = get_secret_code()  # Generate the secret code
    
    print(f"I'm thinking of a {NUM_DIGITS}-digit number.")
    print("You have 10 tries to guess it.")
    
    for attempt in range(1, MAX_GUESSES + 1):
        guess = input(f"Attempt {attempt}: Enter your guess: ")
        
        if len(guess) != NUM_DIGITS or not guess.isdigit(): # Validating the input
            print(f"Invalid! Please enter a {NUM_DIGITS}-digit number.")
            continue
        
        clue = get_clue(guess, secret_code)
        print(clue)
        
        if guess == secret_code:
            break
    else:
        print(f"Quest Failed! Max attempts reached.. The secret code was {secret_code}.")

            
if __name__ == "__main__":
    start_quest() 
    