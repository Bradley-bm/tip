import os
def shutdown(command):
    '''This function checks whether the user wants to shut down the computer.'''
    if command == "Yes":
        print("Shutting down the computer...")
        os.system("shutdown /s /t 30")
    elif command == "No":
        print("Abort shutdown.")
    else:
        print("Sorry, invalid input.")
user_input = input("Do you want to shut down your computer? (Yes/No): ")
shutdown(user_input)
