import GameLoader as gl
import CommandParser  as compar

def displayenv():
    print(gl.roomdict[gl.player.getlocation()].getdescription(), end = ' ')
    for i in gl.roomdict[gl.player.getlocation()].getexits():
        print("To the " + gl.exitdict[i].getdirection() + " is " + gl.exitdict[i].getdescription(), end = ' ')
    for i in gl.roomdict[gl.player.getlocation()].getinv():
        if i != '0':
            print("You see a " + gl.itemdict[i].getname(),end = '.')
    for i in gl.roomdict[gl.player.getlocation()].getcontainers():
        if i != '0':
            print("There is a " + gl.containerdict[i].getname(),end = '.')
    print(" ")

gameover = False
while gameover != True:
    displayenv()
    print(compar.parseinput(input()))

