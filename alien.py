# War of the Worlds

import random

class Player(object):
    '''A player in action game'''
    def __init__(self, namestring, comesfrom):
        '''This is the constructor function '''
        self.name = namestring
        self.hometown = comesfrom
        self.alive = True
        print('\nA new hero appears in our city!')
    def speak(self):
        print('\nI am a hero, who defends the Earth...')
        print('Remember my name! It is', self.name)
        print('I come from', self.hometown)
    def shoot(self, enemy):
        print('\nThe player shoots the alien... ')
        x = random.randint(0, 10)
        if x >= 5:
            print('\nThe player hits the enemy and he will die...')    
            enemy.die()
        else:
            print('\nThe player missed... The enemy will survive!')
            enemy.survived()
    def die(self):
        print('\nThe player is hit and dies...')
        self.alive = False
        

class Alien(object):
    '''An evil creature from another Galaxy'''
    def __init__(self, namestring):
        self.name = namestring
        self.alive = True
    def speak(self):
        print('\nI came from remote Galaxy')
        print('I want to counquer you planet')
        print('Remember my name! It is', self.name)
    def die(self):
        self.alive = False
        print('\nI am hit by a blaster')
        print('I am dying...')
    def survived(self):
        print('\nThe Earther missed... I survived')
    def alienshoot(self, player):
        y = random.randint(0, 10)
        if y >= 5:
            print("\nThe alien shoots back...")
            player.die()                
        else:
            print("\nThe alien missed...")
        
## The end of classes' definitions
# Main part of the program starts here
print('---- War of worlds Game ----')

hero = Player('George', 'Leeds')
hero.speak()

#anotherhero = Player('Peter', 'London')
#anotherhero.speak()

invader = Alien('first Alien')
invader.speak()

hero.shoot(invader)

if invader.alive:
    print('\nOur alien is still alive... He may shoot back!')
    invader.alienshoot(hero)
    if hero.alive:
        print('\nThe alien missed... Our hero is alive!')
    else:
        print('\nPity, but our hero is dead...')
else:
    print('\nThe alien is dead and will never return back...')


'''
Step 1. They introduce themselves

Step 2. The Player shoots
      |                    |
      Step 3A              |
      The Player misses    |
       |                 Step 3B
       |                 The Player hits
       |                    |
       |                    Alien dies. GAME OVER
       |
    Step 4
    The Alien shoots back
    |                     |
    Step 5A               |
    The Alien hits the    |
    Player GAME OVER      |

                         Step 5B
                         The Alien misses
                         The Player survives
                         GAME OVER
'''







        
