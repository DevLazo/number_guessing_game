import random
import time
random_number=random.randint(1,100) #Generates random number between 1 and 100      
print('Welcome to the Number Guessing Game!')      
time.sleep(1)                      
print("I'm thinking of a number between 1 and 100") 
time.sleep(1)
print("""Please select your difficulty level:
      
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
      
      """)
time.sleep(1)

def easy(): # Logic for easy mode
    attempts=0
    e = 10
    while True:
        easy_input=int(input("Enter your guess: "))
        if easy_input > random_number:
            print('Incorrect! The number is less than', easy_input )
            e -= 1
            attempts += 1
            easy_input
        elif easy_input < random_number:
            print('Incorrect. The number is greater than', easy_input)
            e -= 1
            attempts += 1
            easy_input
        elif easy_input == random_number:
            print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
            break
        if e == 0:
            print('You have run out of guesses!')
            print('Random number was', random_number)
            break
def medium(): #Logic for medium mode
    attempts=0
    m = 5
    while True:
        medium_input=int(input("Enter your guess: "))
        if medium_input > random_number:
            print('Incorrect! The number is less than', medium_input )
            m -= 1
            attempts += 1
            medium_input
        elif medium_input < random_number:
            print('Incorrect. The number is greater than', medium_input)
            m -= 1
            attempts += 1
            medium_input
        elif medium_input == random_number:
            print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
            break
        if m == 0:
            print('You have run out of guesses!')
            print('Random number was', random_number)
            break
def hard(): #logic for hard mode
    attempts=0
    h = 3
    while True:
        hard_input=int(input("Enter your guess: "))
        if hard_input > random_number:
            print('Incorrect! The number is less than', hard_input )
            h -= 1
            attempts += 1
            hard_input
        elif hard_input < random_number:
            print('Incorrect. The number is greater than', hard_input)
            h -= 1
            attempts += 1
            hard_input
        elif hard_input == random_number:
            print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
            break
        if h == 0:
            print('You have run out of guesses!')
            print('Random number was', random_number)
            break

while True:
    difficulty=int(input('Enter your choice: ')) #difficulty selection loop
    if difficulty == 1:
        print("""Great! You have selected the Easy difficulty level.
Let's start the game!""")
        easy()
        break   
    elif difficulty == 2:
        print("""Great! You have selected the Medium difficulty level.
Let's start the game!""")
        medium()
        break
    elif difficulty == 3:
        print("""Great! You have selected the Hard difficulty level.
Let's start the game!""")
        hard()
        break
    else:
        print('Please select a difficulty')
        difficulty


