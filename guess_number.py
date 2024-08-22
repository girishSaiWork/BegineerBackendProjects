"""
Number Guessing Game

Description:
This is a simple command-line application that allows users to play a number guessing game. 
The program randomly selects a number within a specified range, and the user has to guess 
the number within a limited number of chances. The game provides hints to assist the user 
in making their guesses.

Author: Girish Sai
Reference URL: https://roadmap.sh/projects/number-guessing-game
Github URL: https://github.com/girishSaiWork/BegineerPythonProjects
"""

import random
import time

# Leaderboard to keep track of high scores
leaderboard = []

def get_difficulty_level():
    """
    Get the difficulty level for the game.

    This function prompts the user to select a difficulty level for the number guessing game.
    The user can choose from three levels: Easy, Medium, and Hard, each providing a different
    number of chances to guess the number. The function validates the user's input and returns
    the number of chances corresponding to the selected difficulty level.

    Returns:
        int: The number of chances based on the selected difficulty level.
    """
    while True:
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")

        choice = input("Enter your choice: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        elif choice == '3':
            return 3
        else:
            print("Invalid choice. Please select a valid difficulty level.")

def get_number_range():
    """
    Get the range of numbers for the guessing game.

    This function prompts the user to enter the lower and upper bounds for the range of numbers
    from which the random number will be selected. It provides a default range of 1 to 100,
    but allows the user to customize the range according to their preference.

    Returns:
        tuple: A tuple containing the lower and upper bounds of the range as integers.
    """
    print("\nYou can choose the range of numbers to guess from.")
    print("Default is between 1 and 100.")
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    return low, high

def provide_hint(number, guess, chances):
    
    """
    Provide a hint to the player based on their guess and remaining chances.

    This function evaluates the player's guess in relation to the actual number and the number of chances left.
    It provides hints based on whether the number is even or odd, or how close the guess is to the actual number.
    The hints vary depending on whether the remaining chances are even or odd.

    Args:
        number (int): The actual number that the player is trying to guess.
        guess (int): The player's most recent guess.
        chances (int): The number of chances remaining for the player.

    Returns:
        None: This function prints hints directly to the console.
    """

    if chances % 2 == 0:
        if number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    else:
        diff = abs(number - guess)
        if diff <= 10:
            print("Hint: You're very close!")
        elif diff <= 20:
            print("Hint: You're somewhat close.")
        else:
            print("Hint: You're far off.")

def play_game():
    """
    Play the Number Guessing Game.

    This function initiates the number guessing game, allowing the player to select a range of numbers
    and a difficulty level that determines the number of chances they have to guess the correct number.
    The player is prompted to enter their guesses, and hints are provided based on their proximity to the
    actual number. The game continues until the player either guesses the number correctly or runs out of chances.

    Returns:
        int or None: The number of attempts taken to guess the number if successful, or None if the player
        runs out of chances.
    """
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    low, high = get_number_range()
    number = random.randint(low, high)
    chances = get_difficulty_level()

    print(f"\nGreat! You have selected a difficulty level with {chances} chances.")
    print("Let's start the game!")
    print("-" * 40)

    start_time = time.time()
    attempts = 0

    while chances > 0:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == number:
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print(f"\n🎉 Congratulations! You guessed the correct number in {attempts} attempts and {duration} seconds.")
            return attempts

        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")

        chances -= 1
        print(f"You have {chances} chances left.")

        if chances > 0:
            provide_hint(number, guess, chances)

    print(f"\n❌ Sorry, you've run out of chances. The correct number was {number}.")
    return None

def update_leaderboard(attempts, player_name):
    """
    Update the leaderboard with the player's name and the number of attempts taken to guess the number.

    This function takes the number of attempts and the player's name as input, appends the player's score
    to the leaderboard, and sorts the leaderboard based on the number of attempts in ascending order. 
    This allows for easy tracking of high scores and encourages competition among players.

    Args:
        attempts (int): The number of attempts taken by the player to guess the number.
        player_name (str): The name of the player who participated in the game.
    Returns:
        None: This function modifies the leaderboard in place and does not return any value.
    """
    leaderboard.append((player_name, attempts))
    leaderboard.sort(key=lambda x: x[1])

def show_leaderboard():
    def show_leaderboard():
        """
        Display the current leaderboard of players and their scores.

        This function prints the leaderboard, which includes the names of players and the number of attempts they took
        to guess the number. The leaderboard is sorted in ascending order based on the number of attempts, allowing players
        to see their ranking and encouraging competition. If there are no scores yet, a message indicating this is displayed.

        Returns:
            None: This function does not return any value; it only prints the leaderboard to the console.
        """

    print("\n🏆 Leaderboard 🏆")
    if not leaderboard:
        print("No high scores yet!")
    else:
        for rank, (name, score) in enumerate(leaderboard, start=1):
            print(f"{rank}. {name} - {score} attempts")

def main():
    """
    Main function to run the Number Guessing Game.

    This function serves as the entry point for the game, displaying a welcome message,
    prompting the player for their name, and managing the game loop. It calls the play_game()
    function to start the game, updates the leaderboard with the player's score, and displays
    the current leaderboard after each game. The player is given the option to play again,
    and the game continues until the player chooses to exit.

    Returns:
        None: This function does not return any value; it only controls the game flow.
    """
    while True:
        print("=" * 40)
        print("🎮 Welcome to the Ultimate Number Guessing Game! 🎮")
        print("=" * 40)

        player_name = input("\nEnter your name: ").strip()

        attempts = play_game()

        if attempts is not None:
            update_leaderboard(attempts, player_name)
            print(f"\nNew High Score! {player_name} guessed the number in {attempts} attempts.")
        
        show_leaderboard()

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThank you for playing the Number Guessing Game! Goodbye!")
            break

if __name__ == "__main__":
    main()