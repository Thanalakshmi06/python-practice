# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
def random_fun():
    my_list = ["saa","boo","three"]
    random_number = random.choice(my_list) 
    print(random_number)
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
