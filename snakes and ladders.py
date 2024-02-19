import random

board_size = 10
computer = 'c'
user = 'u'
EMPTY='-'
z='0'

def create_board():
    board1 = []
    temp = []
    for i in range(100, 0, -1):
        temp.append(str(i).zfill(2))
        if (i - 1) % 10 == 0:
            board1.append(temp)
            temp = []
    for j in range(len(board1)):
        if j % 2:
            board1[j].reverse()
    return board1

def print_board(num1, coin1, num2, coin2):
    board = create_board()
    if num1 <= 10:
        if num1 == 0:
            board[9][num1] = EMPTY
        else:
            board[9][num1 - 1] = coin1
    elif num1 <= 20:
        board[8][20 - num1] = coin1
    elif num1 <= 30:
        board[7][num1 - 21] = coin1
    elif num1 <= 40:
        board[6][40 - num1] = coin1
    elif num1 <= 50:
        board[5][num1 - 41] = coin1
    elif num1 <= 60:
        board[4][60 - num1] = coin1
    elif num1 <= 70:
        board[3][num1 - 61] = coin1
    elif num1 <= 80:
        board[2][80 - num1] = coin1
    elif num1 <= 90:
        board[1][num1 - 81] = coin1
    elif num1 <= 100:
        board[0][100 - num1] = coin1

    if num2 <= 10:
        if num2 == 0:
            board[9][num2] = EMPTY
        else:
            board[9][num2 - 1] = coin2
    elif num2 <= 20:
        board[8][20 - num2] = coin2
    elif num2 <= 30:
        board[7][num2 - 21] = coin2
    elif num2 <= 40:
        board[6][40 - num2] = coin2
    elif num2 <= 50:
        board[5][num2 - 41] = coin2
    elif num2 <= 60:
        board[4][60 - num2] = coin2
    elif num2 <= 70:
        board[3][num2 - 61] = coin2
    elif num2 <= 80:
        board[2][80 - num2] = coin2
    elif num2 <= 90:
        board[1][num2 - 81] = coin2
    elif num2 <= 100:
        board[0][100 - num2] = coin2
    for row in range(len(board)):
        print(*board[row])
    print('\n')

    board = create_board()


def snakes_and_ladders():
    computer = 'C'
    user = 'U'
    print("\n\t\tWELCOME TO GAME OF SNAKES AND LADDERS\n\n")
    print("About the game:\n")
    print("It is played with dice between two players and here it will be with user and computer\n")
    print("SNAKES : if you land on a number and it is prime go to the previous prime number\n")
    print("LADDER : if you land on a perfect square number, you will ladder up by its square root of a number\n")
    print("Let's start the game\n")

    def check_snake_or_ladder(n):
        snakes = {11: 9, 13: 11, 17: 13, 19: 17, 23: 19, 29: 23, 31: 29, 37: 31, 41: 37, 43: 41, 47: 43, 53: 47, 59: 53,
                  61: 59, 67: 61, 71: 67, 73: 71, 79: 73, 83: 79, 89: 83, 97: 89}
        ladder = {4: 14, 9: 12, 16: 26, 25: 34, 36: 48}
        if n in snakes.keys():
            print("Oops!it is a snake:")
            n = snakes[n]

        elif n in ladder.keys():
            print("Woah!it is a ladder.")
            n = ladder[n]
        return n

    def random_num():
        num = random.randint(1, 6)
        return num

    def roll_dice(pos):
        z = 0
        z = random_num()
        print("On dice:", z)
        pos = pos + z
        pos = check_snake_or_ladder(pos)
        return pos

    pos_1 = 0
    pos_2 = 0
    while pos_1 < 100 or pos_2 < 100:
        print("Turn of user")
        result = input("Press enter")
        if result == "":
            pos_1 = roll_dice(pos_1)
            print("Position of user is:", pos_1, ",computer:", pos_2)
            print_board(pos_1, user, pos_2, computer)
            if pos_1 > 99:
                print("\t\tUSER IS WINNER")
                break
        print("Turn of computer")
        pos_2 = roll_dice(pos_2)
        print("Position of computer is:", pos_2, ",user:", pos_1)
        print_board(pos_1, user, pos_2, computer)
        if pos_2 > 99:
            print("COMPUTER IS WINNER\n")
            print("Better luck next time")
            break


snakes_and_ladders()