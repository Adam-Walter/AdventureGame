#import module to work with .json files
import json
#create dictionarys to hold all of the objects within the game in an easily referenceable way
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
#the class for creating the player object and their attributtes, as well as methods to manipulate their data as needed to achieve game actions
class Player:
    def __init__(self,location,health,inv):
        self.__location = location
        self.__health = health
        self.__inv = inv
    def getlocation(self):
        return self.__location
    def gethealth(self):
        return self.__health
    def getinv(self):
        return self.__inv
    def changelocation(self,d):
        self.__location = d
    def giveitem(self,item):
        self.__inv.append(item)
    def dropitem(self,item):
        self.__inv.remove(item)
        roomdict[self.__location].additem(item)
        return "You dropped the " + itemdict[item].getname() + ".  "
    def damage(self,d):
        self.__health -= d
#the class for creating the rooms and their attributtes, as well as methods to manipulate their data as needed to achieve game actions
class Room:
    def __init__(self,id,name,description,inv,containers,npcs,exits):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__inv = inv
        self.__containers = containers
        self.__npcs = npcs
        self.__exits = exits
    def getid(self):
        return self.__id
    def getname(self):
        return self.__name
    def getdescription(self):
        return self.__description
    def getinv(self):
        return self.__inv
    def getcontainers(self):
        return self.__containers
    def getnpcs(self):
        return self.__npcs
    def getexits(self):
        return self.__exits
    def killnpc(self,npc):
        self.__npcs.remove(npc)
    def move(self,p,d):
        valid = False
        for i in self.__exits:
            if exitdict[i].getdirection() == d:
                p.changelocation(exitdict[i].getfinish())
                valid = True
        if valid == True:
            return "You travel to the " + d + "."
        else:
            return "There is no clear path to the " + d + "." 
    def takeitem(self,item):
        if item in self.__inv:
            self.__inv.remove(item)
        else:
            b = False
            for i in self.__containers:
                if containerdict[i].getopen() == True:
                    if item in containerdict[i].getinv():
                        containerdict[i].remove(item)
                        b = True
                if b == True:
                    break
        player.giveitem(item)
        return "You take the " + itemdict[item].getname() + ".  "
    def additem(self,item):
        self.__inv.append(item)
#the class for creating the exits to rooms and their attributtes
class Exit:
    def __init__(self,id,start,finish,description,direction):
        self.__id = id 
        self.__start = start
        self.__finish = finish
        self.__description = description
        self.__direction = direction
    def getid(self):
        return self.__id
    def getstart(self):
        return self.__start
    def getfinish(self):
        return self.__finish
    def getdescription(self):
        return self.__description
    def getdirection(self):
        return self.__direction
#the object for creating the various items and their attributtes
class Item:
    def __init__(self,id,name,description,damage,tags):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__damage = damage
        self.__tags = tags
    def getid(self):
        return self.__id
    def getname(self):
        return self.__name
    def getdescription(self):
        return self.__description
    def getdamage(self):
        return self.__damage
    def gettags(self):
        return self.__tags
#the object for creating the containers and their attributtes, as well as methods to manipulate their data as needed to achieve game actions
class Container:
    def __init__(self,id,name,description,inv,open,key,tags):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__inv = inv
        self.__open = open
        self.__key = key
        self.__tags = tags
    def getid(self):
        return self.__id
    def getname(self):
        return self.__name
    def getdescription(self):
        return self.__description
    def getinv(self):
        return self.__inv
    def getopen(self):
        return self.__open
    def getkey(self):
        return self.__key
    def gettags(self):
        return self.__tags
    def open(self):
        self.__open = True
        return "You open the " + self.__name + ".  "
    def remove(self,item):
        self.__inv.remove(item)
#the object for creating the npcs and their attributtes, as well as methods to manipulate their data as needed to achieve game actions
class Npc:
    def __init__(self,id,name,description,health,inv,tags):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__health = health
        self.__inv = inv
        self.__tags = tags
    def getid(self):
        return self.__id
    def getname(self):
        return self.__name
    def getdescription(self):
        return self.__description
    def gethealth(self):
        return self.__health
    def getinv(self):
        return self.__inv
    def gettags(self):
        return self.__tags
    def damage(self,d):
        self.__health -= d
        if self.__health > 0:
            return "The " + self.__name + " takes " + str(d) + " damage!"
        else:
            roomdict[player.getlocation()].killnpc(self.__id)
            return "The " + self.__name + " takes " + str(d) + " damage, and is slain!"
#open the rooms.json file and create all the room objects from the data and add to the room dictionary
rfile = open('data/rooms.json')
data = json.load(rfile)
for i in data:
    k = data[i]
    roomdict[i] = Room(i,k['name'],k['description'],k['inv'],k['containers'],k['npcs'],k['exits'])
rfile.close()
#open the exits.json file and create all the exit objects from that data and add them to the exit dictionary 
efile = open('data/exits.json')
data = json.load(efile)
for i in data:
    k = data[i]
    exitdict[i] = Exit(i,k['start'],k['finish'],k['description'],k['direction'])
efile.close()
#open the items.json file and create all the item objects from that data and add them to the items dictionary 
ifile = open('data/items.json')
data = json.load(ifile)
for i in data:
    k = data[i]
    itemdict[i] = Item(i,k['name'],k['description'],k['damage'],k['tags'])
ifile.close()
#open the containers.json file and create all the container objects from that data and add them to the containers dictionary 
cfile = open('data/containers.json')
data = json.load(cfile)
for i in data:
    k = data[i]
    containerdict[i] = Container(i,k['name'],k['description'],k['inv'],k['open'],k['key'],k['tags'])
cfile.close()
#open the npcs.json file and create all the npc objects from that data and add them to the npc dictionary 
nfile = open('data/npcs.json')
data = json.load(nfile)
for i in data:
    k = data[i]
    npcdict[i] = Npc(i,k['name'],k['description'],k['health'],k['inv'],k['tags'])
nfile.close()
#open the player.json file and create the player object as a unique object refered to as 'player'
pfile = open('data/player.json')
data = json.load(pfile)
player = Player(data['location'],data['health'],data['inv'])
cfile.close()