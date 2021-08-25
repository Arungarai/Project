import random
response='Y'
def checking_winner(user_input, computer_input):
    if user_input==computer_input:
        print("Match Draw")
    elif (user_input == 'r' and computer_input == 'p')or (user_input=='s' and computer_input=='p')or (user_input=='s' and computer_input=='r'):
        print("You won!")
    else:
        print("Computer has won!")

while response=='Y':
    user_input=input("Enter your choice (r for rock,p for paper,s for scissor)")
    if user_input not in ('r','s','p'):
        print("Wrong input!")
        quit()
    choice=['r','p','s']
    computer_input=random.choice(choice)
    print("The computer's input is"+" "+computer_input)
    checking_winner(user_input,computer_input)
    response=input("Do you want to continue 'Y/N'")
    if response not in ('Y','N'):
        print("Enter the proper input")
else:
    print("Exit")
    quit()


