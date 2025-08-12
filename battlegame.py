# Characters (as strings)
wizard = "wizard"
elf = "elf"
human = "human"
dwarf = "dwarf"

# Character HP (as integers):
wizard_hp = 70
elf_hp = 100
human_hp = 150
dwarf_hp = 80

# Character Damage (as integers)
wizard_damage = 150
elf_damage = 100
human_damage = 20
dwarf_damage = 50

# Dragon Stats (as integers)
dragon_hp = 300
dragon_damage = 50

while True:
    print("1.Wizard")
    print("2.Elf")
    print("3.Human")
    print("4.Dwarf")

    character_choice = input("Choose your character: ")

    if character_choice=="1":
        character=wizard
        my_hp=wizard_hp
        my_damage=wizard_damage
        break
    elif character_choice == "2":
        character=elf
        my_hp=elf_hp
        my_damage=elf_damage
        break
    elif character_choice=="3":
         character=human
         my_hp=human_hp
         my_damage=human_damage
         break
    else :
        print("Uknown character")

print(f"You have chosen the {character}!")
print(f"HP: {my_hp}")
print(f"Damage: {my_damage}")


#battle loop
while True:
    dragon_hp = dragon_hp - my_damage
    print(f"The {character} damaged the Dragon!!")
    print(f"The Dragon's HP is now {dragon_hp}\n")

    if dragon_hp <=0:
        print("The Dragon has lost the battle!")
        break

    my_hp = my_hp - dragon_damage
    print(f"The Dragon damaged the {character}")
    print(f"The {character}'s Hp is now: {my_hp}\n")

    if my_hp <=0:
        print(f"The {character} has lost the Battle!!")
        break

import random
# Randomly choose a character for the dragon

dragon_characters = ["Dragon Warrior", "Dragon Mage", "Dragon Knight"]
dragon_character = random.choice(dragon_characters)

print(f"A wild {dragon_character} appears!")
print(f"Dragon HP: {dragon_hp}")
print(f"Dragon Damage: {dragon_damage}")

def choose_character():
    characters = {
        "wizard": {"hp": 70, "attack": 150},
        "elf": {"hp": 100, "attack": 100},
        "human": {"hp": 150, "attack": 20},
        "dwarf": {"hp": 80, "attack": 50}
    }

    while True:
        choice = input("Choose your character (wizard, elf, human, dwarf) or type 'exit' to quit: ").lower()
        if choice == "exit":
            print("Exiting the game.")
            exit()
        if choice in characters:
            print(f"You have chosen the {choice.capitalize}!")
            return choice, characters[choice]["hp"], characters[choice]["attack"]
        else:
            print("Invalid choice. Please try again.")

def battle(character, character_hp, character_attack):
    dragon_hp = 300
    dragon_damage = 50

    while True:
        dragon_hp = dragon_hp - character_attack
        print(f"The {character} damaged the Dragon!")
        print(f"The Dragon's HP is now {dragon_hp}\n")

        if dragon_hp <= 0:
            print("The Dragon has lost the battle!")
            break

        character_hp = character_hp - dragon_damage
        print(f"The Dragon damaged the {character}")
        print(f"The {character}'s HP is now: {character_hp}\n")

        if character_hp <= 0:
            print(f"The {character} has lost the Battle!!")
            break
        
def play_game():
    while True:
        character, character_hp, character_attack = choose_character()
        battle(character, character_hp, character_attack)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
# end of the game
