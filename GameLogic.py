class CheckMove:
    def __init__(self):
        self.ROWS = 8
        self.COLUMNS = 8

    def check_moves_minus_1(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        valid_moves_minus_1 = []

        if ((0 <= row_check_moves - 1 < self.ROWS) and (0 <= column_check_moves - 1 < self.COLUMNS)) and (
                board[row_check_moves - 1][column_check_moves - 1] == 0):
            valid_moves_minus_1.append((row_check_moves - 1, column_check_moves - 1))  # for -1: check if up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 1) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves - 2))  # for -1: to take pieces up left

        if ((0 <= row_check_moves - 1 < self.ROWS) and (0 <= column_check_moves + 1 < self.COLUMNS)) and (
                board[row_check_moves - 1][column_check_moves + 1] == 0):
            valid_moves_minus_1.append((row_check_moves - 1, column_check_moves + 1))  # for -1: check if up right

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 1) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves + 2))  # for -1: to take pieces up right

        # the same, just checks if its enemy king
        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 2) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves - 2))  # for -1: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 2) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves + 2))  # for -1: to take pieces up right

        return valid_moves_minus_1

    def eat_pieces_minus_1(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        valid_moves_minus_1 = []

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 1) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves - 2))  # for -1: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 1) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves + 2))  # for -1: to take pieces up right

        # the same, just checks if its enemy king
        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 2) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves - 2))  # for -1: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 2) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            valid_moves_minus_1.append((row_check_moves - 2, column_check_moves + 2))  # for -1: to take pieces up right

        return valid_moves_minus_1

    def check_moves_1(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        valid_moves_1 = []

        if ((0 <= row_check_moves + 1 < self.ROWS) and (0 <= column_check_moves - 1 < self.COLUMNS)) and (
                board[row_check_moves + 1][column_check_moves - 1] == 0):
            valid_moves_1.append((row_check_moves + 1, column_check_moves - 1))  # for 1: check if down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -1) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves - 2))  # for 1: to take pieces down left

        if ((0 <= row_check_moves + 1 < self.ROWS) and (0 <= column_check_moves + 1 < self.COLUMNS)) and (
                board[row_check_moves + 1][column_check_moves + 1] == 0):
            valid_moves_1.append((row_check_moves + 1, column_check_moves + 1))  # for 1: check if down right

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -1) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves + 2))  # for 1: to take pieces down right

        # the same, just checking if its enemy king
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -2) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves - 2))  # for 1: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -2) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves + 2))  # for 1: to take pieces down right

        return valid_moves_1

    def eat_pieces_1(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        valid_moves_1 = []

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -1) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves - 2))  # for 1: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -1) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves + 2))  # for 1: to take pieces down right

        # the same, just checking if its enemy king
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -2) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves - 2))  # for 1: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -2) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            valid_moves_1.append((row_check_moves + 2, column_check_moves + 2))  # for 1: to take pieces down right

        return valid_moves_1


    def king_check_moves_minus_2(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        king_valid_moves_minus_2 = []

        if ((0 <= row_check_moves - 1 < self.ROWS) and (0 <= column_check_moves - 1 < self.COLUMNS)) and (
                board[row_check_moves - 1][column_check_moves - 1] == 0):
            king_valid_moves_minus_2.append((row_check_moves - 1, column_check_moves - 1))  # for -2: check if up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 1) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves - 2))  # for -2: to take pieces up left

        if ((0 <= row_check_moves - 1 < self.ROWS) and (0 <= column_check_moves + 1 < self.COLUMNS)) and (
                board[row_check_moves - 1][column_check_moves + 1] == 0):
            king_valid_moves_minus_2.append((row_check_moves - 1, column_check_moves + 1))  # for -2: check if up right

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 1) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves + 2))  # for -2: to take pieces up right

        # the same, just checks if its enemy king
        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 2) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves - 2))  # for -2: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 2) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves + 2))  # for -2: to take pieces up right

        # p2 moves
        if ((0 <= row_check_moves + 1 < self.ROWS) and (0 <= column_check_moves - 1 < self.COLUMNS)) and (
                board[row_check_moves + 1][column_check_moves - 1] == 0):
            king_valid_moves_minus_2.append((row_check_moves + 1, column_check_moves - 1))  # for -2: check if down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == 1) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves - 2))  # for -2: to take pieces down left

        if ((0 <= row_check_moves + 1 < self.ROWS) and (0 <= column_check_moves + 1 < self.COLUMNS)) and (
                board[row_check_moves + 1][column_check_moves + 1] == 0):
            king_valid_moves_minus_2.append((row_check_moves + 1, column_check_moves + 1))  # for -2: check if down right

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == 1) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves + 2))  # for -2: to take pieces down right

        # the same, just checking if its enemy king
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == 2) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves - 2))  # for -2: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == 2) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves + 2))  # for -2: to take pieces down right


        return king_valid_moves_minus_2

    def king_eat_pieces_minus_2(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        king_valid_moves_minus_2 = []

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 1) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves - 2))  # for -2: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 1) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves + 2))  # for -2: to take pieces up right

        # the same, just checks if its enemy king
        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == 2) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves - 2))  # for -2: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == 2) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves - 2, column_check_moves + 2))  # for -2: to take pieces up right

        # p2 moves
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == 1) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves - 2))  # for -2: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == 1) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves + 2))  # for -2: to take pieces down right

        # the same, just checking if its enemy king
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == 2) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves - 2))  # for -2: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == 2) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_minus_2.append((row_check_moves + 2, column_check_moves + 2))  # for -2: to take pieces down right

        return king_valid_moves_minus_2

    def king_check_moves_2(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        king_valid_moves_2 = []

        if ((0 <= row_check_moves - 1 < self.ROWS) and (0 <= column_check_moves - 1 < self.COLUMNS)) and (
                board[row_check_moves - 1][column_check_moves - 1] == 0):
            king_valid_moves_2.append((row_check_moves - 1, column_check_moves - 1))  # for 2: check if up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == -1) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves - 2))  # for 2: to take pieces up left

        if ((0 <= row_check_moves - 1 < self.ROWS) and (0 <= column_check_moves + 1 < self.COLUMNS)) and (
                board[row_check_moves - 1][column_check_moves + 1] == 0):
            king_valid_moves_2.append((row_check_moves - 1, column_check_moves + 1))  # for 2: check if up right

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == -1) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves + 2))  # for 2: to take pieces up right

        # the same, just checks if its enemy king
        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == -2) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves - 2))  # for 2: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == -2) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves + 2))  # for 2: to take pieces up right

        # p2 moves
        if ((0 <= row_check_moves + 1 < self.ROWS) and (0 <= column_check_moves - 1 < self.COLUMNS)) and (
                board[row_check_moves + 1][column_check_moves - 1] == 0):
            king_valid_moves_2.append((row_check_moves + 1, column_check_moves - 1))  # for 2: check if down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -1) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves - 2))  # for 2: to take pieces down left

        if ((0 <= row_check_moves + 1 < self.ROWS) and (0 <= column_check_moves + 1 < self.COLUMNS)) and (
                board[row_check_moves + 1][column_check_moves + 1] == 0):
            king_valid_moves_2.append((row_check_moves + 1, column_check_moves + 1))  # for 2: check if down right

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -1) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves + 2))  # for 2: to take pieces down right

        # the same, just checking if its enemy king
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -2) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves - 2))  # for 2: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -2) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves + 2))  # for 2: to take pieces down right

        return king_valid_moves_2

    def king_eat_pieces_2(self, piece_coordination, board):
        row_check_moves, column_check_moves = piece_coordination
        king_valid_moves_2 = []

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == -1) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves - 2))  # for 2: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == -1) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves + 2))  # for 2: to take pieces up right

        # the same, just checks if its enemy king
        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves - 1] == -2) and (
                board[row_check_moves - 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves - 2))  # for 2: to take pieces up left

        if ((0 <= row_check_moves - 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves - 1][column_check_moves + 1] == -2) and (
                board[row_check_moves - 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves - 2, column_check_moves + 2))  # for 2: to take pieces up right

        # p2 moves
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -1) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves - 2))  # for 2: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -1) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves + 2))  # for 2: to take pieces down right

        # the same, just checking if its enemy king
        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves - 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves - 1] == -2) and (
                board[row_check_moves + 2][column_check_moves - 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves - 2))  # for 2: to take pieces down left

        if ((0 <= row_check_moves + 2 < self.ROWS) and (0 <= column_check_moves + 2 < self.COLUMNS)) and (
                (board[row_check_moves + 1][column_check_moves + 1] == -2) and (
                board[row_check_moves + 2][column_check_moves + 2] == 0)):
            king_valid_moves_2.append((row_check_moves + 2, column_check_moves + 2))  # for 2: to take pieces down right

        return king_valid_moves_2
