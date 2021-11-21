def whoseMove(lastPlayer, win):
    if lastPlayer == "white":
        if win == False:
            return "black"
        else:
            return "white"
    
    if lastPlayer == "black":
        if win == False:
            return "white"
        else:
            return "black"
