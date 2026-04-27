import random

def play_card_game():
    # 1. Define ranks and their values
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = {rank: i + 2 for i, rank in enumerate(ranks)}
    
    # 2. Create a full deck (52 cards) and randomly choose 8 unique cards
    deck = [rank for rank in ranks for _ in range(4)]
    selection = random.sample(deck, 8)
    
    score = 0
    current_card = selection[0]
    
    print("Welcome to the Card Game!")
    print(f"Initial Card: {current_card} | Starting Score: {score}")
    
    # Iterate through the remaining 7 cards
    for i in range(1, 8):
        next_card = selection[i]
        
        # 3. Get user prediction
        prediction = ""
        while prediction not in ['higher', 'lower']:
            prediction = input(f"\nCurrent card is {current_card}. Will the next be 'higher' or 'lower'? ").lower().strip()
            
        print(f"Next card revealed: {next_card}")
        
        # 4. Scoring Logic
        # Per instructions: same value counts as incorrect
        if values[next_card] > values[current_card] and prediction == 'higher':
            print("Correct! You earned 20 points.")
            score += 20
        elif values[next_card] < values[current_card] and prediction == 'lower':
            print("Correct! You earned 20 points.")
            score += 20
        else:
            print("Incorrect! You lost 15 points.")
            score -= 15
            
        # Move to next card
        current_card = next_card
        print(f"Current Score: {score}")

    print("\n" + "="*30)
    print(f"GAME OVER! Final Score: {score}")
    print("="*30)

# Run the game
if __name__ == "__main__":
    play_card_game()