#Creating a dice simulator
#importing a random function
import random

#Creating a dice function
def dice():
    #initial value of is x='y' and using a while loop
    x="y"
    while(x=="y"):
        #no will store a rand value btn 1 to 6
        no=random.randint(1,6)
        #Depending on the number we will print value so we are if ,elif and else
        if(no==1):
            print("______")
            print("|     |")
            print("|  *  |")
            print("|     |")
            print("------")
        elif (no == 2):
            print("______")
            print("|     |")
            print("| * * |")
            print("|     |")
            print("------")
        elif (no == 3):
            print("______")
            print("|  *  |")
            print("|  *  |")
            print("|  *  |")
            print("------")
        elif (no == 4):
            print("______")
            print("| * * |")
            print("|     |")
            print("| * * |")
            print("------")
        elif (no == 5):
            print("______")
            print("| * * |")
            print("|  *  |")
            print("| * * |")
            print("------")
        elif (no == 6):
            print("______")
            print("| * * |")
            print("| * * |")
            print("| * * |")
            print("------")
        else:
            print("You have entered an invalid input")
        #to break the loop user has to enter n, else loop will keep running
        x=input("Enter y to roll a die else enter n :")
#calling the dice function
dice()