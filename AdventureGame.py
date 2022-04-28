import GameLoader as gl
import CommandParser  as compar

gameover = False
print(compar.displayenv())
while gameover != True:   
    print(">>>", end =" ")
    print(compar.parseinput(input().lower()))