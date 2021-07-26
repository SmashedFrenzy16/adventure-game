import time
import sys

name = input("Enter your name: ")

print("Hello " + name + ", welcome to your adventure in the cave.")

time.sleep(2)

start = input("Do you want to start the game? (y/n): ")

time.sleep(2)

if start == "y" or start == "Y":
    print("You enter the cave...")
elif start == "n" or start == "N":
    print(name +", you are not living up to your full potential. Please come back when you are ready.")
    sys.exit
if start == "y" or start == "Y":
    first_encounter = input("You walk to a passage that is divided, you can either go right (r) or left (l). Which one do you you choose?: ") 
    time.sleep(2)
    if first_encounter == "r" or first_encounter == "R":
        print("You chose to go right and met a bear.")
        time.sleep(1)
    else:
        print("You have walked to a dead end. You walk out of the cave and hope to restart the game. See you in the cave soon!")
        sys.exit
    if first_encounter ==  "r" or first_encounter == "R":
        fight = input("Do you choose to fight it with a sword (s) or with a hammer (h)?: ")
        if fight == "s" or fight == "S":
            print("You killed the bear!")
        if fight == "h" or fight =="H":
            print("You died! The bear is feeding on you! Better luck next time!")
            sys.exit
        if fight == "s" or fight == "S":
            time.sleep(2)
            diamond_room = input("You walk into the room with a bag of diamonds. You pick the bag up, but the two ways out are: Going through a room of one year old boiling lava (bl), or going through the room of a really savage bull (sb). Which one do you choose?: ")
            if diamond_room == "bl":
                print("You win! Congratulations!")
        else:
            print("You were torn apart by the bear and now are hanging on the wall. You are dead")
            sys.exit
