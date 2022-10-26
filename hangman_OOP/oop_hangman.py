
import random, time
import os
from game_pkg.ascii import logo, stages, sore_loser, winner
from game_pkg.word_set import word_set

class Hangman:
    def __init__(self):
        self.flag = True
        print(logo)
        print("You have 6 tries to guess all letters in the word")

        self.lives_left = 6
        self.display = []
        return None
    
    def random_word(self):
        chosen_word = random.choice(word_set)
        self.chosen_word = chosen_word
        print(f'Psst, the solution is {self.chosen_word}.\n') #test code, gives solution
        
    def display_hidden_word(self):
        self.display = ["_" for letter in self.chosen_word]
        print(' '.join(self.display))
        return None

 # prints display and the hangman stage based on the index of lives_left
    def show_hangman(self):
        print(stages[self.lives_left])

    def guess_letter(self):
        try:
            guess = input("Guess a letter: ").lower()
        except TypeError: print("Sorry! Please type in a letter!: ")
        self.guess = guess

    #Checks if letter guessed is in word and if there are lives_left 
    def check_guess(self):
        self.already_guessed()
        if self.guess not in self.chosen_word:
            self.lives_left -= 1
            print(f"\nYou lost a life! Letter {self.guess} is not in the word. Lives left:{self.lives_left} \n")
            self.update_display()

    def already_guessed(self):
        if self.guess in self.display:
            print(f"\nYou already guessed {self.guess}")

    def update_display(self):
        for index, value in enumerate(self.chosen_word):
            if value == self.guess:
                self.display[index] = self.guess
        return (f"{' '.join(self.display)}")

    def life_status(self):
        if (self.lives_left)!=1:
            print("\nYou have {0} lives left".format(self.lives_left))
        else:
            print("\nYou have {0} lives left".format(self.lives_left))
        return self.lives_left

    def check_for_win_lose(self):
        display = ' '.join(self.display)
        if not "_" in display: # if there are no more underscores than all letters are solved and you guessed the word
            print(winner)
            return True
        if self.lives_left == 0: # you lose
            self.flag = False
            print("\nGAME OVER! \n", sore_loser) 
    
    # def loop(self):
        new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
        if new_game[0].lower() == 'y':
            cls()
            return self.flag == True
        else: 
            cls()
            print("Thanks for playing!")
    
## Functions ##
def cls():
    os.system('cls' if os.name == 'nt' else 'clear') 


game = Hangman()

while game.flag==True:
    game.random_word
    game.display_hidden_word
    game.show_hangman

    while (game.lives_left) > 0:
        game.guess_letter
        game.check_guess

