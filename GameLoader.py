import json

roomdict = {
    
    }
exitdict = {
    
    }
itemdict = {
    
    }
containerdict = {
    
    }
npcdict = {
    
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
    def damage(self,d):
        self.health -= d

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
            return "You go to the " + d + "."
        else:
            return "There is nowhere to go to the " + d + "." 

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
    def __init__(self,id,name,description,inv,open,key,tags):
        self.id = id
        self.name = name
        self.description = description
        self.inv = inv
        self.open = open
        self.key = key
        self.tags = tags
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
    def gettags(self):
        return self.tags

class Npc:
    def __init__(self,id,name,description,health,inv,tags):
        self.id = id
        self.name = name
        self.description = description
        self.health = health
        self.inv = inv
        self.tags = tags
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getdescription(self):
        return self.description
    def gethealth(self):
        return self.health
    def getinv(self):
        return self.inv
    def gettags(self):
        return self.tags

rfile = open('rooms.json')
data = json.load(rfile)
for i in data:
    k = data[i]
    roomdict[i] = Room(i,k['name'],k['description'],k['inv'],k['containers'],k['npcs'],k['exits'])
rfile.close()

efile = open('exits.json')
data = json.load(efile)
for i in data:
    k = data[i]
    exitdict[i] = Exit(i,k['start'],k['finish'],k['description'],k['direction'])
efile.close()

ifile = open('items.json')
data = json.load(ifile)
for i in data:
    k = data[i]
    itemdict[i] = Item(i,k['name'],k['description'],k['tags'])
ifile.close()

cfile = open('containers.json')
data = json.load(cfile)
for i in data:
    k = data[i]
    containerdict[i] = Container(i,k['name'],k['description'],k['inv'],k['open'],k['key'],k['tags'])
cfile.close()

nfile = open('npcs.json')
data = json.load(nfile)
for i in data:
    k = data[i]
    npcdict[i] = Npc(i,k['name'],k['description'],k['inv'],k['tags'])
nfile.close()

pfile = open('player.json')
data = json.load(pfile)
player = Player(data['location'],data['health'],data['inv'])
cfile.close()