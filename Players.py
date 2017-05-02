'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        return False

    def get_symbol():
        return self.symbol
    
    def get_move():
        raise NotImplementedError()




class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol);
        return False

    def clone():
        return HumanPlayer(self.symbol)
        

#ERICH NOTE: FINISH HUMAN GET MOVE BEFORE PUBLIC RELEASE    
    def get_move():
        col = input("Enter col:")
        row = input("Enter row:")


class MinimaxPlayer(Player):
    def __init__(self):
        Player.__init__(self, symbol);
        return False

    def clone():
        return MinimaxPlayer(self.symbol);

    def get_move():
        #This implementation has been excluded
        return None

