def print_board(board):
    for row in range(len(board)):
        line = str(row) + ": "
        for cell in board[row]:
            line += cell + " "
        print(line)
    print("   A B C D E")
