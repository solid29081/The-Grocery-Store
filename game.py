# import shit
import time
# set variables
points = 0
items = 0
name = None
budget = 50
# game identifiers
game_name = "The Grocery Store"
game_ver = 1.0
license = "GNU General Public License"
ghub_link = "https://github.com/solid29081/The-Grocery-Store/"

# main game code
print(f"Welcome to {game_name}")
print(f"Version {game_ver}")
print(f"This software is under the {license}")
print(f"You can find the source-code, and more information at {ghub_link}")
time.sleep(5)
print(f"Points: {points}")
print(f"Items: {items}")
print(f"Budget: {budget}")
print(f"Selecting Name...")
time.sleep(0.5)
name = input("What would you like to be called?: ")

if name == None:
  print("You need to input a name to continue the game.")
else:
  print(f"Nice name, {name}!")
  print("Game starts in 3 seconds...")

time.sleep(3)

print(f"Points: {points}")
print(f"Items: {items}")
print(f"Budget: {budget}")
print(f"Name: {name}")
print(None)
print(f"{name} is heading to the store to get some groceries. He has a budget of $50, you can tell if you are going above or below budget from the budget text above.")
time.sleep(3)
print(f"{name} needs these 5 things. Apples, Bananas, Steak, Canned Corn, and a little treat for himself.")
time.sleep(3)
print(f"{name} decides to go to the Fruits and Vegetables section.")
time.sleep(1)
print(f"Which brand should {name} choose for apples?")
print("1. Generic No-Name Brand Apples. $2")
print("2. SUUUUUPER APPLE PRO DELUXES. $10")
time.sleep(0.5)
selection1 = int(input("Choose an option based off the number in front of the item.: "))
if selection1 == 1:
  budget -= 2
  points += 5
if selection1 == 2:
  budget -= 10
  points += 13

time.sleep(1)

print(f"Points: {points}")
print(f"Items: {items}")
print(f"Budget: {budget}")
print(f"Name: {name}")
time.sleep(1)
print(f"Which brand should {name} choose for bananas?")
print("1. Generic No-Name Brand Bananas. $5, $1 per banana")
print("2. BIG ULTRA MAXIMUM BANANAS. $20, $4 per banana")
selection2 = int(input("Choose an option based off the number in front of the item.: "))
if selection2 == 1:
  budget -= 5
  points += 10
if selection2 == 2:
  budget -= 20
  points += 40

time.sleep(1)

print(f"Points: {points}")
print(f"Items: {items}")
print(f"Budget: {budget}")
print(f"Name: {name}")

print(f"{name} needs these 5 things. Apples, Bananas, Steak, Canned Corn, and a little treat for himself.")
print(f"{name} decides to go to the Meats section.")
time.sleep(1)
print(f"Which brand should {name} choose for steak?")
print("1. Farmhouse Steak. $10")
print("2. BIG, JUICY, CHEWY, STEAK. $100")
selection3 = int(input("Choose an option based off the number in front of the item.: "))
if selection3 == 1:
  budget -= 10
  points += 20
if selection3 == 2:
  budget -= 100
  points -= 100

time.sleep(1)

print(f"Points: {points}")
print(f"Items: {items}")
print(f"Budget: {budget}")
print(f"Name: {name}")

print(f"{name} needs these 5 things. Apples, Bananas, Steak, Canned Corn, and a little treat for himself.")
print(f"{name} decides to go to the Canned Foods section.")
time.sleep(1)
print(f"Which brand should {name} choose for canned corn?")
print("1. Generic Canned Corn. $2")
print("2. Freshly Canned Corn. $5")
selection4 = int(input("Choose an option based off the number in front of the item.: "))
if selection4 == 1:
  budget -= 2
  points += 2
if selection4 == 2:
  budget -= 5
  points += 10

time.sleep(1)

print(f"Points: {points}")
print(f"Items: {items}")
print(f"Budget: {budget}")
print(f"Name: {name}")

print(f"{name} needs these 5 things. Apples, Bananas, Steak, Canned Corn, and a little treat for himself.")
print(f"{name} decides to go to the candy section.")
time.sleep(1)
print(f"Should {name} buy a candy bar or should he exit?")
print("1. Buy the candy bar. $1")
print("2. Exit")
selection5 = int(input("Choose an option based off the number in front of the item.: "))
if selection5 == 1:
  budget -= 1
  points += 2
if selection5 == 2:
  print(f"{name} skips getting the candy bar and heads to the exit.")

time.sleep(1)

print("You head to self check-out.")

if budget >= 50:
  print(f"As you go ahead and scan your items, your total comes out to a number that's way above your budget! You try stealing the items, but get arrested.")
  print("Ending 1, Bad Ending.")

if selection1 == 1:
    if selection2 == 1:
      if selection3 == 1:
        if selection4 == 1:
          if selection5 == 2:
            print("Your total comes and you pay, When you get home and enjoy your groceries, you realize they taste bad and you throw them away.")
            print("Ending 2, Cheapskate Ending.")
if selection1 == 1:
    if selection2 == 1:
      if selection3 == 1:
        if selection4 == 1:
          if selection5 == 1:
            print("Your total comes and you pay, When you get home and enjoy your groceries, you realize they taste bad and you throw them away. Except for the candy bar, you liked that.")
            print("Secret Ending, 'At least I got the candy bar' ending.")
else:
  print("Your total comes out and you pay, you enjoy your items.")
  print("Ending 3, Normal Ending")

exit(0)
