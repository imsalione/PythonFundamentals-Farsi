import random

name = input("What's your name? ")

print("Good luck! ", name)

words = ['perspolis', 'esteghlal', 'iran', 'shiraz', 'python'
         'water', 'reverse', 'shaah', 'love', 'player', 'computer'
         'windows', 'ninja', 'ali daee', 'ali karimi', 'saleh']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
            
    if failed == 0:
        print("You Win!!!")
        print("The word is: ", word)
        break
    
    print()
    guess = input("guess a character: ")
    
    guesses += guess
    
    if guess not in word:
        turns -= 1
        
        print("Wrong")
        
        print("You have", + turns, 'more guesses!')
        
        if turns == 0:
            print("You loose :(")
        