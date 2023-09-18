import random
class Hangman: 
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find= random.choice(self.possible_words)
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.lives = 5
        self.error_count = 0
        self.turn_count = 0

    
    def display_letter(self):

        display = ""
        for letter in  self.word_to_find :
            if letter in self.correctly_guessed_letters:
                display += letter
            else:
                display += "_"

        return display

    

    def play(self):

        #display_letter()

        self.word_completion = ['_' ]* len( self.word_to_find)
        self.gussed = False
        self.gussed_letter = []
        self. gussed_word = []

  

        while self.lives > 0:

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in self.correctly_guessed_letters:
                print("You already guessed that letter.")
                continue

            self.correctly_guessed_letters.append(guess)

            if guess in self.word_to_find:
                print("good gusse")
            else:
                self.lives -= 1
                print(f"Wrong guess! You have {self.lives} lives left.")
            self.wrongly_guessed_letters.append(guess)
   
           # print(current_display)

        if self.correctly_guessed_letters == self.word_to_find:
                
            self.well_played()

        4
      

        if self.correctly_guessed_letters != self.word_to_find:
                
            self.game_over()

            print("`bad_guessed_letter " + self.word_to_find)

    def start_game(self):

        self.play()

        print("welcome to hangman game ")

    def well_played(self):

        return print("You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!")
       

    def game_over(self):
                
           
     return print("game over")
    
Hangman().start_game()




                

        


        
    


        