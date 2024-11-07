# Dodatkowe (niewymagane)
# 13. Gramy w kółko i krzyżyk (3x3) - tekstowo

def display_board(board):
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            if column_index < 2:
                print(f' {column:2}', end="|")
            else:
                print(f'{column:2} ', end="")  
        print()  
        if row_index < 2:  
            print("-" * 11)

def check_score(board, current_player):
    for row in board:
        sign_counter = 0
        for column in row:
            if column == current_player:
                sign_counter += 1
        if sign_counter == 3:
            return True

    for col in range(3):
        sign_counter = 0
        for row in range(3):
            if board[row][col] == current_player:
                sign_counter += 1
        if sign_counter == 3:
            return True

    if board[0][0] == board[1][1] == board[2][2] == current_player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True

    return False

def is_move_possible(board, row, column):
    if board[row][column] == 'X' or board[row][column] == 'O':
        return False
    return True

def play_game(board):
    current_player = 'X'
    
    while True:
        display_board(board)
        print(f'Gracz ({current_player}) wykonuje ruch: podaj wiersz a następnie kolumnę (1-3)')
        
        row = int(input("wiersz: ")) - 1
        column = int(input("kolumna: ")) - 1

        if 0 <= row < 3 and 0 <= column < 3:
            if is_move_possible(board, row, column):
                board[row][column] = current_player

                if check_score(board, current_player):
                    display_board(board)
                    print(f"Koniec gry: wygrana gracza {current_player}")
                    break

                current_player = 'O' if current_player == 'X' else 'X'

            else:
                print("\nWybrane pole jest zajęte, wybierz inne.")
        else:
            print("Nieprawidłowy ruch. Podaj poprawne współrzędne (1-3).")

if __name__ == "__main__":
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    input("Kliknij ENTER, aby rozpocząć grę ")
    play_game(board)