#rock paper scissor game demo

import random

user_score=0
computer_score=0
computer_choices=[1,2,3]
running=True



print("""
    SELECT OPTIONS!!!
    1.ROCK
    2.PAPER
    3.SCISSOR""")
while running:
    for round_play in range(1,6):
        print(f"======round: {round_play}=======")
        user=int(input("User-option(1,2,3): "))
        #randomly computer chooses
        computer_choice=random.choice(computer_choices)
        print(f'Computer choice: {computer_choice}')
        if user<=0 or user>3:
            print("invalid option")
            break
        elif (user == 1 and computer_choice == 3) or (user == 2 and computer_choice == 1) or (
                user == 3 and computer_choice == 2):
            print("you win")
            user_score+=1

        elif user==computer_choice:
            print("TIE (DRAW)")
            user_score+=1
            computer_score+=1

        else:
            print("computer win")
            computer_score+=1
    play_again=input("want play again after 5 rounds (y/n): ").lower()
    if not play_again=="y":
        running=False

#----------TOTAL SCORE's-----------------
print()
print("====== SCORE BOTH TEAM=====")
print(f'User Score: {user_score} || Computer Score: {computer_score}')


#------Winner--------
print("=====WINNER======")
if user_score>computer_score:
    print(f"Congratulation User win")
elif user_score<computer_score:
    print(f"Congratulation Computer win")
else:
    print("GAME IS TIE")

