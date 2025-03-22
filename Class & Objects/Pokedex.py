# Gotta catch them all!
class Pokemon:
    def __init__(self, entry, name, height, category, weight, level, types, description, is_caught=False):
        self.entry = entry
        self.name = name
        self.height = height
        self.category = category
        self.weight = weight
        self.level = level
        self.types = types if isinstance(types, list) else [types]  # Ensure types is a list
        self.description = description
        self.is_caught = is_caught
        self.hp = level * 5  # Add some game mechanics
        self.moves = []  # Pokemon can learn moves
    
    def speak(self):
        print(f"{self.name}, {self.name}!")
    
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Height: {self.height} m")
        print(f"Category: {self.category} Pokémon")
        print(f"Weight: {self.weight} kg")
        print(f"Level: {self.level}")
        print(f"Types: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        print(f"HP: {self.hp}")
        
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"You have not caught {self.name} yet!")
    
    def level_up(self):
        self.level += 1
        self.hp = self.level * 5
        print(f"{self.name} leveled up to level {self.level}!")
        
    def learn_move(self, move):
        if len(self.moves) < 4:
            self.moves.append(move)
            print(f"{self.name} learned {move}!")
        else:
            print(f"{self.name} already knows 4 moves.")
            print("Current moves:", ", ".join(self.moves))
            replace = input("Replace a move? (yes/no): ")
            if replace.lower() == "yes":
                for i, known_move in enumerate(self.moves):
                    print(f"{i+1}. {known_move}")
                move_index = int(input("Replace which move? (1-4): ")) - 1
                if 0 <= move_index < 4:
                    old_move = self.moves[move_index]
                    self.moves[move_index] = move
                    print(f"{self.name} forgot {old_move} and learned {move}!")
    
    def catch(self):
        self.is_caught = True
        print(f"Gotcha! {self.name} was caught!")

# Example usage
pika = Pokemon(25, 'Pikachu', 0.4, 'Mouse', 6.0, 5, 'Electric', 
               'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.')

# Add some moves
pika.learn_move("Thunder Shock")
pika.learn_move("Quick Attack")

# Display details and catch
pika.display_details()
pika.catch()
pika.level_up()
