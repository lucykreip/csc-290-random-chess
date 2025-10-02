import chess
import random

def main ():

    print("Welcome to Chess!")
    botColor = input("Should the computer player be black or white(b or w)? ")
    startingFEN = input("Starting FEN position? (hit ENTER for standard starting postion) ")
    board = None
    if (startingFEN == ""):
        board = chess.Board()
    else:
        board = chess.Board(startingFEN)
    

    isOver = False
    botName = ""
    playerName = "" 
    isBotMove = None
    if (botColor == "w"):
       botColor = chess.WHITE
       botName = "Bot (as white)"
       playerName = "Black"
    #    isbotMove = board.turn(botColor)
       isBotMove = True
       board.turn = isBotMove
    elif (botColor == "b"):
        botColor = chess.BLACK
        botName = "Bot (as black)"
        playerName = "White"
        isBotMove = False
        board.turn = not isBotMove

    
    print(board)

    while (isOver == False) :
        if (isBotMove == True):

            moveList =list(board.legal_moves)

            randIndex = random.randint(0,len(moveList)-1)

            botMove = moveList[randIndex]

            for move in moveList:
                if board.is_capture(move):
                    botMove = move
                    break
                    
            print(f"{botName}: {botMove}")

            # when turn is done, push the move to the board, change who's turn it is so the board
            # knows, and update the boolean isBotMove
            board.push(botMove)
            board.turn = not isBotMove
            isBotMove = False 
            print("New FEN position: " + board.fen())
        else:
            moveList =list(board.legal_moves)

            playerInput = input(f"{playerName}: ")
            
            try:
                playerMove = chess.Move.from_uci(playerInput)
            except:
                print("Make sure your input is in UCI format!")
                playerInput = input(f"{playerName}: ")

            if playerMove not in moveList:
                print("That move is not legal! Try again?")
            else:
                board.push(playerMove)
                board.turn = isBotMove
                isBotMove = True
                print("New FEN position: " + board.fen())
        print(board)
        

        # print(f"Printing isBotMove: {isBotMove}")
        


            
    # TO DO : All we need to do is randomize from the list of legal moves for the bot  within the while loop !  

    print(board)
    # print(botName)
    # print(playerName)
    # board.turn = False
    # True == white and False == black 
    print(board.turn)



if __name__ == "__main__":
    main()

