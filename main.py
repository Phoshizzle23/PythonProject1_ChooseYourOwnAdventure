# Project #4 - Choose Your Own Adventure

import time

def introduction():
    print("You are a brave knight ⚔️ on a quest to rescue Princess Bella 👸🏼")
    time.sleep(2)
    print("Princess Bella 👸🏼 is locked in a tower 🏰 guarded by a fierce dragon 🐉🔥🐉🔥")
    time.sleep(2)
    print("You must make your way through a dangerous path 🛤️ from the mystic lake 🏞️ to reach the tower 🐲")
    time.sleep(2)
    print("Be cautious❗ Along the road, you will encounter goblins 👺 and face many challenges 🧗🏼")
    time.sleep(2)
    print("Your choices will determine your fate 🔮 Good luck, brave knight 🌟")
    time.sleep(2)
    print("\n---\n")

def mystic_lake():
    print("You arrive at the mystic lake 🏞️ shimmering with magical energy ✨")
    time.sleep(2)
    print("As you approach the lake 🏞️ you see a small boat tied to the shore ⛵")
    time.sleep(2)
    print("What do you do❔")
    time.sleep(1)

    choice = input("1. Get on the boat and row across the lake ⛵\n"
                   "2. Go around the lake and continue on foot 🏃 \n"
                   "Enter your choice (1 or 2): ")

    if choice == "1":
        print("You choose to take the boat and row across the lake 🚣🏼‍♂️ ")
        time.sleep(2)
        print("The boat glides smoothly, and you reach the other side safely 🚣 ")
        time.sleep(2)
        print("Congratulations❗ You have successfully crossed the mystic lake ✅ ")
        time.sleep(2)
        goblin_encounter()
    elif choice == "2":
        print("You decide to go around the lake and continue on foot 👣 ")
        time.sleep(2)
        print("As you make your way through the dense forest, you feel a sense of foreboding 👻 ")
        time.sleep(2)
        print("Suddenly, a group of goblins ambushes you❗ 👿")
        time.sleep(2)
        print("Prepare for a fight❗ 🥊")
        time.sleep(2)
        battle()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        mystic_lake()

def goblin_encounter():
    print("You continue on your journey and come across a group of goblins blocking the path 🚧 ")
    time.sleep(2)
    print("They seem ready for a fight 👊🏼 ")
    time.sleep(2)
    print("What do you do❔")
    time.sleep(1)

    choice = input("1. Engage in combat and defeat the goblins 💥 \n"
                   "2. Try to negotiate and find a peaceful solution 🤝 \n"
                   "Enter your choice (1 or 2): ")

    if choice == "1":
        print("You draw your sword and charge at the goblins❗ 🗡️ ")
        time.sleep(2)
        print("After a fierce battle, you emerge victorious 💥 ")
        time.sleep(2)
        print("Congratulations❗ You have defeated the goblins 🎖️ ")
        time.sleep(2)
        tower()
    elif choice == "2":
        print("You decide to attempt negotiations with the goblins 💬 ")
        time.sleep(2)
        print("Surprisingly, the goblins agree to let you pass peacefully 🙏🏻")
        time.sleep(2)
        print("You thank them and continue your journey 🕊️ ")
        time.sleep(2)
        tower()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        goblin_encounter()

def battle():
    print("You engage in a fierce battle with the goblins❗ ⚒️ ")
    time.sleep(2)
    print("The fight is intense, but your skill and bravery prevail 🥇 ")
    time.sleep(2)
    print("Congratulations❗ You have defeated the goblins 💎 ")
    time.sleep(2)
    tower()

def tower():
    print("You finally arrive at the tower where Princess Bella is imprisoned 🏰")
    time.sleep(2)
    print("As you approach, the fearsome dragon awakens and prepares to attack❗ 🐉 ")
    time.sleep(2)
    print("What do you do❔")
    time.sleep(1)

    choice = input("1. Engage in a direct fight with the dragon 👿🐲💀\n" 
                   "2. Look for a way to outsmart the dragon 🌈🐉\n"
                   "Enter your choice (1 or 2): ")

    if choice == "1":
        print("You gather your courage and face the dragon head-on❗ 🐲 ")
        time.sleep(2)
        print("After an epic battle, you defeat the dragon 👹💀")
        time.sleep(2)
        print("Congratulations❗ You have rescued Princess Bella and completed your quest❗ 🌟 ")
        time.sleep(2)
        ending()
    elif choice == "2":
        print("You decide to assess the situation and look for a way to outsmart the dragon 🐲 ")
        time.sleep(2)
        print("After careful observation, you notice a hidden passage that leads to the tower 🧗 ")
        time.sleep(2)
        print("You sneak past the dragon and reach Princess Bella 👸🏼 ")
        time.sleep(2)
        print("Congratulations❗ You have rescued Princess Bella and completed your quest❗ 🦄")
        time.sleep(2)
        ending()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        tower()

def ending():
    print("Princess Bella is overjoyed to be rescued by you, the brave knight ⚔️ ")
    time.sleep(2)
    print("You both return to the kingdom, where you are hailed as a hero 🦹‍♂️ ")
    time.sleep(2)
    print("Your valor and courage will be remembered for generations to come 👰💎👑 ")
    time.sleep(2)

# Start the adventure
introduction()
mystic_lake()

# Print the contents of "The End.txt" file
file_path = "The End.txt"

try:
    with open(file_path, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")

