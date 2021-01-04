import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock,paper,scissors]

userChoice = int(input("What do you choose?\n\nType\n0 for Rock\n1 for Paper\n2 for Scissors\n\n"))
computerChoice = int(random.randint(0,2))

print(f"\nYour choice: \n{items[userChoice]}")
print(f"Computer choice: \n{items[computerChoice]}")

if userChoice == 0:
  if computerChoice == 0:
    print("\nIt's a Draw!\n")
   
  elif computerChoice == 1:
    print("\nComputer Win!\n")
  
  else:
    print("\nYou Win!\n")

elif userChoice == 1:
  if computerChoice == 0:
    print("\nYou Win!\n")
   
  elif computerChoice == 1:
    print("\nIt's a Draw!\n")
  
  else:
    print("\nComputer Win!\n")

else:
  if computerChoice == 0:
    print("\nComputer Win!\n")
   
  elif computerChoice == 1:
    print("\nYou Win!\n")
  
  else:
    print("\nIt's a Draw!\n")
