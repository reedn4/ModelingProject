from math import floor, ceil
class Sudoku:
    def __init__(self, puz, but=[], lab=[]):
        # Known values of puzzle
        self.known = puz
        # Possible values for unknown cells
        self.guess = []
        # Guess cells with single value
        self.single = []
        self.buttons = but
        self.gLabels = lab
        self.initGuess()

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
                        self.single += [[r, c]]
            tempF += [temp]
        self.guess = tempF

    def fillCell(self, r, c, num):
        # --- Add cell value to known values of puzzle --- #
        # Fill cell in known list
        self.known[r][c] = num
        if len(self.buttons) > 0:
            self.buttons[r][c].config(text=str(num), command=None)
        # Delete guess list for cell
        self.guess[r][c] = 'null'
        self.updateGL(r, c)
        if [r, c] in self.single:
            self.single.remove([r,c])
        # Update guess list for change
        for n in range(9):
            # Row update
            rTemp = self.guess[r][n]
            if isinstance(rTemp, list):
                if num in rTemp:
                    rTemp.remove(num)
                    self.updateGL(r, n)
                    if len(rTemp) == 1:
                        self.single += [[r, n]]
            # Column update
            cTemp = self.guess[n][c]
            if isinstance(cTemp, list):
                if num in cTemp:
                    cTemp.remove(num)
                    self.updateGL(n, c)
                    if len(cTemp) == 1:
                        self.single += [[n, c]]
            # Box update
            bTemp = self.guess[3 * floor(r / 3) + ceil((n + 1) / 3) - 1][3 * floor(c / 3) + n % 3]
            if isinstance(bTemp, list):
                if num in bTemp:
                    bTemp.remove(num)
                    self.updateGL(3 * floor(r / 3) + ceil((n + 1) / 3) - 1, 3 * floor(c / 3) + n % 3)
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

    def updateGL(self, r, c):
        if len(self.gLabels) > 0:
            temp = self.guess[r][c]
            strT = ''
            if isinstance(temp, list):
                for n in range(1, 10):
                    strT += '  '
                    if n in temp:
                        strT += str(n)
                    else:
                        strT += '  '
                    if n % 3 == 0 and n < 9:
                        strT += ' \n'
                self.gLabels[r][c].config(text=strT)
            else:
                self.gLabels[r][c].config(text=strT, bg='gray25')

    def nSing(self):
        # --- Fill cells containing naked singles --- #
        while len(self.single) > 0:
            # Get row and column of single cell
            r = self.single[0][0]
            c = self.single[0][1]
            # Fill cell of known puzzle
            self.fillCell(r, c, self.guess[r][c][0])

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

    def nPair(self):
        # --- Update guesses based on naked pairs --- #
        bLst = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        # Go through all 9 rows, columns, and boxes
        for n in range(9):
            # Set row
            row = self.guess[n]
            doneR = []
            # Set Column
            col = [k[n] for k in self.guess]
            doneC = []
            # Set Box
            r = bLst[n][0]
            cL = bLst[n][1]
            box = [self.guess[r + ceil((k + 1) / 3) - 1][cL + k % 3] for k in range(9)]
            doneB = []
            # Go through each cell in the row, column, and box
            for c in range(9):
                # Row
                # Check if there are two guesses for the cell
                if isinstance(row[c], list) and len(row[c]) == 2:
                    # All cells in the row except the current cell
                    lst = row[:c]+row[(c+1):]
                    # Check for matching pair
                    if row[c] in lst:
                        # Find any matching cell in the row
                        match = lst.index(row[c])
                        # Fix index to account for removed cell
                        if match >= c:
                            match += 1
                        # Check to see if pair was already found
                        if match not in doneR:
                            # Add cell to found list
                            doneR += [match]
                            # delete any other instances of numbers in pair
                            for k in range(len(row)):
                                # Check that the cell isn't the pair
                                if row[k] != row[c] and isinstance(row[k], list):
                                    # Check for first number in pair
                                    if row[c][0] in row[k]:
                                        # Remove number from guess
                                        row[k].remove(row[c][0])
                                        self.updateGL(n, k)
                                        # Check for naked single
                                        if len(self.guess[n][k]) == 1:
                                            self.single += [[n, k]]
                                    # Check for the second number in pair
                                    if row[c][1] in row[k]:
                                        # Remove number from guess
                                        row[k].remove(row[c][1])
                                        self.updateGL(n, k)
                                        # Check for naked single
                                        if len(self.guess[n][k]) == 1:
                                            self.single += [[n, k]]
                # Column (Same technique as used for the row - see above comments)
                if isinstance(col[c], list) and len(col[c]) == 2:
                    lst = col[:c]+col[(c+1):]
                    if col[c] in lst:
                        match = lst.index(col[c])
                        if match >= c:
                            match += 1
                        if match not in doneC:
                            doneC += [match]
                            for k in range(len(col)):
                                if col[k] != col[c] and isinstance(col[k], list):
                                    if col[c][0] in col[k]:
                                        col[k].remove(col[c][0])
                                        self.updateGL(k, n)
                                        if len(self.guess[k][n]) == 1:
                                            self.single += [[k, n]]
                                    if col[c][1] in col[k]:
                                        col[k].remove(col[c][1])
                                        self.updateGL(k, n)
                                        if len(self.guess[k][n]) == 1:
                                            self.single += [[k, n]]
                # Box (Same technique as used for the row - see above comments)
                if isinstance(box[c], list) and len(box[c]) == 2:
                    lst = box[:c]+box[(c+1):]
                    if box[c] in lst:
                        match = lst.index(box[c])
                        if match >= r:
                            match += 1
                        if match not in doneB:
                            doneB += [match]
                            for k in range(len(box)):
                                if box[k] != box[c] and isinstance(box[k], list):
                                    if box[c][0] in box[k]:
                                        box[k].remove(box[c][0])
                                        self.updateGL(r + ceil((k + 1) / 3) - 1, cL + k % 3)
                                        if len(self.guess[r + ceil((k + 1) / 3) - 1][cL + k % 3]) == 1:
                                            self.single += [[r + ceil((k + 1) / 3) - 1, cL + k % 3]]
                                    if box[c][1] in box[k]:
                                        box[k].remove(box[c][1])
                                        self.updateGL(r + ceil((k + 1) / 3) - 1, cL + k % 3)
                                        if len(self.guess[r + ceil((k + 1) / 3) - 1][cL + k % 3]) == 1:
                                            self.single += [[r + ceil((k + 1) / 3) - 1, cL + k % 3]]

    def pointPair(self):
        # --- Update guesses based on pointing pairs --- #
        # Top left location of each box
        bLst = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        # Go through each box
        for box in bLst:
            # Set Box
            r = box[0]
            c = box[1]
            # Go through all possible values 1-9
            for n in range(1, 10):
                indN = []
                # Go through each cell in the box
                for k in range(9):
                    # Row number
                    rT = r + ceil((k + 1) / 3) - 1
                    # Column number
                    cT = c + k % 3
                    # Check if the cell value is already known
                    if isinstance(self.guess[rT][cT], list):
                        # Check if the number is a possible cell value
                        if n in self.guess[rT][cT]:
                            indN += [[rT, cT]]
                # Check for matches
                if len(indN) > 0:
                    row = True
                    col = True
                    rLst = []
                    cLst = []
                    # Go through each match
                    for item in indN:
                        rLst += [item[0]]
                        cLst += [item[1]]
                        # Check if the matches are in the same row
                        if indN[0][0] != rLst[-1]:
                            row = False
                        # Check if the matches are in the same column
                        if indN[0][1] != cLst[-1]:
                            col = False
                    # If the matches are in the same row
                    if row:
                        # Remove pair numbers from other cells in the row
                        for m in range(9):
                            # Check if the cell value is already known
                            if isinstance(self.guess[rLst[0]][m], list):
                                # Check if cell is not a pair and contains the first pair value
                                if n in self.guess[rLst[0]][m] and m not in cLst:
                                    # Remove value
                                    self.guess[rLst[0]][m].remove(n)
                                    self.updateGL(rLst[0], m)
                                    if len(self.guess[rLst[0]][m]) == 1:
                                        self.single += [[rLst[0], m]]
                    # If the matches in the same column
                    if col:
                        # Remove pair numbers from other cells in the column
                        for m in range(9):
                            # Check if the cell value is already known
                            if isinstance(self.guess[m][cLst[0]], list):
                                # Check if cell is not a pair and contains the first pair value
                                if n in self.guess[m][cLst[0]] and m not in rLst:
                                    # Remove value
                                    self.guess[m][cLst[0]].remove(n)
                                    self.updateGL(m, cLst[0])
                                    if len(self.guess[m][cLst[0]]) == 1:
                                        self.single += [[m, cLst[0]]]

    def claimPair(self):
        # --- Update guesses based on claiming pairs --- #
        bLst = [0, 1, 2]
        # Go through every value 1-9
        for n in range(1, 10):
            # Go through each of the 9 rows and columns
            for k in range(9):
                # Row
                row = self.guess[k]
                rLst = []
                # Column
                col = [item[k] for item in self.guess]
                cLst = []
                # Check for values in each cell
                for c in range(9):
                    # Row
                    if isinstance(row[c], list):
                        if n in row[c]:
                            rLst += [c]
                    # Column
                    if isinstance(col[c], list):
                        if n in col[c]:
                            cLst += [c]
                # Check if value is in the row
                if len(rLst) > 0:
                    # Check if values appear in the same box
                    boxS = True
                    for elem in rLst:
                        if ceil((rLst[0] + 1) / 3) != ceil((elem + 1) / 3):
                            boxS = False
                    # If values are in the same box
                    if boxS:
                        # Find row span of the box
                        indB = bLst.index(k % 3)
                        addB = (ceil((k+1)/3) - 1) * 3
                        # Find column span of the box
                        initm = (ceil((rLst[0] + 1)/3) - 1) * 3
                        # Go through all columns in the box
                        for m in range(initm, initm + 3):
                            # Check first row that is not the current row
                            if isinstance(self.guess[bLst[indB - 1] + addB][m], list):
                                # Check if cell contains the value
                                if n in self.guess[bLst[indB - 1] + addB][m]:
                                    # Remove value
                                    self.guess[bLst[indB - 1] + addB][m].remove(n)
                                    removed = True
                                    self.updateGL(bLst[indB - 1] + addB, m)
                                    # Check if there is a single possible value left
                                    if len(self.guess[bLst[indB - 1] + addB][m]) == 1:
                                        self.single += [[bLst[indB - 1] + addB, m]]
                            # Check second row that is not the current row
                            if isinstance(self.guess[bLst[indB - 2] + addB][m], list):
                                # Check if cell contains the value
                                if n in self.guess[bLst[indB - 2] + addB][m]:
                                    # Remove value
                                    self.guess[bLst[indB - 2] + addB][m].remove(n)
                                    removed = True
                                    self.updateGL(bLst[indB - 2] + addB, m)
                                    # Check if there is a single possible value left
                                    if len(self.guess[bLst[indB - 2] + addB][m]) == 1:
                                        self.single += [[bLst[indB - 2] + addB, m]]
                # Check if value is in the column
                if len(cLst) > 0:
                    # Check if values appear in the same box
                    boxS = True
                    for elem in cLst:
                        if ceil((cLst[0] + 1) / 3) != ceil((elem + 1) / 3):
                            boxS = False
                    # If values are in the same box
                    if boxS:
                        # Find column span of the box
                        indB = bLst.index(k % 3)
                        addB = (ceil((k+1)/3) - 1) * 3
                        # Find row span of the box
                        initm = (ceil((cLst[0] + 1) / 3) - 1) * 3
                        # Go through all rows of the box
                        for m in range(initm, initm + 3):
                            # Check first column that is not the current row
                            if isinstance(self.guess[m][bLst[indB - 1] + addB], list):
                                # Check if cell contains the value
                                if n in self.guess[m][bLst[indB - 1] + addB]:
                                    # Remove value
                                    self.guess[m][bLst[indB - 1] + addB].remove(n)
                                    self.updateGL(m, bLst[indB - 1] + addB)
                                    # Check if there is a single possible value left
                                    if len(self.guess[m][bLst[indB - 1] + addB]) == 1:
                                        self.single += [[m, bLst[indB - 1] + addB]]
                            # Check second column that is not the current row
                            if isinstance(self.guess[m][bLst[indB - 2] + addB], list):
                                # Check if cell contains the value
                                if n in self.guess[m][bLst[indB - 2] + addB]:
                                    # Remove value
                                    self.guess[m][bLst[indB - 2] + addB].remove(n)
                                    self.updateGL(m, bLst[indB - 2] + addB)
                                    # Check if there is a single possible value left
                                    if len(self.guess[m][bLst[indB - 2] + addB]) == 1:
                                        self.single += [[m, bLst[indB - 2] + addB]]

    def nTriple(self):
        # --- Update guesses based on naked triples --- #
        bLst = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        # Go through all 9 rows, columns, and boxes
        for n in range(9):
            # Set row
            row = self.guess[n]
            rowL = []
            # Set Column
            col = [k[n] for k in self.guess]
            colL = []
            # Set Box
            r = bLst[n][0]
            cL = bLst[n][1]
            box = [self.guess[r + ceil((k + 1) / 3) - 1][cL + k % 3] for k in range(9)]
            boxL = []
            # Go through each cell in the row, column, and box
            for c in range(9):
                # Row
                if len(row[c]) <= 3 and len(row[c]) > 0:
                    for item in rowL:
                        temp = []
                        for itemS in item:
                            temp += row[itemS]
                        if len(list(dict.fromkeys(temp + row[c]))) <= 3:
                            if len(row[item[0]]) > len(row[c]):
                                item += [c]
                            else:
                                item.insert(0, c)
                    rowL += [[c]]
                # Column
                if len(col[c]) <= 3 and len(col[c]) > 0:
                    for item in colL:
                        temp = []
                        for itemS in item:
                            temp += col[itemS]
                        if len(list(dict.fromkeys(temp + col[c]))) <= 3:
                            if len(col[item[0]]) > len(col[c]):
                                item += [c]
                            else:
                                item.insert(0, c)
                    colL += [[c]]
                # Box
                if len(box[c]) <= 3 and len(box[c]) > 0:
                    for item in boxL:
                        temp = []
                        for itemS in item:
                            temp += box[itemS]
                        if len(list(dict.fromkeys(temp + box[c]))) <= 3:
                            if len(box[item[0]]) > len(box[c]):
                                item += [c]
                            else:
                                item.insert(0, c)
                    boxL += [[c]]
            # Check for naked triples in the row
            for item in rowL:
                if len(item) == 3:
                    lst = []
                    for sub in item:
                        for num in row[sub]:
                            if num not in lst:
                                lst += [num]
                    for k in range(9):
                        if k not in item and isinstance(row[k], list):
                            for val in lst:
                                if val in row[k]:
                                    row[k].remove(val)
                                    self.updateGL(n, k)
                                    if len(self.guess[n][k]) == 1:
                                        self.single += [[n, k]]
            # Check for naked triples in the column
            for item in colL:
                if len(item) == 3:
                    lst = []
                    for sub in item:
                        for num in col[sub]:
                            if num not in lst:
                                lst += [num]
                    for k in range(9):
                        if k not in item and isinstance(col[k], list):
                            for val in lst:
                                if val in col[k]:
                                    col[k].remove(val)
                                    self.updateGL(k, n)
                                    if len(self.guess[k][n]) == 1:
                                        self.single += [[k, n]]
            # Check for naked triples in the box
            for item in boxL:
                if len(item) == 3:
                    lst = []
                    for sub in item:
                        for num in box[sub]:
                            if num not in lst:
                                lst += [num]
                    for k in range(9):
                        if k not in item and isinstance(box[k], list):
                            for val in lst:
                                if val in box[k]:
                                    box[k].remove(val)
                                    self.updateGL(r + ceil((k + 1) / 3) - 1, cL + k % 3)
                                    if len(self.guess[r + ceil((k + 1) / 3) - 1][cL + k % 3]) == 1:
                                        self.single += [[r + ceil((k + 1) / 3) - 1, cL + k % 3]]

    def xWing(self):
        # --- Update guesses based on x-wing --- #
        return

    def hPair(self):
        # --- Update guesses based on hidden pairs --- #
        return

    def nQuad(self):
        # --- Update guesses based on naked quads --- #
        return

