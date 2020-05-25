from math import floor,ceil
class Sudoku:
    def __init__(self,puz):
        # Known values of puzzle
        self.known = puz
        # Possible values for unknown cells
        self.guess = []
        # Guess cells with single value
        self.single = []
        self.initGuess()

    def getRow(self, r, c):
        # --- Returns the row containing the given cell --- #
        temp = []
        for n in range(9):
            temp += [[r, n]]
        return temp

    def getColumn(self, r, c):
        # --- Returns the column containing the given cell --- #
        temp = []
        for n in range(9):
            temp += [[n, c]]
        return temp

    def getBox(self, r, c):
        # --- Returns the box containing the given cell --- #
        temp = []
        for n in range(9):
            temp += [[3 * floor(r / 3) + ceil((n + 1) / 3) - 1, 3 * floor(c / 3) + n % 3]]
        return temp

    def initGuess(self):
        # --- Initialize values in guess  --- #
        tempF = []
        # Rows
        for r in range(9):
            temp = []
            # Columns
            for c in range(9):
                # Check if cell value is already known
                if isinstance(self.known[r][c], int):
                    temp += ["null"]
                # If cell value is not known
                else:
                    tempL = []
                    # Known numbers in the row
                    optR = self.known[r]
                    # Known numbers in the column
                    optC = [item[c] for item in self.known]
                    # Known numbers in the box
                    optS = []
                    for n in range(3*(ceil((r+1)/3)-1), 3*ceil((r+1)/3)):
                        for m in range(3*(ceil((c+1)/3)-1), 3*ceil((c+1)/3)):
                            optS += [self.known[n][m]]
                    # Full list of numbers the box can't contain
                    opt = optR + optC + optS
                    # Compare with all possibilities 1-9
                    for n in range(1, 10):
                        if n not in opt:
                            tempL += [n]
                    # Add list of possible values to guess list
                    temp += [tempL]
                    # Check if there is only a single possibility
                    if len(tempL) == 1:
                        self.single += [[r,c]]
            tempF += [temp]
        self.guess = tempF

    def fillCell(self, r, c, num):
        # --- Add cell value to known values of puzzle --- #
        # Fill cell in known list
        self.known[r][c] = num
        # Delete guess list for cell
        self.guess[r][c] = 'null'
        # Update guess list for change
        for n in range(9):
            # Row update
            rTemp = self.guess[r][n]
            if isinstance(rTemp, list):
                if num in rTemp:
                    rTemp.remove(num)
                    if len(rTemp) == 1:
                        self.single += [[r, n]]
            # Column update
            cTemp = self.guess[n][c]
            if isinstance(cTemp, list):
                if num in cTemp:
                    cTemp.remove(num)
                    if len(cTemp) == 1:
                        self.single += [[n, c]]
            # Box update
            bTemp = self.guess[3 * floor(r / 3) + ceil((n + 1) / 3) - 1][3 * floor(c / 3) + n % 3]
            if isinstance(bTemp, list):
                if num in bTemp:
                    bTemp.remove(num)
                    if len(bTemp) == 1:
                        self.single += [[3 * floor(r / 3) + ceil((n + 1) / 3) - 1, 3 * floor(c / 3) + n % 3]]

    def display(self):
        # --- Display known values of puzzle --- #
        strT = '  |-----|-----|-----|-----|-----|-----|-----|-----|-----|\n'
        for r in self.known:
            for c in r:
                strT += '  |  '
                if isinstance(c, int):
                    strT += str(c)
                else:
                    strT += ' '
            strT += '  |\n'
            strT += '  |-----|-----|-----|-----|-----|-----|-----|-----|-----|\n'
        return strT

    def displayG(self):
        # --- Display guess values of puzzle --- #
        strT = ' |-------|-------|-------|-------|-------|-------|-------|-------|-------|\n'
        for r in range(9):
            for m in range(3):
                for c in range(9):
                    temp = self.guess[r][c]
                    strT += ' |'
                    for n in range(3*m+1,3*(m+1)+1):
                        strT += ' '
                        if isinstance(temp, list):
                            if n in temp:
                                strT += str(n)
                            else:
                                strT += ' '
                        else:
                            strT += ' '
                strT += ' |\n'
            strT += ' |-------|-------|-------|-------|-------|-------|-------|-------|-------|\n'
        return strT

    def nSing(self):
        # --- Fill cells containing naked singles --- #
        while len(self.single) > 0:
            # Get row and column of single cell
            r = self.single[0][0]
            c = self.single[0][1]
            # Fill cell of known puzzle
            self.fillCell(r, c, self.guess[r][c][0])
            # Delete from list of single cells
            self.single = self.single[1:]

    def hSing(self):
        # --- Fill cells containing hidden singles --- #
        bLst = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        # Go through 9 rows, columns, and boxes
        for m in range(9):
            # Go through each number 1-9
            for n in range(1, 10):
                # Rows
                rCnt = []
                # Go through each of the 9 elements in the row
                for c in range(9):
                    item = self.guess[m][c]
                    if isinstance(item, list):
                        if n in item:
                            rCnt += [[m, c]]
                if len(rCnt) == 1:
                    self.fillCell(rCnt[0][0], rCnt[0][1], n)
                # Columns
                cCnt = []
                # Go through each of the 9 elements in the column
                for r in range(9):
                    item = self.guess[r][m]
                    if isinstance(item, list):
                        if n in item:
                            rCnt += [[r, m]]
                if len(cCnt) == 1:
                    self.fillCell(cCnt[0][0], cCnt[0][1], n)
                # Boxes
                bCnt = []
                r = bLst[m][0]
                c = bLst[m][1]
                # Go through each of the 9 elements in the box
                for k in range(9):
                    item = self.guess[r + ceil((k + 1) / 3) - 1][c + k % 3]
                    if isinstance(item, list):
                        if n in item:
                            bCnt += [[r + ceil((k + 1) / 3) - 1, c + k % 3]]
                if len(bCnt) == 1:
                    self.fillCell(bCnt[0][0], bCnt[0][1], n)




