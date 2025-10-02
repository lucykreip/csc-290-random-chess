import chess
import random

def main ():
    print("Welcome to Chess!")
    botColor = input("Should the computer player be black or white(b or w) ?")
    startingFEN = input("Starting FEN position? (hit ENTER for standard starting postion)")
    # initializing board
    if (startingFEN == ""):
        board = chess.Board()
    else:
        board = chess.Board(startingFEN)

    botName = ""
    playerName = "" 
    
    if (botColor == "w"):
       botColor = chess.WHITE
       botName = "Bot(as white)"
       playerName = "Player(as black)"
       print(botName)
       print(playerName)
    elif (botColor == "b"):
        botColor = chess.BLACK
        botName = "Bot(as black)"
        playerName = "Player(as white)"
        print(botName)
        print(playerName)

    print("Printing Initial Board......")
    print(board)
    print("-----------------")
    while not board.is_game_over() :
        # if its the bots turn 
        if (board.turn == botColor):
            moveList =list(board.legal_moves)
            randIndex = random.randint(0,len(moveList)-1)
            randMove = moveList[randIndex]
            print("Bot moves to: ", randMove)
            board.push(randMove)
            # isbotMove isn't needed since doing board.push alr flips the turns 
        else:
            print(board)
            move = input("Input Your Move: ")
            board.push_uci(move) 

    print("Game Results:" , board.result())
    board.reset()



            
    # TO DO : All we need to do is randomize from the list of legal moves for the bot  within the while loop !  

    # print(board)
    # print(botName)
    # print(playerName)
    # board.turn = False
    # True == white and False == black 
    # print(board.turn)



if __name__ == "__main__":
    main()

