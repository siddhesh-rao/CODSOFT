import math

# Display the board
def print_board(board):
    for i in range(3):
        print(board[3*i], board[3*i+1], board[3*i+2])
    print()

# Check for winner
def check_winner(board):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != "_":
            return board[wc[0]]
    if "_" not in board:
        return "Tie"
    return None

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    if result == "O":   # AI wins
        return 1
    elif result == "X": # Human wins
        return -1
    elif result == "Tie":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "_":
                board[i] = "O"
                score = minimax(board, depth+1, False, alpha, beta)
                board[i] = "_"
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "_":
                board[i] = "X"
                score = minimax(board, depth+1, True, alpha, beta)
                board[i] = "_"
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

# AI chooses best move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == "_":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = "_"
            if score > best_score:
                best_score = score
                move = i
    return move

# Game Loop
def play_tic_tac_toe():
    board = ["_"] * 9
    print("🎮 Tic-Tac-Toe: You = X | AI = O")
    print_board(board)

    while True:
        # Human turn
        user = int(input("Enter position (1-9): ")) - 1
        if board[user] != "_":
            print("Invalid move, try again.")
            continue
        board[user] = "X"
        print_board(board)

        if check_winner(board):
            print("Result:", check_winner(board))
            break

        # AI turn
        ai = best_move(board)
        board[ai] = "O"
        print("AI played at position:", ai + 1)
        print_board(board)

        if check_winner(board):
            print("Result:", check_winner(board))
            break

# Start the game
play_tic_tac_toe()
