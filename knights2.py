if name == "main":
    import random

# Call for this when you want to create a new knight
def create_knight(knights):
        print("Let's create a knight!")
        knight_name = input("What is the knight's name: ")
        knights.append([knight_name])

# Call for this when you want to create a new weapon
def create_weapon(weapons):
    print("Let's create a weapon!")
    weapon_name = input("What is the weapon: ")
    weapons.append([weapon_name])

# Call a knight and change their data
def change_knight_data(knights):
    print("--- What would you like to update? ---")
    print(f"1: Knight's name: {knights[0][0]}")
    selection = input("Select your option: ")
    try:
        selection = int(selection)
        if selection == 1:
            new_name = input("What is their new name: ")
            knights[0][0] = new_name
            print(f"Your knight's new name is: {new_name}")
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_knight_data(knights)

# Call a weapon and change its data
def change_weapon_data(weapons):
    print("--- What would you like to update? ---")
    print(f"1: Weapon's name: {weapons[0][0]}")
    selection = input("Select your option: ")
    try:
        selection = int(selection)
        if selection == 1:
            new_name = input("What is the new weapon name: ")
            weapons[0][0] = new_name
            print(f"Your weapon's new name is: {new_name}")
        else:
            print("--- Please select a valid option ---")
    except:
        print("--- Try Again! ---")
        change_weapon_data(weapons)

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
        except:
            print("--- Try Again! ---")
            select_knight(knights)

# Show the current weapon and update it
def select_weapon(weapons):
    if len(weapons) == 0:
        print("You need to create a weapon first!! \n")
    else:
        change_weapon_data(weapons)

# This is the menu and we make our selections here
def menu(knights, weapons):
    knights_number = 0
    while True:
        # Print the display options
        print("What do you want to do?")
        print("1: Create a new knight")
        print("2: Update your knight")
        print("3: Create a new weapon")
        print("4: Update your weapon")
        print("0: Exit")

        # Takes the users selection option
        try:
            select = input("Selection number: ")
            select = int(select)
            print()
            if select == 1:
                create_knight(knights)
                print("\n--- Your Knight ---\n")
                print("Knight's name:  " + str(knights[knights_number][0]) + "\n")
                knights_number += 1
            elif select == 2:
                if len(knights) == 0:
                    print("You need to create a knight first!! \n")
                else:
                    select_knight(knights)
            elif select == 3:
                create_weapon(weapons)
                print("\n--- Your Weapon ---\n")
                print(f"Weapon's name: {str(weapons[0][0])}\n")
            elif select == 4:
                if len(weapons) == 0:
                    print("You need to create a weapon first!! \n")
                else:
                    select_weapon(weapons)
            elif select == 0:
                print("--- All your Knights ---\n")
                knights_number = 0
                while knights_number < len(knights):
                    print(f"{knights_number + 1} - Knight's name: {knights[knights_number][0]}")
                    knights_number += 1
                if len(knights) == 0:
                    print(f"Wait... You have no knights! Have a number: {random.randint(0,100)}\n")
                else:
                    print("\n")
                knights = []
                weapons = []
                break
            else:
                print("--- Try again! ---\n")
        except:
            print("--- Try again! ---\n")
        finally:
            print("--- Try again! ---\n")
#Setting the scene
knights = []
weapons = []

#Run the program
menu(knights, weapons)
