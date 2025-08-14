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

import random
# Randomly choose a character for the dragon

def play_game():
    while True:
        dragon_hp = 300  

        dragon_characters = ["Dragon Warrior", "Dragon Mage", "Dragon Knight"]
        dragon_character = random.choice(dragon_characters)

        print(f"A wild {dragon_character} appears!")
        print(f"Dragon HP: {dragon_hp}")
        print(f"Dragon Damage: {dragon_damage}")
        
        while True:
            print("\nChoose Your Character:")
            print("1. Wizard")
            print("2. Elf")
            print("3. Human")
            print("4. Dwarf")

            character_choice = input("Pick a character or type 'exit' to quit: ").lower()

            if character_choice == "exit":
                print("Thanks for playing! Goodbye.")
                return


            if character_choice == "wizard" or character_choice == "1":
                character = wizard
                my_hp = wizard_hp
                my_damage = wizard_damage
                break
            elif character_choice == "elf" or character_choice == "2":
                character = elf
                my_hp = elf_hp
                my_damage = elf_damage
                break
            elif character_choice == "human" or character_choice == "3":
                character = human
                my_hp = human_hp
                my_damage = human_damage
                break
            elif character_choice == "dwarf" or character_choice == "4":
                character = dwarf
                my_hp = dwarf_hp
                my_damage = dwarf_damage
                break
            else:
                print("Unknown character, please pick again.")

        print(f"\nYou have chosen the {character.capitalize()}!")
        print(f"HP: {my_hp}")
        print(f"Damage: {my_damage}\n")

        # Battle loop
        while True:
            dragon_hp -= my_damage
            print(f"The {character} damaged the Dragon!!")
            print(f"The Dragon's HP is now {dragon_hp}\n")

            if dragon_hp <= 0:
                print("The Dragon has lost the battle!")
                break

            my_hp -= dragon_damage
            print(f"The Dragon damaged the {character}")
            print(f"The {character}'s HP is now: {my_hp}\n")

            if my_hp <= 0:
                print(f"The {character} has lost the battle!!")
                break

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break


# Start the game
if __name__ == "__main__":
    play_game()

