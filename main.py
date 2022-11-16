import random
from logo import logo

print(logo)


def com_num():
    global num
    num = random.randint(0, 100)

def easy_lvl():
    pl_term = 10
    left_term = 0
    while left_term < 10:
        pl_num = int(input("Guess the number : "))
        if pl_num == num:
            print(" !! Hurray !! You WIN ")
            break
        elif pl_num < num:
            print("it is lower ")
            left_term = left_term + 1
            pl_term = pl_term - 1
            print(f" Your Remaining Attempt :  {pl_term} ")
        else:
            print(" It is high ")
            left_term = left_term + 1
            pl_term = pl_term - 1
            print(f" Your Remaining Attempt :  {pl_term} ")
    else:
        print(" Your Game Over and the correct number is : ", num)



def hard_lvl():
    pl_term = 5
    left_term = 0
    while left_term < 5:
        pl_num = int(input("Guess the number : "))
        if pl_num == num:
            print(" !! Hurray !! You get it ")
            break
        elif pl_num < num:
            print("it is lower ")
            left_term = left_term + 1
            pl_term = pl_term - 1
            print(f" Your Remaining Attempt :  {pl_term} ")
        else:
            print(" It is high ")
            left_term = left_term + 1
            pl_term = pl_term - 1
            print(f" Your Remaining Attempt :  {pl_term} ")
    else:
        print(" Your Game Over and the correct number is : ", num)


com_num();

Flag = True
while Flag:
    ask_new = input(" Want to play game ( y for yes and n for no ): ").lower()
    if ask_new == "y":
        ask = input(" Enter the Lever You Want To Play : ( H for hard and E for easy ) : ").lower()
        if ask == "h":
            hard_lvl();
        elif ask == "e":
            easy_lvl();
    else:
        print(" Good Bye ")
        Flag = False