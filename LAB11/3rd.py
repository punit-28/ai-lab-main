
board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")


def winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def minimax(maximizing, alpha, beta):
    result = winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if " " not in board:
        return 0

    if maximizing:
        best = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best


def ai_move():
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -float("inf"),
                            float("inf"))
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = "O"


def play():
    while True:
        display()

        if winner() or " " not in board:
            break

        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if pos < 0 or pos > 8 or board[pos] != " ":
                print("Invalid move!")
                continue

            board[pos] = "X"

        except ValueError:
            print("Enter a number from 1 to 9.")
            continue

        if winner() or " " not in board:
            break

        ai_move()
        print("AI played.")

    display()

    if winner():
        print(winner(), "wins!")
    else:
        print("Draw!")


play()
