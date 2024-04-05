import random

Uscore = 0
Cscore = 0
def Guess_Game():
    global Uscore,Cscore
    print("Welcome to Number Guessing Game:\n")
    User = int(input("Enter a Number Between 1 and 10000: "))
    Correct_Guess = random.randint(1, 10000)
   
    if User == Correct_Guess:
        print("Congrats, Your guess is correct")
        Uscore += 1
    else:
        print("Incorrect, Please try again!")
        print("Correct answer:", Correct_Guess)
        Cscore += 1
       
    Attempt = input("Do you want to Continue (Y/N): ")
    if Attempt.upper() == 'Y':
        Guess_Game()
    else:
        print("User:", Uscore, "Computer:", Cscore)
        return

Guess_Game()
