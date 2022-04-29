import json
from os import name
import GameLoader as gl

cfile = open('data/commands.json')
commanddict = json.load(cfile)
cfile.close()

tfile = open('data/itemtags.json')
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
        if commandtype == 'take':
            return take(i)
        if commandtype == 'drop':
            return drop(i)
        if commandtype == 'checkinv':
            return checkinv(i)
        if commandtype == 'open':
            return open(i)
    else:
        return "I'm sorry, that command was not valid."

def displayenv():
    s = gl.roomdict[gl.player.getlocation()].getdescription() + '  '

    __exitlen = len(gl.roomdict[gl.player.getlocation()].getexits())
    __count = 1
    for i in gl.roomdict[gl.player.getlocation()].getexits():
        if __count == 1 and __count != __exitlen:
            s+="To your " + gl.exitdict[i].getdirection() + " is " + gl.exitdict[i].getdescription() + ', '
        elif __count == 1 and __count == __exitlen:
            s+="To your " + gl.exitdict[i].getdirection() + " is " + gl.exitdict[i].getdescription() + '.  '
        elif __count > 1 and __count != __exitlen:
            s+="to the " + gl.exitdict[i].getdirection() + " is " + gl.exitdict[i].getdescription() + ', '
        elif __count == __exitlen and __count > 1:
            s+="and to the " + gl.exitdict[i].getdirection() + " there is " + gl.exitdict[i].getdescription() + '.  '
        __count += 1

    __invlen = len(gl.roomdict[gl.player.getlocation()].getinv())
    __count = 1
    for i in gl.roomdict[gl.player.getlocation()].getinv():
        if gl.itemdict[i].getname()[0].lower() in ['a','e','i','o','u']:
            __aan = 'an '
        else:
            __aan = 'a ' 
        if __count == 1 and __count != __invlen:
            s+= "You see " + __aan + gl.itemdict[i].getname() + ', '
        elif __count == 1 and __count == __invlen:
            s+= "You see " + __aan + gl.itemdict[i].getname() + '.  '
        elif __count > 1 and __count != __invlen:
            s+= __aan + gl.itemdict[i].getname() + ', '
        elif __count == __invlen and __count > 1:
            s+= "and " + __aan + gl.itemdict[i].getname() + '.  '
        __count += 1

    __contlen = len(gl.roomdict[gl.player.getlocation()].getcontainers())
    __count = 1
    for i in gl.roomdict[gl.player.getlocation()].getcontainers():
        if gl.containerdict[i].getname()[0].lower() in ['a','e','i','o','u']:
            __aan = 'an '
        else:
            __aan = 'a ' 
        if __count == 1 and __count != __contlen:
            s+="There is " + __aan + gl.containerdict[i].getname() + ', '
        elif __count == 1 and __count == __contlen:
            s+="There is " + __aan + gl.containerdict[i].getname() + '.  '
        elif __count > 1 and __count != __contlen:
            s+= __aan + gl.containerdict[i].getname() + ', '
        elif __count == __contlen and __count > 1:
            s+="and " + __aan + gl.containerdict[i].getname() + '. '
        __count += 1

    for i in gl.roomdict[gl.player.getlocation()].getcontainers():
        if gl.containerdict[i].getopen() == True:
            __invlen = len(gl.containerdict[i].getinv())
            if __invlen == 0:
                s+="The " + gl.containerdict[i].getname() + " is empty.  "
            __count = 1
            for k in gl.containerdict[i].getinv():
                if gl.itemdict[k].getname()[0].lower() in ['a','e','i','o','u']:
                    __aan = 'an '
                else:
                    __aan = 'a ' 
                if __count == 1 and __count != __invlen:
                    s+="In the " + gl.containerdict[i].getname() + " there is " + __aan + gl.itemdict[k].getname() + ", "
                elif __count == 1 and __count == __invlen:
                    s+="In the " + gl.containerdict[i].getname() + " there is " + __aan + gl.itemdict[k].getname() + ".  "
                if __count > 1 and __count != __invlen:
                    s+= __aan + gl.itemdict[k].getname() + ", "
                elif __count == __invlen and __count > 1:
                    s+= "and " + __aan + gl.itemdict[k].getname() + ".  "
                __count += 1

    __npclen = len(gl.roomdict[gl.player.getlocation()].getnpcs())
    __count = 1
    for i in gl.roomdict[gl.player.getlocation()].getnpcs():
        if gl.npcdict[i].getname()[0].lower() in ['a','e','i','o','u']:
            __aan = 'an '
        else:
            __aan = 'a ' 
        if __count == 1 and __count != __npclen:
            s+= "There is " + __aan + gl.npcdict[i].getname() + ', '
        elif __count == 1 and __count == __npclen:
            s+= "There is " + __aan + gl.npcdict[i].getname() + ' here with you.  '
        elif __count > 1 and __count != __npclen:
            s+= __aan + gl.npcdict[i].getname() + ', '
        elif __count == __npclen and __count > 1:
            s+= "and " + __aan + gl.npcdict[i].getname() + ' here with you.  '
        __count += 1

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
            return 'You attack the ' + target.getname() + ' with the ' + argument.getname() + '.  ' + target.damage(argument.getdamage())
        elif have == True:
            return 'You attack the ' + target.getname() + ' with your fists!  ' + target.damage(10)
    else:
        return 'You do not have a ' + tag

def take(i):
    target = ''
    for k in i:
        have = True
        if k in itemtags:
            have = False
            tag = k
        for j in gl.roomdict[gl.player.getlocation()].getinv():
            if k.lower() in gl.itemdict[j].gettags():
                target = gl.itemdict[j]
                have = True
        for j in gl.roomdict[gl.player.getlocation()].getcontainers():
            for l in gl.containerdict[j].getinv():
                if k.lower() in gl.itemdict[l].gettags():
                    target = gl.itemdict[l]
                    have = True
    if target != '' and have == True:
        return gl.roomdict[gl.player.getlocation()].takeitem(target.getid())
    elif target == '' and have == False:
        return "That item is not here."
    else:
        return "That is not a valid item."

def drop(i):
    target = ''
    for k in i:
        have = True
        if k in itemtags:
            have = False
            tag = k
        for j in gl.player.getinv():
            if k.lower() in gl.itemdict[j].gettags():
                target = gl.itemdict[j]
                have = True
    if target != '' and have == True:
        return gl.player.dropitem(target.getid())
    elif target == '' and have == False:
        return "That item is not in your inventory."
    else:
        return "That is not a valid item."

def checkinv(i):
    s = "Your inventory contains: \n"
    for i in gl.player.getinv():
        s+= gl.itemdict[i].getname() + ", \n"
    return s
def open(i):
    target = ''
    for k in i:
        for j in gl.roomdict[gl.player.getlocation()].getcontainers():
            if k in gl.containerdict[j].gettags():
                target = gl.containerdict[j]
    return target.open()