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

    print("\033[0;37m\nYou wake up in a crashed car beside a snowy highway htting a lonesome tree")
    time.sleep(5)
    print("You don't know why but things looks mising and shattered glass scattered around. What do you do?")
    time.sleep(5)
    print("1. Search the car")
    print("2. Exit the car and look around")
    print("3. Stay in the car to think.")

    choice1 = input("> ")
    if choice1 == "1":
        print("You find a compass, spare clothes, and a flashlight inside a torn backpack")
        time.sleep(4)
        print("The compass points north. Do you take them?")
        print("1. Yes")
        print("2. No, search for other options.")

        choice2 = input("> ")
        if choice2 == "1":
            print("You pocket the compass and flashlight.")
            time.sleep(3)
            print("You also notice you are halfway naked, with the spare clothes being the only protection from frostbite.")
            time.sleep(5)
            print("But eventually, the creep of the cold seaps in. The car is no longer safe.")
            time.sleep(5)
            print("and")
            time.sleep(1)
            print("...")
            time.sleep(1)
        elif choice2 == "2":
            print("You stay back to consider more options, but it is clear there is nothing left of use inside.")
            time.sleep(5)
            print("The cold of the outside creeps in without you knowing...")
            time.sleep(3)
            print("and")
            time.sleep(1)
            print("...")
            time.sleep(1)
    elif choice1 == "2":
        print("You step out into the freezing cold.")
        time.sleep(2)
        print("The dark gray shadow surrounding you, stretching endlessly. Do you...")
        print("1. Follow the highway.")
        print("2. Look for tracks in the snow.")

        choice2 = input("> ")
        if choice2 == "1":
            print("With only worn socks, you tread the highay. You aren't even clear if you know where your going.")
            time.sleep(5)
            print("White specks falls lighly ontop of the highway. Piles of white eventually masking the road before your eyes.")
            time.sleep(5)
            print("There no longer is a highway to follow,")
            time.sleep(3)
            print("and")
            time.sleep(1)
            print("...")
            time.sleep(1)
        elif choice2 == "2":
            print("You see faint tracks of crushed snow travel in a direction you are unsure where it leads.")
            time.sleep(5)
            print("Sooner or later, the tracks will no longer be visible")
            time.sleep(3)
            print("and")
            time.sleep(1)
            print("...")
            time.sleep(1)
    elif choice1 == "3":
        print("You decide to stay in the car and conserve energy, taking measure to seal all visible holes with all you have.")
        time.sleep(5)
        print("Fingers start to stiffen, yet the heart remains warm. You know nothing of what cause for the present.")
        time.sleep(5)
        print("No memory of the crash, nor a reason for why you are here. Yet, you feel as though you do.")
        time.sleep(5)
        print("Chilling fog clouding your mind, despite the sickly hot air filling the room.")
        time.sleep(3)
        print("The harsh cold no longer seems dangerous,")
        time.sleep(2)
        print("yet")
        time.sleep(1)
        print("...")
        time.sleep(1)

    print("\nThank you for playing the demo!")

adventure_game()
