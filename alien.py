# Hero kills an allien

class Player(object):
    '''A player in action game'''
    def __init__(self, namestring, comesfrom):
        '''This is the constructor function '''
        self.name = namestring
        self.hometown = comesfrom
        print('\nA new hero appears in our city!')
    def speak(self):
        print('\nI am a hero, who defends the Earth...')
        print('Remember my name! It is', self.name)
        print('I come from', self.hometown)
    def shoot(self, enemy):
        print('\nPlayer shoots an enemy...')
        enemy.die()

class Alien(object):
    '''An evil creature from another Galaxy'''
    def __init__(self, namestring):
        self.name = namestring
    def speak(self):
        print('\nI came from remote Galaxy')
        print('I want to counquer you planet')
        print('Remember my name! It is', self.name)
    def die(self):
        print('\nI am hit by a blaster')
        print('I am dying...')
        
## The end of classes' definitions
# Main part of the program starts here
print('---- War of worlds Game ----')

hero = Player('George', 'Leeds')

hero.speak()

anotherhero = Player('Peter', 'London')
anotherhero.speak()

invader = Alien('first Alien')
invader.speak()

hero.shoot(invader)




        
