def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def check_tie(board):
    for cell in board:
        if cell == ' ':
            return False
    return True

def play_game():
    board = [' '] * 9
    current_player = 'X'
    print("Let's play Tic Tac Toe!")
    print_board(board)
    while True:
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = current_player
            print_board(board)
            if check_win(board):
                print(f"Congratulations! Player {current_player} wins!")
                break
            elif check_tie(board):
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already taken. Try again.")

play_game()