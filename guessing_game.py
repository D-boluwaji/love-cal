import random
def guessing_game ():
    """A guessing game to guess the first and last number in a list of numbers"""
    print("Guess two numbers between 1-9 \n If you're tired input 00 in any to quit")
    numbers = [1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
   # print(numbers[0], numbers[-1]) #to know the answer uncomment this
    count = 0
    won = True
    while True:
        try:
            guessed_value = int(input("Guess my first number: "))
            guessed_value2 = int(input("Guess my last number: "))
            if guessed_value == numbers[0] and guessed_value2 == numbers[-1]:
                won = True
                break
            elif guessed_value == 00 or guessed_value2 == 00:
                won = False
                break
            else:
                count+=1
        except:
            print("Input an integer!")
        
    if won:
        print(f"Game Over \n You guessed correctly after {count} attempts")
    else:
        print(f"Game Over \n You didn't guess correctly after {count} attempts")


guessing_game()
