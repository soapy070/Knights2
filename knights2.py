import random

def create_knight(knights):
    print("Let's create a knight!")
    knight_name = input("What is the knight's name: ")
    knights.append([knight_name])

def create_weapon(weapons):
    print("Let's create a weapon!")
    weapon_name = input("What is the weapon: ")
    weapons.append([weapon_name])

def change_knight_data(knight):
    print("--- What would you like to update? ---")
    print(f"1: Knight's name: {knight[0]}")
    selection = input("Select your option: ")
    try:
        selection = int(selection)
        if selection == 1:
            new_name = input("What is their new name: ")
            knight[0] = new_name
            print(f"Your knight's new name is: {new_name}")
        else:
            print("--- Please select a valid option ---")
    except ValueError:
        print("--- Invalid input, try again! ---")
        change_knight_data(knight)

def change_weapon_data(weapon):
    print("--- What would you like to update? ---")
    print(f"1: Weapon's name: {weapon[0]}")
    selection = input("Select your option: ")
    try:
        selection = int(selection)
        if selection == 1:
            new_name = input("What is the new weapon name: ")
            weapon[0] = new_name
            print(f"Your weapon's new name is: {new_name}")
        else:
            print("--- Please select a valid option ---")
    except ValueError:
        print("--- Invalid input, try again! ---")
        change_weapon_data(weapon)

def select_knight(knights):
    if len(knights) == 0:
        print("You need to create a knight first!! \n")
    else:
        print("What knight would you like to update?\n")
        for index, knight in enumerate(knights):
            print(f"{index + 1} - Knight's name: {knight[0]}")
        selection = input("\nSelect the knight's number: ")
        try:
            selection = int(selection) - 1
            change_knight_data(knights[selection])
        except (ValueError, IndexError):
            print("--- Invalid input, try again! ---")
            select_knight(knights)

def select_weapon(weapons):
    if len(weapons) == 0:
        print("You need to create a weapon first!! \n")
    else:
        change_weapon_data(weapons[0])

def menu(knights, weapons):
    knights_number = 0
    while True:
        print("What do you want to do?")
        print("1: Create a new knight")
        print("2: Update a knight")
        print("3: Create a new weapon")
        print("4: Update a weapon")
        print("0: Exit")

        try:
            select = int(input("Selection number: "))
            if select == 1:
                create_knight(knights)
                print("\n--- Your Knight ---\n")
                print(f"Knight's name: {knights[-1][0]}\n")
            elif select == 2:
                select_knight(knights)
            elif select == 3:
                create_weapon(weapons)
                print("\n--- Your Weapon ---\n")
                print(f"Weapon's name: {weapons[-1][0]}\n")
            elif select == 4:
                select_weapon(weapons)
            elif select == 0:
                print("--- All your Knights ---\n")
                knights_number = 0
                while knights_number < len(knights):
                    print(f"{knights_number + 1} - Knight's name: {knights[knights_number][0]}")
                if len(knights) == 0:
                    print(f"Wait... You have no knights! Have a number: {random.randint(0,100)}\n")
                else:
                    print("\n")
                knights.clear()
                weapons.clear()
                break
            else:
                print("--- Invalid input, try again! ---")
        except ValueError:
            print("--- Invalid input, try again! ---")

#Setting the scene
knights = []
weapons = []

#Run the program
menu(knights, weapons)
