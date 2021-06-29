import random
def random_fun():
    random_number = random.randrange(0,100)
    User_input =input("Enter user input:")
    if random_number == User_input:
        print("Draw")
    else:
        print("Computer win!")
        
    user_input = input("if you want to continue (yes/no):")
    
    if user_input == "yes":
        random_fun()
    else:
        print("The program was terminated")
        
random_fun()
