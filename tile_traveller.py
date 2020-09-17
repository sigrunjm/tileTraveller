# Player in tile 1,1. 
# When he goes north the y value goes +1 when he goes south his y value goes -1.
# When he goes east the x value goes +1 when he goes west his x value goes -1.
# His x and y value can not go below 1 or above 3
# When he enters tile 3,1 he wins the game.
# The program asks the player wich direction in possible (N/n, S/s, W/w, E/e)
# If the player enters a direction that is not possible the program outputs the message "Not a valid direction!"

#possible moves

N = "(N)orth"
S = "(S)outh"
W = "(W)est"
E = "(E)ast"

x = 1
y = 1

while not (x==3 and y==1):
    if ((x == 1) and (y == 1)) or ((x==2) and (y==1)):
        print("You can travel: (N)orth.")
        get_direction = input("Direction: ")
        if get_direction == ("N"):
            y += 1
        else:
            print("Not a valid direction!")
    elif ((x == 1) and (y==2)):
        print("You can travel: (N)orth or (E)ast or (S)outh")
        get_direction = input("Direction: ")
        if get_direction == ("N"):
            y += 1
        elif get_direction == ("S"):
            y -= 1
        elif get_direction == ("E"):
            x += 1
        else: 
            print("Not a valid direction!")
    elif ((x == 2) and (y == 2)) or ((x == 3) and (y == 3)):
        print("You can travel: (S)outh or (W)est")
        get_direction = input("Direction: ")
        if get_direction == ("S"):
            y -= 1
        elif get_direction == ("W"):
            x -= 1
        else:
            print("Not a valid direction!")
    elif ((x == 1) and (y == 3)):
        print("You can travel: (S)outh or (E)ast")
        get_direction = input("Direction: ")
        if get_direction == ("S"):
            y -= 1
        elif get_direction == ("E"):
            x += 1
        else:
            print("Not a valid direction!")
    elif ((x == 2) and (y == 3)):
        print("You can travel: (W)est or (E)ast")
        get_direction = input("Direction: ")
        if get_direction == ("W"):
            x -= 1
        elif get_direction == ("E"):
            x += 1
        else:
            print("Not a valid direction!")
    elif ((x == 3) and (y == 2)):
        print("You can travel: (N)orth or (S)outh")
        get_direction = input("Direction: ")
        if get_direction == ("N"):
            y += 1
        elif get_direction == ("S"):
            y -= 1
        else:
            print("Not a valid direction!")

print('Victory!')












