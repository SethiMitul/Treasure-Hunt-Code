print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#Write your code below this line 👇
path_taken = input("You come across a trisection path. Which way do you want to go? (Left Right or Straight)\n").lower()
if path_taken == "straight":
  print("Congratulations on clearing level 1. Welcome to level 2 THE BRIDGE ROUTE!!!")
  lake_question = input("You came across a lake.What are you going to do?(Wait or Swim)\n").lower()
  if lake_question == "swim":
    print("You crossed the lake safely into a place")
    the_door_problem = input("You came across 3 doors A black one, A white one and A Green one. Which one do you pick(White, Black or Green)\n").lower()
    if the_door_problem =="white":
      print('''You got killed by a venemous snake
      Better luck next time..''')
    elif the_door_problem =="black":
      print("Congratulations on finding the Treasure hope you like it.See you another time......")
    elif the_door_problem =="green":
      print('''You got eaten by a tiger
      Better luck next time''')
    else:
      print("Dont outsmart us brother")
  else:
    print("The boat drowned and you killed your self. Try Again")
else:
  print("You are not capable to win the TREASURE.Try agian GAME OVER....")
  exit()
