import random
from game_logic import TeekoGameLogic
from heuristic import HeuristicEvaluator
from utils import print_board

class TeekoPlayer:
   
    def __init__(self):
        self.my_piece = random.choice(['b', 'r'])
        self.opp = 'b' if self.my_piece == 'r' else 'r'
        self.game_logic = TeekoGameLogic(self.my_piece, self.opp)
        self.heuristic = HeuristicEvaluator(self.my_piece, self.opp)

    def make_move(self, state):
        drop_phase = sum(row.count(' ') for row in state) > 17
        successors = self.game_logic.succ(state, drop_phase)
        best_move = None
        best_score = float('-inf')

        for succ_state, move in successors:
            score = self.min_value(succ_state, depth=0, max_depth=3)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def min_value(self, state, depth, max_depth):
        if depth == max_depth or self.game_logic.game_value(state) != 0:
            return self.heuristic.heuristic_game_value(state)
        value = float('inf')
        for succ_state, _ in self.game_logic.succ(state, drop_phase=False):
            value = min(value, self.max_value(succ_state, depth + 1, max_depth))
        return value

    def max_value(self, state, depth, max_depth):
        if depth == max_depth or self.game_logic.game_value(state) != 0:
            return self.heuristic.heuristic_game_value(state)
        value = float('-inf')
        for succ_state, _ in self.game_logic.succ(state, drop_phase=False):
            value = max(value, self.min_value(succ_state, depth + 1, max_depth))
        return value

    def print_board(self, board):
        print_board(board)
