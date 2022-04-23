import GameLoader as gl
import CommandParser  as compar

'''def displayenv():
    print(gl.roomdict[gl.player.getlocation()].getdescription(), end = ' ')
    for i in gl.roomdict[gl.player.getlocation()].getexits():
        print("To the " + gl.exitdict[i].getdirection() + " is " + gl.exitdict[i].getdescription(), end = ' ')
    for i in gl.roomdict[gl.player.getlocation()].getinv():
        print("You see a " + gl.itemdict[i].getname(),end = '.')
    for i in gl.roomdict[gl.player.getlocation()].getcontainers():
        print("There is a " + gl.containerdict[i].getname(),end = '.')
    for i in gl.roomdict[gl.player.getlocation()].getnpcs():
        print("There is a " + gl.npcdict[i].getname(),end = ' here with you.') 
    print(" ")'''

gameover = False
print(compar.displayenv())
while gameover != True:   
    print(compar.parseinput(input().lower()))