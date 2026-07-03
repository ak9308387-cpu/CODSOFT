print("=" * 35)
print("      TIC-TAC-TOE AI")
print(" Human (X) vs Computer (O)")
print("=" * 35)

board = [" " for _ in range(9)]


def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def board_full():
    return " " not in board


def minimax(is_ai):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if board_full():
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best


def computer_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


while True:
    show_board()

    while True:
        try:
            user = int(input("Enter your move (1-9): ")) - 1
            if 0 <= user <= 8 and board[user] == " ":
                board[user] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number.")

    if winner("X"):
        show_board()
        print("🎉 Congratulations! You Win.")
        break

    if board_full():
        show_board()
        print("🤝 Match Draw.")
        break

    print("\nComputer is thinking...\n")
    computer_move()

    if winner("O"):
        show_board()
        print("💻 Computer Wins!")
        break

    if board_full():
        show_board()
        print("🤝 Match Draw.")
        break
