import chess
import random
import datetime

def main ():

    print("-"*20)
    print(f"\tWelcome to Chess!")
    print("-"*20)
    print(f"Time: {datetime.datetime.now()}")
    botColor = input("Computer player? (w=white/b=black) ")
    startingFEN = input("Starting FEN position? (hit ENTER for standard starting postion) ")
    board = None
    if (startingFEN == ""):
        board = chess.Board()
    else:
        board = chess.Board(startingFEN)
    
    botName = ""
    playerName = "" 
    
    if (botColor == "w"):
       botColor = chess.WHITE
       botName = "Bot (as white)"
       playerName = "Black"
    #    print(botName)
    #    print(playerName)
    elif (botColor == "b"):
        botColor = chess.BLACK
        botName = "Bot (as black)"
        playerName = "White"
        # print(botName)
        # print(playerName)

    print("Printing Initial Board......")
    print(board)
    print("-----------------")
    while not board.is_game_over() :
        # if its the bots turn 
        if (board.turn == botColor):
            moveList = list(board.legal_moves)
            randIndex = random.randint(0,len(moveList)-1)

            botMove = moveList[randIndex]

            for move in moveList:
                if board.is_capture(move):
                    botMove = move
                    break
                    
            print(f"{botName}: {botMove}")

            board.push(botMove)
            print(f"New FEN position: {board.fen()}")
        else:
            moveList = list(board.legal_moves)

            playerInput = input(f"{playerName}: ")
            
            playerMove = None

            try:
                playerMove = chess.Move.from_uci(playerInput)
            except:
                print("Make sure your input is in UCI format!")
                playerInput = input(f"{playerName}: ")

            if playerMove not in moveList:
                print("That move is not legal! Try again?")
            else:
                board.push(playerMove)
                print(f"New FEN position: {board.fen()}")
        print(board)
        

    print(board)
    print(f"Game Result: {board.result()}")

    board.reset()


if __name__ == "__main__":
    main()

