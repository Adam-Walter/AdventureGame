import json
import GameLoader as gl

cfile = open('commands.json')
commanddict = json.load(cfile)
cfile.close()

tfile = open('itemtags.json')
itemtags = json.load(tfile)
tfile.close()

def parseinput(input):
    commandtype = ''
    target = ''
    argument = ''
    i = input.split(' ')
    for k in i:
        if k.lower() in commanddict.keys():
            commandtype = commanddict[k.lower()]
    if commandtype != '':
        if commandtype == 'move':
            return move(i)
        if commandtype == 'attack':
            return attack(i)        
        if commandtype == 'look':
            return look(i)
    else:
        return "I'm sorry, that command was not valid."

def displayenv():
    s = gl.roomdict[gl.player.getlocation()].getdescription() + ' '
    for i in gl.roomdict[gl.player.getlocation()].getexits():
        s+="To the " + gl.exitdict[i].getdirection() + " is " + gl.exitdict[i].getdescription() + ' '
    for i in gl.roomdict[gl.player.getlocation()].getinv():
        s+= "You see a " + gl.itemdict[i].getname() + '. '
    for i in gl.roomdict[gl.player.getlocation()].getcontainers():
        s+="There is a " + gl.containerdict[i].getname() + '. '
    for i in gl.roomdict[gl.player.getlocation()].getnpcs():
        s+= "There is a " + gl.npcdict[i].getname() + ' here with you. ' 
    return s

def look(i):
    target = ''
    for j in i:
        for k in gl.roomdict[gl.player.getlocation()].getinv():
            if j in gl.itemdict[k].gettags():
                target = gl.itemdict[k]
        for k in gl.roomdict[gl.player.getlocation()].getcontainers():
            if j in gl.containerdict[k].gettags():
                target = gl.containerdict[k]
        for k in gl.roomdict[gl.player.getlocation()].getnpcs():
            if j in gl.npcdict[k].gettags():
                target = gl.npcdict[k]
    if target != '':
        return target.getdescription()
    else:
        return displayenv()

def move(i):
    target = ''
    for k in i:
        if k.lower() in ['north','south','east','west']:
            target = k
            return gl.roomdict[gl.player.getlocation()].move(gl.player,target) + "\n" + displayenv()
    if target == '':
        return "I'm sorry I don't understand where you want to move to."

def attack(i):
    argument = ''
    target = ''
    for k in i:
        have = True
        if k in itemtags:
            have = False
            tag = k
        for j in gl.player.getinv():
            if k.lower() in gl.itemdict[j].gettags():
                argument = gl.itemdict[j]
                have = True
    for k in i:
        for j in gl.roomdict[gl.player.getlocation()].getnpcs():
            if k in gl.npcdict[j].gettags():
                target = gl.npcdict[j]
    if target == '':
        if argument != '' and have == True:
            return 'You attack the air with the ' + argument.getname()
        elif have == True:
            return 'You attack the air with your fists!'
    elif target != '':
        if argument != '' and have == True:
            return 'You attack the ' + target.getname() + ' with the ' + argument.getname()
        elif have == True:
            return 'You attack the ' + target.getname() + ' with your fists!'
    else:
        return 'You do not have a ' + tag