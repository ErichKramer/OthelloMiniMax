'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''
from Board import * 



class OthelloBoard(Board):
    def __init__(self, rows, cols, p1, p2):
        Board.__init__(self, rows, cols)
        self.p1_symbol = p1
        self.p2_symbol = p2


    #this function is substitute for clone. call as New = Old.cloneOBoard()
    def cloneOBoard(self):
        tmp = OthelloBoard(self.cols, self.rows, self.p1_symbol, self.p2_symbol)
        tmp.grid = copy.deepcopy(self.grid)
        return tmp;

    def initialize(self):
        Board.set_cell(self.cols /2 -1, self.rows /2 -1, p1_symbol)
        Board.set_cell(self.cols /2, self.rows /2, p1_symbol)
        Board.set_cell(self.cols /2 -1, self.rows /2 , p2_symbol)
        Board.set_cell(self.cols /2, self.rows /2 -1, p2_symbol)

