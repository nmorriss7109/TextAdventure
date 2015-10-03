import time
pause = 3.5


print("Welcome to my Domain... I am your humble God and narrator.")

ans = input("If you wish to continue, type \"y\"")

if ans.lower() == "y":
    print("Ok then, let's go!")
elif ans.lower() == "yes":
    print("I said \"type \'y\'\"! But, I guess that works for now... Please just input \"y\" or \"n\" in the future.")
else:
    print("No? Ok then...")

name = input("Brave warrior, what is your name?").lower()
name = name[0].upper() + name[1:]

print(name + "... You enter a large, stone building in the center of town, "
      "looking for someone to decide and sponsor your next adventure...")
time.sleep(pause)
print("Before you stand three patrons... "
      "The first of which seeks a the mythical stone of wisdom from the treacherous skeleton dungeon")
print("The second wishes to recover a legendary blade wielded by one of the ancient orc kings, Gorgath the Elder")
ans = input("")




