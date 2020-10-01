import random

def hangman():
    wrong = 0
    stages = ["",
              "______    ",
              "|        ",
              "|    |   ",
              "|    o   ",
              "|   /|\  ",
              "|   / \  ",
              "|        ",
              ]
    word_list = ["cat", "rachel", "happy", "beach", "tiger", "lake"]
    random_word = random.randint(0,5)
    word  =  word_list[random_word]
    response_letters = list(word)
    board =(["__"] * len(word))
    win = False
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a Letter:"
        guess = input(msg)
        if guess in response_letters:
              found = response_letters.index(guess)
              board[found] = guess
              response_letters[found] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0:wrong +1]))
        if "__" not in board:
            print("You Win!, it was {}!".format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You Lose! the answer was {}.".format(word))

hangman()
                     
