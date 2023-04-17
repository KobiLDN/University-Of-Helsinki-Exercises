def who_won(game_board: list):
    player1Score = 0
    player2Score = 0
    for list in game_board:
        for i in list:
            if i == 1:
                player1Score += 1
            elif i == 2:
                player2Score += 1
    print(player1Score)
    print(player2Score)
    if player1Score == player2Score:
        return 0
    elif player1Score > player2Score:
        return 1
    else:
        return 2

if __name__ == "__main__":
    game_board = [[1, 2, 1], [0, 0, 1], [2, 2, 0]]
    
    print(who_won(game_board))