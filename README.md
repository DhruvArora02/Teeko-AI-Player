# Teeko-AI-Player

__Project Overview__ -

This project implements an AI-powered game player for the board game Teeko, a strategic two-player game. The AI leverages Minimax with heuristic evaluations to intelligently compete against opponents. It can handle both drop and movement phases of the game while ensuring valid moves and optimal gameplay.

__Key Features__ -

- Intelligent Move Generation: The AI uses Minimax with a heuristic evaluation function to assess non-terminal states.

- Successor States Handling: Generates valid successor states for both drop and movement phases.

- Win-Condition Detection: Checks for horizontal, vertical, diagonal, and 2x2 box patterns to identify winning states.

- Readable Board Display: Prints the current board state with row and column labels for easy interpretation.

- Opponent Move Validation: Ensures that opponent moves follow game rules.

- Strategic Gameplay: Competes against easy, medium, and hard opponents with adaptive strategies.

__Technologies Used__ -

- Programming Language: Python
- Libraries: random for selecting piece color, copy for state manipulation during move generation.

__How It Works__ -

1. Game Phases -
    - Drop Phase: Each player alternates placing their pieces on empty spaces on the board.
    
    - Movement Phase: Players move their pieces to adjacent empty spaces to form a winning alignment.

2. AI Logic -

    - Move Generation: Generates valid successor states depending on the game phase.

    - Heuristic Evaluation: Assigns scores based on aligned pieces and proximity to forming a winning line or box.

    - Minimax Algorithm: Explores possible game states up to a specified depth to determine the best move.

3. Win Detection -

    - Horizontal/Vertical Wins: Four aligned pieces in rows or columns.
      
    - Diagonal Wins: Four aligned pieces diagonally.
      
    - 2x2 Box Patterns: A square of four pieces.







