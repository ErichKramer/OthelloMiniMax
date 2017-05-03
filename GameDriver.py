import sys
import OthelloBoard


class GameDriver:
    def __init__(self, p1type, p2type, num_rows, num_cols):
        if p1type in "human":
            4+4
            #make it a human player object
        elif p1type in "minimax" or p1type in "ai":
            4+4
            #make it a minimax player
        else:
            print("Invalid player 1 type!")
            exit(-1)

        if p2type in "human":
            4+4
            #make it a human player object
        elif p2type in "minimax" or p1type in "ai":
            4+4#make it a minimax player
        else:
            print("Invalid player 2 type!")
            exit(-1)
        print("Recieved : ", p1type, " ", p2type);

        self.board = OthelloBoard.OthelloBoard(num_rows, num_cols, 'X', 'O')

    def run(self):
        print("This is where the game code would go, IF I HAD ANY")


def main():
    if(len(sys.argv)) != 3:
        print("Usage: python3 GameDriver.py <player1 type> <player2 type>")
        exit(-1)
    game = GameDriver(sys.argv[1], sys.argv[2], 4, 4)
    game.run();
    return 0


main()
