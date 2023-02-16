pos = ["1","2","3","4","5","6","7","8","9"]
replay = True

def printGameBoard():
    print("     |     |     ")
    print(f"  {pos[0]}  |  {pos[1]}  |  {pos[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {pos[3]}  |  {pos[4]}  |  {pos[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {pos[6]}  |  {pos[7]}  |  {pos[8]}  ")
    print("     |     |     ")

def whoWon(symbol):
    if symbol == "X":
        print("Player 2 has won!")
    else:
        print("Player 1 has won!")


def getInput(num):
    print("Player " + str(num) + " is your turn: ", end= "")
    while True:
        try:
            move = int(input()) - 1

            if pos[move] != " ":
                print("Someone has played there, choose some other position: ", end= "")
            else:
                return move
        except ValueError:
            print("Wrong input! Choose a position of number 1 to 9: ", end= "")
            

def player(num):
    move = getInput(num)
    if num == 1:
        pos[move] = "O"    
    else:
        pos[move] = "X"

def gameStarts():
    print("\n\nGame begins!\n")
    for x in range(len(pos)):
        pos[x] = " "

def gameEnded():
    for x in range(0,7,3):
        if pos[x] != " " and pos[x] == pos[x+1] and pos[x+1] == pos[x+2]:  #horizontal win condition
            whoWon(pos[x])
            return True
    for x in range(0,3):
        if pos[x] != " " and pos[x] == pos[x+3] and pos[x+3] == pos[x+6]:  #vertical win condiditon
            whoWon(pos[x])
            return True
    if pos[4] != " " and ((pos[0] == pos[4] and pos[4] == pos[8]) or (pos[2] == pos[4] and pos[4] == pos[6])):  #checks diagonial win condition, uses center symbol (used by both) to check for winner. 
        whoWon(pos[4])
        return True
    
    
print("Welcome to TicTacToe Game! \n \nAs you see bellow those are the pos number to play.\nWhen asked to play simply input one of those!")
printGameBoard()
gameStarts()

while replay:
    

    for x in range(0,5):
        player(1)
        printGameBoard()
        if gameEnded() == True:
            break
        if x == 4:
            print("Game is a Draw!")
            break
        player(2)
        printGameBoard()
        if gameEnded() == True:
            break            
    
    replay = input("Want to play again? (yes/no): ")
    if replay == "Yes" or replay == "yes":
        replay = True
        gameStarts()
        printGameBoard()
    else:
        replay = False
        

