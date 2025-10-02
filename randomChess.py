import chess
import random

def main ():
    print("Welcome to Chess!")
    botColor = input("Should the computer player be black or white(b or w) ?")
    startingFEN = input("Starting FEN position? (hit ENTER for standard starting postion)")
    board = None
    if (startingFEN == ""):
        board = chess.Board()
    else:
        board = chess.Board(startingFEN)
    isOver = False
    botName = ""
    playerName = "" 
    isbotMove = None
    if (botColor == "w"):
       botColor = chess.WHITE
       botName = "Bot(as white)"
       playerName = "Player(as black)"
    # isbotMove = board.turn(botColor)
       isbotMove = True
       board.turn = isBotMove
    elif (botColor == "b"):
        botColor = chess.BLACK
        botName = "Bot(as black)"
        playerName = "Player(as white)"
        isbotMove = False
        board.turn = not isBotMove

    
    print(board)

    while (isOver == False) :
        if (isbotMove == True):
            moveList =list(board.legal_moves)

            randIndex = random.randint(0,len(moveList)-1)

            randMove = moveList[randIndex]

            print(randMove)
            board.push(randMove)
            board.turn = not isbotMove
            isBotMove = False
        else:

            board.turn = isBotMove
            isBotMove = True


        isOver = True


            
    # TO DO : All we need to do is randomize from the list of legal moves for the bot  within the while loop !  

    print(board)
    print(botName)
    print(playerName)
    # board.turn = False
    # True == white and False == black 
    print(board.turn)



if __name__ == "__main__":
    main()

