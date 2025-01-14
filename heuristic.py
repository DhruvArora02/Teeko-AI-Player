class HeuristicEvaluator:
    
    def __init__(self, my_piece, opp):
        self.my_piece = my_piece
        self.opp = opp

    def heuristic_game_value(self, state):
        terminal = self.game_value(state)
        if terminal != 0:
            return terminal
        my_score = 0
        opp_score = 0
        for row in range(5):
            for col in range(5):
                if state[row][col] == self.my_piece:
                    my_score += self.evaluate_position(state, row, col)
                elif state[row][col] == self.opp:
                    opp_score += self.evaluate_position(state, row, col)
        return (my_score - opp_score) / 100.0

    def evaluate_position(self, state, row, col):
        score = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and state[nr][nc] == self.my_piece:
                score += 1
        return score
