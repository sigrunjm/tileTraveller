# Player in tile 1,1. 
# When he goes north the y value goes +1 when he goes south his y value goes -1.
# When he goes east the x value goes +1 when he goes west his x value goes -1.
# His x and y value can not go below 1 or above 3
# When he enters tile 3,1 he wins the game.
# The program asks the player wich direction in possible (N/n, S/s, W/w, E/e)
# If the player enters a direction that is not possible the program outputs the message "Not a valid direction!"

#possible moves

N = "(N)North"
S = "(S)South"
W = "(W)West"
E = "(E)East"

x = 1
y = 1
player = x , y
print(player)




