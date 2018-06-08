def insertMoves(board,listOfMoves):
 
    for move in listOfMoves:
        x=move[0]
        y=move[1]
        sign=move[2]
        board[y][x]=sign
    
