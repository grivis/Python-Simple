class Gamepiece(object):
    types = ['Paper', 'Scissors','Rock']
    def __init__(self, typeid):
        self.type = Gamepiece.types[typeid]
    def __str__(self):
        return self.type                                               

class Gamepot(object):
    def fill(self, pieces):
        self.content = pieces
    def __str__(self):
        strings = []
        for item in self.content:
            strings.append(str(item))
        return 'Pot now contains: ' + ' '.join(strings)
    def rempiece(self, pieceid):
            self.content.pop(pieceid)


class Player(object):
    def __init__(self, name):
        self.name = name
    def takepiece(self, pot, pieceid):
        self.holds = pot.content[pieceid]
        pot.rempiece(pieceid)
    def takerandom(self, pot):
        x = random.randrange(len(pot.content))
        self.holds = pot.content[x]
        pot.rempiece(x)
        
        #######
    def __str__(self):
        return str(self.holds)

#### Main program starts here

pieces = [Gamepiece(0), Gamepiece(1), Gamepiece(2)]

##
import random
name = input("What is your name? ")
rps = int(input("Ok " + name + " , would you like to be Paper(0), Scissors(1) or Rock(2)? "))
    

pot = Gamepot()
pot.fill(pieces)
#print(pot)

person = Player(name)
person.takepiece(pot, rps)
#print(pot)
#print(person)

robot = Player('Robby')
robot.takerandom(pot)

print("You chose", str(person),  "and the A.I. chose",  str(robot))
if str(person) == "Scissors" and str(robot) == "Rock":
    print("Unlucky, ", name, " the A.I. won this time! ")
elif str(person) == "Rock" and str(robot) == "Scissors":
    print("Well done! ", name, " you have won this time! ")
elif str(person) == "Rock" and str(robot) == "Paper":
    print("Unlucky, ", name, " the A.I. won this time! ")
elif str(person) == "Scissors" and str(robot) == "Paper":
    print("Well done! ", name, " you have won this time! ")
elif str(person) == "Paper" and str(robot) == "Rock":
    print("Well done! ", name, " you have won this time! ")
elif str(person) == "Paper" and str(robot) == "Scissors":
    print("Unlucky, ", name, " the A.I. won this time! ")






    
    



