import time

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

def adventure_game():
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

    print("\033[0;37m\nYou wake up in a crashed car beside a snowy highway.")
    time.sleep(1)
    print("You see a backpack and shattered glass scattered around. What do you do?")
    time.sleep(1)
    print("1. Search the car")
    print("2. Exit the car and look around")
    print("3. Stay in the car to think.")

    choice1 = input("> ")
    if choice1 == "1":
        print("You find a compass, spare clothes, and a granola bar.")
        time.sleep(1)
        print("The compass points northwest. Do you follow it?")
        print("1. Yes")
        print("2. No, search for other options.")

        choice2 = input("> ")
        if choice2 == "1":
            print("You brave the snow and head northwest.")
            print("You find a small cabin in the woods!")
        elif choice2 == "2":
            print("You stay back to consider more options, but time is running out...")
    elif choice1 == "2":
        print("You step out into the freezing cold.")
        print("The wilderness stretches endlessly. Do you...")
        print("1. Follow the highway.")
        print("2. Look for tracks in the snow.")

        choice2 = input("> ")
        if choice2 == "1":
            print("The highway leads to an abandoned gas station.")
        elif choice2 == "2":
            print("You follow the tracks and find a hunter's cabin.")
    elif choice1 == "3":
        print("You decide to stay in the car and conserve energy.")
        print("The cold intensifies, and you start to lose hope...")

    print("\nThank you for playing!")

adventure_game()
