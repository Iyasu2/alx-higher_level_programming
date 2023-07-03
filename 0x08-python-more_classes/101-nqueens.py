#!/usr/bin/python3


import sys
'''
this function solves the queen problem
'''


def nqueens(N):
    '''
    this function solves the queen problem
    '''
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        '''
        checks whether it is valid to place a queen at the given position
        '''
        for r, c in enumerate(board):
            if c == col or r - c == row - col or r + c == row + col:
                return False
            return True

    def solve(board, row):
        '''
        recursively tries to place queens on the board
        '''
        if row == N:
            print(board)
            return

        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solve([-1] * N, 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
