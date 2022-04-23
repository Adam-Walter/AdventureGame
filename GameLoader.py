roomdict = {
    
    }
exitdict = {
    
    }
itemdict = {
    
    }
containerdict = {
    
    }

class Player:
    def __init__(self,location,health,inv):
        self.location = location
        self.health = health
        self.inv = inv
    def getlocation(self):
        return self.location
    def gethealth(self):
        return self.health
    def getinv(self):
        return self.inv
    def changelocation(self,d):
        self.location = d

class Room:
    def __init__(self,id,name,description,inv,containers,npcs,exits):
        self.id = id
        self.name = name
        self.description = description
        self.inv = inv
        self.containers = containers
        self.npcs = npcs
        self.exits = exits
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getdescription(self):
        return self.description
    def getinv(self):
        return self.inv
    def getcontainers(self):
        return self.containers
    def getnpcs(self):
        return self.npcs
    def getexits(self):
        return self.exits
    def move(self,p,d):
        valid = False
        for i in self.exits:
            if exitdict[i].getdirection() == d:
                p.changelocation(exitdict[i].getfinish())
                valid = True
        if valid == True:
            return "You go " + d
        else:
            return d + " is not a valid direction to travel."

class Exit:
    def __init__(self,id,start,finish,description,direction):
        self.id = id 
        self.start = start
        self.finish = finish
        self.description = description
        self.direction = direction
    def getid(self):
        return self.id
    def getstart(self):
        return self.start
    def getfinish(self):
        return self.finish
    def getdescription(self):
        return self.description
    def getdirection(self):
        return self.direction

class Item:
    def __init__(self,id,name,description,tags):
        self.id = id
        self.name = name
        self.description = description
        self.tags = tags
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getdescription(self):
        return self.description
    def gettags(self):
        return self.tags

class Container:
    def __init__(self,id,name,description,inv,open,key):
        self.id = id
        self.name = name
        self.description = description
        self.inv = inv
        self.open = open
        self.key = key
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getdescription(self):
        return self.description
    def getinv(self):
        return self.inv
    def getopen(self):
        return self.open
    def getkey(self):
        return self.key

with open ("rooms.txt", "r") as roomfile:
    line = roomfile.readline()
    while line != '':
        items = line.split(',')
        roomdict[items[0]] = Room(items[0],items[1],items[2],items[3].split(' '),items[4].split(' '),items[5].split(' '),items[6].split(' '))
        line = roomfile.readline()
with open ('exits.txt', 'r') as exitfile:
    line = exitfile.readline()
    while line != '':
        items = line.split(',')
        exitdict[items[0]] = Exit(items[0],items[1],items[2],items[3],items[4])
        line = exitfile.readline()
with open ('items.txt', 'r') as itemfile:
    line = itemfile.readline()
    while line != '':
        items = line.split(',')
        itemdict[items[0]] = Item(items[0],items[1],items[2],items[3].split(' '))
        line = itemfile.readline()
with open ("containers.txt", "r") as containerfile:
    line = containerfile.readline()
    while line != '':
        items = line.split(',')
        containerdict[items[0]] = Container(items[0],items[1],items[2],items[3].split(' '),items[4],items[5])
        line = containerfile.readline()
with open ('player.txt', 'r') as playerfile:
    line = playerfile.readline()
    items = line.split(',')
    player = Player(items[0],items[1],items[2].split(' '))
