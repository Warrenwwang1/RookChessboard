

class Chessboard():
    def __init__(self, board, rooks=8):
        self.board = board
        self.rooks = rooks

    def isComplete(self):
        """
        check if the current board is complete (i.e. all rooks have been placed).
        """
        if sum([sum(row) for row in self.board]) != self.rooks:
            return False
        return True

    def isValidBoard(self):
        """
        checks if current board is a valid board such that
        1) no rooks are colliding
        2) all elements in board are legal (i.e. 0 or 1)
        """
        cols_used = set()
        for row in self.board:
            row_has_rook = False
            for col_index, val in enumerate(row):
                if val != 0 and val != 1:
                    return False
                if val == 1:
                    if col_index in cols_used:
                        return False
                    if row_has_rook:
                        return False
                    cols_used.add(col_index)
                    row_has_rook = True
        return True

    def findEmptyRows(self):
        """
        finds and returns a list of all the empty row indices of board
        """
        emptyRows = []
        for rowIndex, row in enumerate(self.board):
            if sum(row) == 0:
                emptyRows += [rowIndex]
        return emptyRows

    def findEmptyCols(self):
        """
        finds and returns a list of all the empty column indices of board
        """
        emptyCols = set([i for i in range(0, self.rooks)])
        for rowIndex, row in enumerate(self.board):
            for colIndex, col in enumerate(row):
                if col == 1 and colIndex in emptyCols:
                    emptyCols.remove(colIndex)
        return list(emptyCols)

    def completeBoard(self):
        """
        returns a board that is complete with non-colliding rooks
        """
        if self.isComplete():
            return self.board

        emptyCols = self.findEmptyRows()
        emptyRows = self.findEmptyCols()

        if len(emptyCols) != len(emptyRows) or not self.isValidBoard():
            raise Exception("Input Board is unsolvable")

        for row, col in zip(emptyCols, emptyRows):
            self.board[row][col] = 1
        return self.board
