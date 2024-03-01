# Programmer: Sean Gay
# Date : 3.1.2024


import random
import pickle

# Global game state
game_state = {
    'player': {},
    'locations': {},
    'quests': {},
    'factions': {},
    'abilities': {},
    'spells': {},
    'crafting_recipes': {},
    'magic_schools': {},
    # ... (add more as needed)
}

# Character creation
def create_character():
    player_name = input("Enter your character's name: ")
    player_race = input("Choose your race (Human, Elf, Dwarf): ")
    player_class = input("Choose your class (Warrior, Mage, Rogue): ")

    # Set initial attributes based on race and class
    initial_attributes = {'strength': 5, 'intelligence': 5, 'dexterity': 5}
    if player_race == 'Elf':
        initial_attributes['intelligence'] += 2
    elif player_race == 'Dwarf':
        initial_attributes['strength'] += 2

    game_state['player'] = {
        'name': player_name,
        'race': player_race,
        'class': player_class,
        'attributes': initial_attributes,
        'level': 1,
        'experience': 0,
        'health': 10,
        'mana': 10,
        'gold': 0,
        'inventory': [],
        'equipment': {},
        'skills': {},
        'status_effects': [],
        'location': 'Starting Town',
    }

# Location definition
def create_location(name, description, quests=None, enemies=None, treasures=None):
    game_state['locations'][name] = {
        'description': description,
        'quests': quests or [],
        'enemies': enemies or [],
        'treasures': treasures or [],
        # ... (add more properties as needed)
    }

# Quest definition
def create_quest(name, description, rewards=None, prerequisites=None):
    game_state['quests'][name] = {
        'description': description,
        'rewards': rewards or {},
        'prerequisites': prerequisites or {},
        'status': 'available',  # or 'completed', 'failed', etc.
        # ... (add more properties as needed)
    }

# Ability definition
def create_ability(name, description, damage_range):
    game_state['abilities'][name] = {
        'description': description,
        'damage_range': damage_range,
        # ... (add more properties as needed)
    }

# Spell definition
def create_spell(name, description, mana_cost, effect):
    game_state['spells'][name] = {
        'description': description,
        'mana_cost': mana_cost,
        'effect': effect,
        # ... (add more properties as needed)
    }

# Crafting recipe definition
def create_crafting_recipe(name, ingredients, result):
    game_state['crafting_recipes'][name] = {
        'ingredients': ingredients,
        'result': result,
        # ... (add more properties as needed)
    }

# Magic school definition
def create_magic_school(name, spells):
    game_state['magic_schools'][name] = {
        'spells': spells,
        # ... (add more properties as needed)
    }

# ... (add more functions to create factions, mini-games, etc.)

# Game initialization
def initialize_game():
    create_character()
    create_location('Starting Town', 'A small town to begin your journey.')

# Example usage:
initialize_game()
print(game_state)


