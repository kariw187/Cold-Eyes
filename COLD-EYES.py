import time

# Function to display ASCII art
def display_ascii_art():
    print("""
 ▄████▄   ▒█████   ██▓    ▓█████▄    ▓█████▓██   ██▓▓█████   ██████ 
▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▒██▀ ██▌   ▓█   ▀ ▒██  ██▒▓█   ▀ ▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▒██░    ░██   █▌   ▒███    ▒██ ██░▒███   ░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▒██░    ░▓█▄   ▌   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄   ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░░██████▒░▒████▓    ░▒████▒ ░ ██▒▓░░▒████▒▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒    ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒     ░ ░  ░▓██ ░▒░  ░ ░  ░░ ░▒  ░ ░
░        ░ ░ ░ ▒    ░ ░    ░ ░  ░       ░   ▒ ▒ ░░     ░   ░  ░  ░  
░ ░          ░ ░      ░  ░   ░          ░  ░░ ░        ░  ░      ░  
░                          ░                ░ ░                     
""")

# Function to display the player's inventory
def display_inventory(inventory):
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Your inventory is empty.")

# Function to handle player commands
def handle_command(command, inventory, current_location):
    command = command.lower().strip()
    parts = command.split()
    action = parts[0] if parts else ""
    target = " ".join(parts[1:]) if len(parts) > 1 else ""

    if action == "take":
        if current_location == "car" and target in ["compass", "flashlight", "granola bar"]:
            if target not in inventory:
                inventory.append(target)
                print(f"You take the {target}.")
            else:
                print(f"You already have the {target}.")
        elif current_location == "highway" and target == "key":
            if target not in inventory:
                inventory.append(target)
                print("You find a small key buried in the snow. It might unlock something.")
            else:
                print("You already have the key.")
        else:
            print(f"There is no {target} here.")

    elif action == "go":
        if target in ["north", "south", "east", "west"]:
            if current_location == "car" and target == "north":
                print("You head north along the highway.")
                return "highway"
            elif current_location == "highway" and target == "south":
                print("You return to the crashed car.")
                return "car"
            else:
                print(f"You can't go {target} from here.")
        else:
            print("Invalid direction. Try 'go north', 'go south', etc.")

    elif action == "look":
        if current_location == "car" and target == "car":
            print("The car is badly damaged. You see a compass, flashlight, and granola bar inside.")
        elif current_location == "highway" and target == "snow":
            print("You notice something glinting in the snow.")
        else:
            print(f"There is nothing to look about {target} here.")

    elif action == "use":
        if target == "key" and "key" in inventory:
            print("You use the key to try to start the car. It sputters to life!")
            print("You drive away from the crash site and survive the cold.")
            print("\033[92mCongratulations! You've escaped the wilderness.\033[39m")
            return "end"
        else:
            print(f"You can't use {target} here.")

    elif action == "inventory":
        display_inventory(inventory)

    elif action == "quit":
        print("\nYou decide to give up. The cold consumes you.")
        print("\033[91mGame Over.\033[39m")
        return "end"

    else:
        print("Invalid command. Try 'take [item]', 'go [direction]', 'look [object]', etc.")

    return current_location

# Main game function
def cold_eyes_game():
    # Initialize player inventory and game state
    inventory = []
    current_location = "car"
    game_over = False

    # Introduction
    print("\033[96mHot breath sickens the noxious air within the metal van,")
    time.sleep(3)
    print("Chattering tones radiate, echoing through my ears.")
    time.sleep(3)
    print("The screen glows fresh; I lay my head back,")
    time.sleep(3)
    print("Watching snowflakes dance as they pass by.")
    time.sleep(3)
    print("\nSky and earth swallowed by a blanket of white,")
    time.sleep(3)
    print("Time stretches, snaps, then recoils like a taut string.")
    time.sleep(3)
    print("A jolt, a skid—then a splintered tree,")
    time.sleep(3)
    print("Lost in the vastness of this pale sea.")
    time.sleep(3)
    print("\nLast I saw… rather, last I felt—")
    time.sleep(3)
    print("Was its heated breath against my skin,")
    time.sleep(3)
    print("And their piercing...")
    time.sleep(2)
    display_ascii_art()
    time.sleep(3)
    print("...Watching me.")
    time.sleep(3)
    
    print("\033[34\nmWelcome to Cold Eyes.")
    time.sleep(2)
    print("You wake up in a crashed car beside a snowy highway.")
    time.sleep(2)
    print("The air is freezing, and the world is eerily silent.")
    time.sleep(2)
    print("You must make careful choices to survive the cold and uncover the truth.\033[39m")
    time.sleep(2)

    # Main game loop
    while not game_over:
        print(f"\nYou are at the {current_location}. What do you do?")
        command = input("> ")
        new_location = handle_command(command, inventory, current_location)

        if new_location == "end":
            game_over = True
        else:
            current_location = new_location

# Run the game
cold_eyes_game()
