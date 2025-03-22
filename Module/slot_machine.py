import random

def play():
    symbols = ['🍒', '🍇', '🍉', '7️⃣']
    result1 = random.choice(symbols)
    result2 = random.choice(symbols)
    result3 = random.choice(symbols)
    print(f"{result1}|{result2}|{result3}")
    
    if result1 == '7️⃣' and result2 == '7️⃣' and result3 == '7️⃣':
        print('Jackpot!💰')
    return

# Main game loop
playing = True
while playing:
    print("\n--- SLOT MACHINE ---")
    play()
    
    # Ask player if they want to continue
    continue_playing = input("Play again? (Y/N): ")
    if continue_playing.upper() != 'Y':
        playing = False
        print("Thanks for playing!")
