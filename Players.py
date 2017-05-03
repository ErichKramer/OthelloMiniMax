'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol():
        return self.symbol
    
    #parent get_move should not be called
    def get_move():
        raise NotImplementedError()



class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol);

    def clone():
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference
    def get_move():
        col = input("Enter col:")
        row = input("Enter row:")
        return  (col, row)


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol);


    def clone():
        return MinimaxPlayer(self.symbol);


    def get_move():
        #This implementation has been excluded
        return None

