class Board:
    def __init__(self, board):
        self.board = board
    
    def __str__(self):
        board_str = ''

        for row in self.board:
            board_str += ' '.join([str(item) if item != 0 else '*' for item in row]) + '\n'

        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]
    
    def valid_in_col(self, col, num):
        return all(row[col] != num for row in self.board)

    def valid_in_square(self, row, col, num):
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for row_no in range(start_row, start_row + 3):
            for col_no in range(start_col, start_col + 3):
                if self.board[row_no][col_no] == num:
                    return False
        
        return True

    def is_valid(self, empty, num):
        row, col = empty

        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)

        return all([valid_in_row, valid_in_col, valid_in_square])

    def solve(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True

        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    gameboard = Board(board)

    print(f'Unsolved puzzle:\n{gameboard}')

    if gameboard.solve():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('Cannot solve puzzle')

    return gameboard

puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

if __name__ == '__main__':
    solve_sudoku(puzzle)

