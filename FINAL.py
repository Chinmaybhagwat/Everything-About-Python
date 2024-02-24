# Author: Chinmay Bhagwat
# Project: Tic-Tac-Toe for AAI551

import time  # import the time module for time-related functions
import random  # import the random module for generating random values

# define a function to create an empty game board

def create_board():
    return [[' ' for i in range(3)] for j in range(3)]

# define a function to print the game board

def print_board(board):

    # print the column numbers
    print("   0   1   2")
    print("  --- --- ---")

    # loop through each row and column of the board and print the values
    for i in range(len(board)):
        print(i, end=" ")
        for j in range(len(board[0])):
            print("|", board[i][j], end="")
        print("|")
        print("  --- --- ---")

# define a function to check if a player has won the game

def check_winner(board, player):
    # check rows for winning condition
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != player:
                break
        else:
            return True
    # check columns for winning condition
    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] != player:
                break
        else:
            return True

    # check diagonals for winning condition
    for i in range(len(board)):
        if board[i][i] != player:
            break
    else:
        return True

    for i in range(len(board)):
        if board[i][len(board)-i-1] != player:
            break
    else:
        return True
    # if no winning condition is found, return False
    return False

# define a function for the AI's turn
def ai_turn(board, ai_player, player):
    print("AI is thinking...")

    time.sleep(2)  # wait for 2 seconds to simulate thinking
    # check for a winning move

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                board[i][j] = ai_player
                if check_winner(board, ai_player):
                    print_board(board)
                    print("AI wins!")
                    return True
                board[i][j] = ' '
    # check for a blocking move

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                board[i][j] = player
                if check_winner(board, player):
                    board[i][j] = ai_player
                    print_board(board)
                    return False
                board[i][j] = ' '
    # take the center spot if available

    if board[1][1] == ' ':
        board[1][1] = ai_player
        print_board(board)
        return False
    # take a random spot if all else fails
    empty_spots = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_spots.append((i,j))
    row, col = random.choice(empty_spots)
    board[row][col] = ai_player
    print_board(board)
    return False

# define a function for the player's turn

def player_turn(board, player):
    # Prompts the player for their turn and checks if it is valid
    # Returns True if the game should end, False otherwise

    print("Player", player, "turn.")
    start_time = time.time()
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    elapsed_time = time.time() - start_time

    if elapsed_time > 10:
        print("Time's up! You exceeded the time limit.")
        return False

    if board[row][col] == ' ':
        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print("Player", player, "wins!")
            return True

        if all(' ' not in sublist for sublist in board):
            print("It's a tie!")
            return True
        return False

    else:
        print("That spot is already taken. Try again")
        return False


def play_game():
    # Initializes the game, alternates turns between the player and AI
    # Exits the loop when the game is over

    board = create_board()
    print_board(board)
    players = ['X', 'O']
    current_player = players[0]
    while True:
        if current_player == players[0]:
            if player_turn(board, current_player):
                break
        else:
            if ai_turn(board, current_player, players[0]):
                break
        if check_winner(board, current_player):
            break
        if all(' ' not in sublist for sublist in board):
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]


play_game()

# Below is the same program done using OOP. I used class and functions are same

''' class TicTacToe:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.players = ['X', 'O']
        self.current_player = self.players[0]

    def print_board(self):
        print("   0   1   2")
        print("  --- --- ---")
        for i in range(len(self.board)):
            print(i, end=" ")
            for j in range(len(self.board[0])):
                print("|", self.board[i][j], end="")
            print("|")
            print("  --- --- ---")

    def check_winner(self, player):
        for i in range(len(self.board)):
            if all(x == player for x in self.board[i]):
                return True
        for j in range(len(self.board[0])):
            if all(x == player for x in [self.board[i][j] for i in range(len(self.board))]):
                return True
        if all(self.board[i][i] == player for i in range(len(self.board))):
            return True
        if all(self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))):
            return True
        return False

    def player_turn(self):
        print("Player", self.current_player, "turn.")
        start_time = time.time()
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        elapsed_time = time.time() - start_time
        
        if elapsed_time > 10:
            print("Time's up! You exceeded the time limit.")
            return False
        
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.print_board()
            if self.check_winner(self.current_player):
                print("Player", self.current_player, "wins!")
                return True
            if all(' ' not in sublist for sublist in self.board):
                print("It's a tie!")
                return True
            return True  # Indicate successful move
            
        else:
            print("That spot is already taken. Try again")
            return False

    def ai_turn(self):
        print("AI is thinking...")
        time.sleep(2)


        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.players[1]
                    if self.check_winner(self.players[1]):
                        self.print_board()
                        print("AI wins!")
                        return True
                    self.board[i][j] = ' '


        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.players[0]
                    if self.check_winner(self.players[0]):
                        self.board[i][j] = self.players[1]
                        self.print_board()
                        return False
                    self.board[i][j] = ' '


        if self.board[1][1] == ' ':
            self.board[1][1] = self.players[1]
            self.print_board()
            return False


        empty_spots = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    empty_spots.append((i, j))
        row, col = random.choice(empty_spots)
        self.board[row][col] = self.players[1]
        self.print_board()
        return False

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()
        while True:
            if self.current_player == 'X':
                while not self.player_turn():
                    pass
            else:
                if self.ai_turn():
                    break
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]
            print()
            if all(' ' not in sublist for sublist in self.board):
                print("It's a tie!")
                break
            if self.check_winner(self.current_player):
                print("Player", self.current_player, "wins!")
                break


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
'''