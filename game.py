# v -> choose players
# v ->create the board
# v ->choose initial player
# v -> until someone wins, check the winner
# v ->   show the board
# v -> choose location, mark it
#   toggle active player


def main():
    # create the board
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # Choose initial player
    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    # until someone wins
    while not find_winner(board):
        # show board
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("not an option, try again")
            continue

        #toogle active player
        active_player_index = (active_player_index + 1) % len(players)

    print(f"game over! {player} has won with the board: ")
    show_board(board)



def choose_location(board, symbol):
    row = int(input("choose a row: "))
    column = int(input("choose a column: "))

    row -= 1
    column -= 1

    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print("|", end=' ')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"its {player}'s turn. Here is the board:")
    print()


def find_winner(board):
    # TODO: implement how we check for the winner
    return False


if __name__ == '__main__':
    main()
