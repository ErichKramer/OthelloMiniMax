'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.


    FILE.PY: This exists as a demo of the Board object
'''

from Board import Board



x = Board(15, 15);


x.set_cell( 4, 4, 'x')

x.set_cell( 1, 3, 'B')


x.display()

y = x.cloneBoard();
y.display();

