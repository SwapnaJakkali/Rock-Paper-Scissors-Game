import random 

choices=['rock','paper','scissors']

user_score = 0
computer_score = 0

while True:
    user_choice=input("choose any of from choices[rock,paper,scissors] or exit to quit the game :")

    if user_choice=='exit':
        print("\nfinal score , yours",user_score,"computers score:",computer_score)
        print("\nthanks for playing")
        result = abs(user_score-computer_score)
        if user_score>computer_score:
            print("Congrats you won by ",result ,"point" if result==1 else "points")
        elif user_score==computer_score:
            print("its a tie!")
        else:
            print("You lose by ",result , "point" if result==1 else "points"  )
        break 
    if user_choice not in choices:
        print("invalid choice try again")
        continue
    computer_choice=random.choice(choices)
    print("you choose :",user_choice)
    print("computer choose :",computer_choice)

    if user_choice==computer_choice:
        print("its a tie")

    elif (user_choice=='rock' and computer_choice=='scissors') or (user_choice=='paper'and computer_choice=='rock') or (user_choice=='scissors' and computer_choice=='paper'):
        print("You won")
        user_score+=1

    else:
        print("You lose")
        computer_score+=1 
    print("Yours score :",user_score,"Computers score :",computer_score)