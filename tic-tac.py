def print_board(board):
    print("Доступные ячейки:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    
    print("\nТекущее состояние доски:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Игрок {current_player}, введите номер ячейки (1-9):")
        
        try:
            cell = int(input()) - 1
            row, col = divmod(cell, 3)

            if cell < 0 or cell > 8 or board[row][col] != " ":
                print("Неверный ввод. Пожалуйста, выберите пустую ячейку от 1 до 9.")
                continue
        except (ValueError, IndexError):
            print("Неверный ввод. Пожалуйста, введите число от 1 до 9.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Поздравляем! Игрок {winner} выиграл!")
            break

        if is_board_full(board):
            print_board(board)
            print("Игра окончена вничью!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
