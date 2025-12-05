# v -> choose players
# v ->create the board
# v ->choose initial player
# v -> until someone wins, check the winner
#   show the board
#   choose location, mark it
#   toogle active player





def main():
    #create the board
    board = [
        [None,None,None],
        [None, None, None],
        [None, None, None]
    ]

    #Choose initial player
    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X","O"]

    #until someone wins
    while not find_winner(board):
        #show board
        player = players[active_player_index]

        announce_turn(player)
        show_board(board)
        input("paused")dkq

def show_board(board):
    for row in board:
        print("|")
        for cell in row:
            print(cell, end = " | ")

        print()



def announce_turn(player):
    print()
    print(f"its {player}'s turn. Here is the board:")
    print()


def find_winner(board):
    #TODO: implement how we check for the winner
    return False





if __name__ == '__main__':
    main()