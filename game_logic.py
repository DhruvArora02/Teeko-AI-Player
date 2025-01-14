import copy

class TeekoGameLogic:
    
    def __init__(self, my_piece, opp):
        self.my_piece = my_piece
        self.opp = opp
        self.board = [[' ' for _ in range(5)] for _ in range(5)]

    def succ(self, state, drop_phase):
        """ Generate all successors. """
        successors = []
        if drop_phase:
            for row in range(5):
                for col in range(5):
                    if state[row][col] == ' ':
                        new_state = copy.deepcopy(state)
                        new_state[row][col] = self.my_piece
                        successors.append((new_state, [(row, col)]))
        else:
            for row in range(5):
                for col in range(5):
                    if state[row][col] == self.my_piece:
                        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < 5 and 0 <= nc < 5 and state[nr][nc] == ' ':
                                new_state = copy.deepcopy(state)
                                new_state[row][col] = ' '
                                new_state[nr][nc] = self.my_piece
                                successors.append((new_state, [(nr, nc), (row, col)]))
        return successors

    def game_value(self, state):
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                    return 1 if row[i] == self.my_piece else -1

        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i + 1][col] == state[i + 2][col] == state[i + 3][col]:
                    return 1 if state[i][col] == self.my_piece else -1

        for i in range(2):
            for j in range(2):
                if state[i][j] != ' ' and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == state[i + 3][j + 3]:
                    return 1 if state[i][j] == self.my_piece else -1

                if state[i][4 - j] != ' ' and state[i][4 - j] == state[i + 1][3 - j] == state[i + 2][2 - j] == state[i + 3][1 - j]:
                    return 1 if state[i][4 - j] == self.my_piece else -1

        return 0
