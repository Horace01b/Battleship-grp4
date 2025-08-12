# Characters (as strings)
wizard = "wizard"
elf = "elf"
human = "human"

# Character HP (as integers):
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Character Damage (as integers)
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon Stats (as integers)
dragon_hp = 300
dragon_damage = 50

while True:
    print("1.Wizard")
    print("2.Elf")
    print("3.Human")

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






