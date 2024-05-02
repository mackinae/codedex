import  random
print("===================")
print("Rock Paper Scissors")
print("===================")

#ask player for input
player = int(input("1) ✊ \n2) ✋ \n3) ✌\nPick a number between 1 and 3: "))
computer = random.randint(1,3)

#determine what choice player made and output it visually
if player == 1:
  print("You chose: ✊")
elif player == 2:
  print("You chose: ✋")
elif player == 3:
  print("You chose: ✌")
else:
  print("Invalid choice")

#determine what the CPU chose and output it visually
if player > 3:
  print("😠")  #check to see if player made valid choice.if true display angry face from CPU
elif computer == 1:
  print("CPU chose: ✊")
elif computer == 2:
  print("CPU chose: ✋")
elif computer == 3:
  print("CPU chose: ✌")

#check win/loss/tie conditions
if player > 3:
  print("Player Forfeits CPU win!") #display forfeit if player chose invalid option
elif(player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
  print("The Player has won!")
elif player == computer:
  print("The Game was a tie!")
else:
  print("The CPU won!")
