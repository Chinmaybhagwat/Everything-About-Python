import time
import random


class TicTacToe:
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

        # Check if AI can win in the next move
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.players[1]
                    if self.check_winner(self.players[1]):
                        self.print_board()
                        print("AI wins!")
                        return True
                    self.board[i][j] = ' '

        # Check if opponent can win in the next move and block them
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.players[0]
                    if self.check_winner(self.players[0]):
                        self.board[i][j] = self.players[1]
                        self.print_board()
                        return False
                    self.board[i][j] = ' '

        # Place a move in the center if it's available
        if self.board[1][1] == ' ':
            self.board[1][1] = self.players[1]
            self.print_board()
            return False

        # Otherwise, choose a random empty spot on the board
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


