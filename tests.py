from chessboard import *
import unittest

class TestChessboard(unittest.TestCase):

    def testFindEmptyRowsWithEmptyBoard(self):
        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        chessboard = Chessboard(board, 3)

        emptyRows = chessboard.findEmptyRows()
        self.assertEqual(len(emptyRows), 3)
        self.assertTrue(0 in emptyRows)
        self.assertTrue(1 in emptyRows)
        self.assertTrue(2 in emptyRows)


    def testFindEmptyRowsWithCompleteBoard(self):
        board = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)

        emptyRows = chessboard.findEmptyRows()
        self.assertEqual(len(emptyRows), 0)


    def testFindEmptyColsWithEmptyBoard(self):
        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        chessboard = Chessboard(board, 3)

        emptyCols = chessboard.findEmptyCols()
        self.assertEqual(len(emptyCols), 3)
        self.assertTrue(0 in emptyCols)
        self.assertTrue(1 in emptyCols)
        self.assertTrue(2 in emptyCols)

    def testFindEmptyColsWithCompleteBoard(self):
        board = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)

        emptyCols = chessboard.findEmptyCols()
        self.assertEqual(len(emptyCols), 0)

    def testIsComplete(self):
        board = [[1, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertFalse(chessboard.isComplete())

        board = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertTrue(chessboard.isComplete())

        board = [[0, 0, 0],
                [1, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertFalse(chessboard.isComplete())

    def testCompleteBoard(self):
        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        chessboard.completeBoard()
        self.assertTrue(chessboard.isComplete())

        board = [[0, 1, 0],
                [1, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        chessboard.completeBoard()
        self.assertTrue(chessboard.isComplete())

        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        chessboard = Chessboard(board, 3)
        chessboard.completeBoard()
        self.assertTrue(chessboard.isComplete())

    def isValidBoard(self):
        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        chessboard = Chessboard(board, 3)
        self.assertTrue(chessboard.isValidBoard())

        board = [[1, 1, 0],
                [0, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertFalse(chessboard.isValidBoard())

        board = [[1, -1, 0],
                [0, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertFalse(chessboard.isValidBoard())

        board = [[1, "abc", 0],
                [0, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertFalse(chessboard.isValidBoard())

        board = [[1, 0, 0],
                [1, 0, 0],
                [0, 0, 1]]
        chessboard = Chessboard(board, 3)
        self.assertFalse(chessboard.isValidBoard())


if __name__ == '__main__':
    unittest.main()
