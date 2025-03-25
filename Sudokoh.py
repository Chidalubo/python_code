class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.empty = 0
        self.box_size = 3

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.empty:
                    return i, j
        return None

    def is_valid(self, num, pos):
        # Check row
        for i in range(self.size):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(self.size):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // self.box_size
        box_y = pos[0] // self.box_size

        for i in range(box_y * self.box_size, box_y * self.box_size + self.box_size):
            for j in range(box_x * self.box_size, box_x * self.box_size + self.box_size):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, self.size + 1):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = self.empty

        return False

    def print_board(self):
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

# Example usage:
if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solver = SudokuSolver(board)
    solver.print_board()
    print("\nSolving...\n")
    solver.solve()
    solver.print_board()
