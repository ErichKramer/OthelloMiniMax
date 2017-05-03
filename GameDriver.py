'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''
from Players import *
import sys
import OthelloBoard


class GameDriver:
    def __init__(self, p1type, p2type, num_rows, num_cols):
        if p1type in "human":
            self.p1 = HumanPlayer('X')

        elif p1type in "minimax" or p1type in "ai":
            self.p1 = MinimaxPlayer('X')

        else:
            print("Invalid player 1 type!")
            exit(-1)

        if p2type in "human":
            self.p2 = HumanPlayer('O')

        elif p2type in "minimax" or p1type in "ai":
            self.p2 = MinimaxPlayer('O')

        else:
            print("Invalid player 2 type!")
            exit(-1)

        self.board = OthelloBoard.OthelloBoard(num_rows, num_cols, self.p1.symbol, self.p2.symbol)

    def display(self):
        print("Player 1 (", self.p1.symbol, ") score: ", \
                self.board.count_score(self.p1.symbol), "\n")

    def process_move(self, curr_player, opponent):
        invalid_move = True
        while(invalid_move):
            (col, row) = curr_player.get_move(self.board)
            if( not board.is_legal_move(col, row, curr_player.symbol)):
                print("Invalid move")
            else:
                print("Move: Col=", col, " Row=", row)
                board.play_move(col,row,curr_player.symbol)
                return;


    def run(self):
        self.board.initialize();
        self.board.display();
        curr = self.p1
        opponent = self.p2

        print("This is where the game code would go, IF I HAD ANY")


def main():
    if(len(sys.argv)) != 3:
        print("Usage: python3 GameDriver.py <player1 type> <player2 type>")
        exit(-1)
    game = GameDriver(sys.argv[1], sys.argv[2], 4, 4)
    game.run();
    return 0


main()
