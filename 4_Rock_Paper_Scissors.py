import random
print("wellcome to Rock✊, Paper✋,  Scissors🤘 Game.")
user_choice=int(input("what do you choose? Type these--\n1. for Rock ✊\n2. for paper ✋\n3 for Scissors 🤘\nEnter Your Choice: "))
computer_choice=random.randint(1, 3)
print(f"Computer choose {computer_choice}\n")
if(user_choice>3 or user_choice<1):
    print("You Choose Invalid Number\n Plese choose valid Number\n")
elif(user_choice==1 and computer_choice==3):
    print("You Win!🥳\n")
elif(user_choice==3 and computer_choice==1):
    print("You lose!😔\n")
elif(computer_choice>user_choice):
    print("You lose!😔\n")
elif(computer_choice<user_choice):
    print("You Win!🥳\n")
elif(computer_choice==user_choice):
    print("Draw 🤷\n")
else:
    print("Invalid Number\n")