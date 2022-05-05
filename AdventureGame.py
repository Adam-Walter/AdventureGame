#Import the other modules that make up the game.
import GameLoader as gl
import CommandParser  as compar



#display the enviroment once initially and then start a loop to ask for player, input parse it, and display the result as long as gameover is not equal to True
gameover = False
print(compar.displayenv())
while gameover != True:   
    print(">>>", end =" ")
    print(compar.parseinput(input().lower()))