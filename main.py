from chessboard import *

if __name__ == '__main__':
    f = open("input.txt", "r")
    rows = int(f.readline())

    board = [[0] * rows for i in range(rows)]

    for row in range(rows):
        line = str(f.readline())
        if len(line[:-1]) != rows:
            raise Exception("Invalid Input!")

        col = line.find("1")
        if col >= 0:
            board[row][col] = 1

    print("BOARD READ")
    for row in board:
        print(row)

    cb = Chessboard(board, rows)
    print("COMPLETE")
    complete_board = cb.completeBoard()
    for row in complete_board:
        print(row)
