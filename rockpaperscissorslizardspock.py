import  random
print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")

#ask player for input
player = int(input("1) ✊ \n2) ✋ \n3) ✌\n4) 🦎\n5) 🖖\nPick a number between 1 and 5: "))
computer = random.randint(1,5)

#determine what choice player made and output it visually
if player == 1:
  print("You chose: ✊")
elif player == 2:
  print("You chose: ✋")
elif player == 3:
  print("You chose: ✌")
elif player == 4:
  print("You chose :🦎")
elif player == 5:
  print("You chose: 🖖")
else:
  print("Invalid choice")

#determine what the CPU chose and output it visually
if player > 5:
  print("😠")  #check to see if player made valid choice.if true display angry face from CPU
elif computer == 1:
  print("CPU chose: ✊")
elif computer == 2:
  print("CPU chose: ✋")
elif computer == 3:
  print("CPU chose: ✌")
elif computer == 4:
  print("CPU chose: 🦎")
else:
  print("CPU chose: 🖖")

#check win/loss/tie conditions
if player > 5:
  print("Player Forfeits CPU win!") #display forfeit if player chose invalid option
elif(player == 1 and computer == 3) or (player == 1 and computer == 4) or (player == 2 and computer == 1) or(player == 2 and computer == 5) or (player == 3 and computer == 2) or (player == 3 and computer == 4) or (player == 4 and computer == 5) or (player == 4 and computer == 3) or (player == 5 and computer == 3) or (player == 5 and computer == 1):
  print("The Player has won!")
elif player == computer:
  print("The Game was a tie!")
else:
  print("The CPU won!")
