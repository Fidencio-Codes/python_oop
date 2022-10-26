import random
import os

word_set = ('abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# stages in descending order to match the number of lives

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Having fun with the winner/loser logos
sore_loser = "\n(⋟﹏⋞) *ANGER* \n\n(╯°□°╯︵ ┻━┻ *flips table*"
winner = "\nWho's a winner? (☞ﾟ∀ﾟ)☞ You are! \n\nᕕ(⌐■_■)ᕗ ♪♬"

class Game:
    def __init__(self):
        self.flag = True
        print(logo)
        print(print("You have 6 tries to guess all letters in the word"))
        
        self.display = []
        self.lives_left = 6
        return None
    
    #Instance method
    def random_word(self):
        chosen_word = random.choice(word_set)
        self.chosen_word = chosen_word
        # Test Code, gives solution
        print(f'Psst, the solution is {self.chosen_word}.\n')

    #Instance method
    def display_board(self): #init asterisko
        self.display = ["_" for letter in self.chosen_word]
        print(''.join(self.display))
        return None
    
    def life_status(self):
        if (self.lives_left)!=1:
            print("\nTienes {0} vidas".format(self.vidas))
        else:
            print("\nTienes {0} vida".format(self.vidas))

        return self.vidas
    
    def letter(self):
        """
        Gets a letter from the user.
        
        Returns:
            letra: an alphabetic character
        """
        #Pedir la letra
        letra=str(input("Escribe una letra: "))
        letra=letra.lower() #Pasarla a minuscula por cualquier cosa
        self.letra=letra
        
        return None
    
    def play(self):
        #Evaluar si efectivamente es un solo caracter alfabético
        if  len(self.letra)>1 or len(self.letra)==0:
            print("\t\nOJO. Introduciste más de un caracter o ninguno.\nDebes escribir un caracter a la vez. (-1 de vida)\n")
            self.vidas=self.vidas - 1
        elif (self.letra).isalpha()==False:
            print("\t\nOJO. Introduciste un caracter que no pertenece al alfabeto. (-1 de vida)\n")
            self.vidas=self.vidas - 1
        elif self.letra not in self.palabra:
            print("Esa letra no está en la palabra. (-1 de vida)\n")
            self.vidas=self.vidas - 1
        else:
            print("¡Bien!") #Si acierta, imprime esto y no quita vida
            #Reemplazar los asteriscos por los caracteres ya hallados que esten en la palabra
            for index in range(len(self.palabra)):
                if self.letra==self.palabra[index]:
                    self.lista[index]=self.letra
                    
        print(''.join(self.lista)) #Imprimir el avance
        return None
    
    def win(self):
        if '*' not in self.lista: #Si adivina antes de gastar sus oportunidades, gana
            print("\n\nHaz ganado, la palabra es: {0}\n¡Felicidades!".format(self.palabra))
            if self.palabra not in self.descubiertas:
                (self.descubiertas).append(self.palabra) #Si es la primera vez que la descubre, añadirla a la lista
            return True #Si ya ganó, salir del loop
   
    def loss(self):
        if '*' in self.lista:
            print("\n\nPerdiste. :c")
        return None
    
    def descubierta(self):
        if self.palabra in self.descubiertas:
               print("\n\t>>PISTA. Ya has adivinado antes esta palabra<<") #Si ya la descubrió anteriormente, darle una pista
        if len(self.descubiertas)>0:
                print("\nTus palabras descubiertas hasta el momento son las siguientes:\n{0}".format(' '.join(self.descubiertas)))
        return None
    
    def goodbye():
        try:
            status=int(input("Jugar de nuevo?\t\nSI:presiona 1\t\nNO:presiona 0\n"))
            if status==1:
                return True
            elif status==0:
                print("\nHasta pronto...")
                return False
            else:
                print("No entendí tu respuesta, hazlo de nuevo:")
                return Game.goodbye()
        except:
            print("No entendí tu respuesta, hazlo de nuevo:")
            return Game.goodbye()
        
    def status(self):
        
        self.flag= Game.goodbye()
        
        return self.flag
    
#MAIN

juego=Game()
#statuss=juego.flag

while juego.flag==True:
    
    juego.random_word()
    juego.descubierta()
    juego.init_asteriscos()
    juego.life_counter_status()
    
    while (juego.vidas) > 0:
        
        juego.letter()
        juego.play()
        juego.life_counter_status()
        
        if juego.win()==True:
            break
        
    juego.loss()
    
    juego.status()