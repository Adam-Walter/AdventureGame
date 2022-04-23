import GameLoader as gl

commanddict = {
    'go' : 'move',
    'walk' : 'move',
    'run' : 'move',
    'attack' : 'attack'
    }
itemtags = ['sword','blade','longsword','shortsword']

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
            for k in i:
                if k in ['north','south','east','west']:
                    target = k
                    return gl.roomdict[gl.player.getlocation()].move(gl.player,target)
            if target == '':
                return "I'm sorry I don't understand where you want to move to."
        if commandtype == 'attack':
            for k in i:
                have = True
                if k in itemtags:
                    have = False
                    tag = k
                    for j in gl.player.getinv():
                        if j != '0': 
                            if k.lower() in gl.itemdict[j].gettags():
                                argument = gl.itemdict[j]
                                have = True
            if argument != '' and have == True:
                return 'You attack with the ' + argument.getname()
            elif have == True:
                return 'You attack with your fists!'
            else:
                return 'You do not have a ' + tag
                        
    else:
        return "I'm sorry, that command was not valid."

