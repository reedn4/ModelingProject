from SudokuStruct import Sudoku

row1 = [1, 5, '_', '_', 4, 2, '_', '_', 6]
row2 = [2, 7, 4, 5, 6, '_', '_', 1, '_']
row3 = ['_', '_', 6, '_', '_', 7, 4, '_', 2]
row4 = ['_', 1, '_', '_', '_', '_', '_', 4, '_']
row5 = ['_', '_', '_', '_', 5, '_', '_', '_', '_']
row6 = ['_', 6, '_', 4, '_', 3, 1, 9, '_']
row7 = ['_', 2, '_', 6, '_', 5, 9, '_', '_']
row8 = [9, 8, 5, '_', 3, '_', '_', 6, '_']
row9 = ['_', 4, '_', 2, 1, 9, 8, 3, '_']
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', '_', '_', '_', '_', '_', '_', 8, '_']
row2 = [6, 8, '_', 4, 7, '_', '_', 2, '_']
row3 = ['_', 1, 9, 5, '_', 8, 6, 4, 7]
row4 = ['_', 6, '_', 9, '_', '_', '_', '_', 4]
row5 = [3, 4, 2, 6, 8, '_', '_', '_', '_']
row6 = [1, 9, '_', '_', 5, '_', 8, 3, '_']
row7 = ['_', '_', '_', 7, 2, '_', 4, '_', 3]
row8 = ['_', '_', 6, '_', '_', 5, '_', 1, '_']
row9 = ['_', '_', 3, 8, 9, 1, 5, '_', '_']
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', 8, '_', 9, '_', '_', '_', 5, '_']
row2 = [4, '_', '_', 6, 5, '_', 9, 1, 3]
row3 = ['_', '_', 5, 4, '_', '_', '_', '_', '_']
row4 = [1, '_', 2, '_', 6, 5, '_', '_', '_']
row5 = [7, '_', 4, '_', '_', '_', 5, '_', 8]
row6 = ['_', '_', '_', '_', '_', '_', '_', '_', 2]
row7 = [3, '_', '_', '_', '_', 1, '_', '_', 6]
row8 = [8, 7, '_', '_', '_', '_', '_', 4, '_']
row9 = ['_', 5, '_', '_', 4, '_', 8, '_', 1]
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

row1 = ['_', '_', '_', '_', '_', '_', 8, '_', '_']
row2 = ['_', '_', '_', '_', '_', 2, '_', 7, 4]
row3 = ['_', '_', 7, '_', '_', 8, '_', 2, '_']
row4 = ['_', '_', 8, 3, 4, 5, '_', 9, '_']
row5 = ['_', '_', 3, '_', '_', 6, '_', '_', 1]
row6 = [6, '_', '_', 8, '_', '_', '_', '_', '_']
row7 = ['_', 2, 4, 9, '_', 3, 6, '_', 8]
row8 = ['_', 1, 9, '_', '_', '_', '_', '_', '_']
row9 = ['_', '_', '_', '_', 5, 4, 9, '_', '_']
lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

sud = Sudoku(lst)
# print(sud.display())
# print(sud.single)
# print(sud.displayG())
sud.nSing()
# print(sud.display())
# print(sud.displayG())
sud.hSing()
sud.nSing()
# print(sud.display())
# print(sud.displayG())
# sud.nSing()
# sud.hSing()
# sud.pointPair()
# print(sud.displayG())
# print(sud.displayG())
# print(sud.single)
print(sud.displayG())
sud.claimPair()
print(sud.display())