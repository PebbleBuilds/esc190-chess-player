import time

class Queue:
 def __init__(self):
  self.store = []

 def enqueue(self,x):
  self.store = self.store + [x]

 def dequeue(self):
  temp = list(self.store)
  #print("Temp is",temp)
  self.store = []
  for i in range(1,len(temp)):
   self.store = self.store + [temp[i]]
  return temp[0]

 def empty(self):
  if len(self.store) == 0:
   return True
  else:
   return False

class tree:
 def __init__(self,x):
        self.store = [x,[]]

 def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

 def Print_DepthFirst(self):
     print(self.store[0])
     if self.store[1] == []:
      return True
     else:
      for i in self.store[1]:
       i.Print_DepthFirst()

 def Get_Subtrees(self):
     r = []
     for i in self.store[1]:
         r += [i]
     return r


 def Get_Data(self):
     return self.store

 def Get_LevelOrder(self):
     ans = []
     q = Queue()
     q.enqueue(self.store)
     while q.empty() != True:
      r = q.dequeue()
      ans = ans + [r[0]]
      for i in r[1]:
       q.enqueue(i.Get_Data())
     return ans


def GetPlayerPositions(board,player):
    b = list(board)
    positions = []
    if player == "white":
        min = 9
        max = 16
    else:
        min = 19
        max = 26
    for i in range(0,len(b)):
        if b[i]>min and b[i]<max:
            positions += [i]
    return positions


def getColour(board,value):
    b = list(board)
    if b[value] == 0:
        return 0;
    elif b[value] >19:
        return "black"
    else:
        return "white"

def Left(pos):
    return pos + 1

def Right(pos):
    return pos - 1

def Up(pos):
    return pos + 8

def Down(pos):
    return pos - 8

def GetPieceLegalMoves(board,position):
    b = list(board)
    moves = []
    rightSpace = position % 8
    leftSpace = 7 - (position % 8)
    upSpace = 7 - (position // 8)
    downSpace = position // 8

    colour = getColour(b,position)

    #white pawn
    if b[position] == 10:
        if b[Up(position)] == 0:
            moves += [Up(position)]
        if leftSpace != 0:
            if b[Up(Left(position))] > 19:
                moves += [Up(Left(position))]
        if rightSpace != 0:
            if b[Up(Right(position))] > 19:
                moves += [Up(Right(position))]
    #black pawn
    elif b[position] == 20:
        if b[Down(position)] == 0:
            moves += [Down(position)]
        if leftSpace != 0:
            if getColour(b,Left(Down(position))) == "white":
                moves += [Left(Down(position))]
        if rightSpace != 0:
            if getColour(b,Right(Down(position))) == "white":
                moves += [Right(Down(position))]

    #knight
    elif b[position] % 10 == 1:

        if leftSpace > 0 and upSpace > 1:
            if colour != getColour(b,Left(Up(Up(position)))):
                moves += [Left(Up(Up(position)))]
        if rightSpace > 0 and upSpace > 1:
            if colour != getColour(b,Right(Up(Up(position)))):
                moves += [Right(Up(Up(position)))]
        if leftSpace > 0 and downSpace > 1:
            if colour != getColour(b,Left(Down(Down(position)))):
                moves += [Left(Down(Down(position)))]
        if rightSpace > 0 and downSpace > 1:
            if colour != getColour(b,Right(Down(Down(position)))):
                moves += [Right(Down(Down(position)))]
        if leftSpace > 1 and upSpace > 0:
            if colour != getColour(b,Left(Left(Up(position)))):
                moves += [Left(Left(Up(position)))]
        if rightSpace > 1 and upSpace > 0:
            if colour != getColour(b,Right(Right(Up(position)))):
                moves += [Right(Right(Up(position)))]
        if leftSpace > 1 and downSpace > 0:
            if colour != getColour(b,Left(Left(Down(position)))):
                moves += [Left(Left(Down(position)))]
        if rightSpace > 1 and downSpace > 0:
            if colour != getColour(b,Right(Right(Down(position)))):
                moves += [Right(Right(Down(position)))]

    #bishops
    elif b[position] % 10 == 2:
        #topleft
        cursor = position
        while True:
            leftSpace = 7 - (cursor % 8)
            upSpace = 7 - (cursor // 8)
            if leftSpace > 0 and upSpace > 0 and colour != getColour(b,cursor+9):
                moves += [cursor + 9]
                if colour == "white":
                    if getColour(b,Left(Up(cursor))) == "black":
                        break
                if colour == "black":
                    if getColour(b,Left(Up(cursor))) == "white":
                        break
                cursor = cursor + 9
            else:
                break
        #top right
        cursor = position
        while True:
            rightSpace = (cursor % 8)
            upSpace = 7 - (cursor // 8)
            if rightSpace > 0 and upSpace > 0 and colour != getColour(b,cursor + 7):
                moves += [cursor + 7]
                if colour == "white":
                    if getColour(b,cursor+7) == "black":
                        break
                if colour == "black":
                    if getColour(b,cursor+7) == "white":
                        break
                cursor = cursor + 7
            else:
                break
        #bottom left
        cursor = position
        while True:
            leftSpace = 7 - (cursor % 8)
            downSpace = cursor // 8
            if leftSpace > 0 and downSpace > 0 and colour != getColour(b,cursor - 7):
                moves += [cursor - 7]
                if colour == "white":
                    if getColour(b,cursor - 7) == "black":
                        break
                if colour == "black":
                    if getColour(b,cursor - 7) == "white":
                        break
                cursor = cursor - 7
            else:
                break
        #bottom right
        cursor = position
        while True:
            rightSpace = (cursor % 8)
            downSpace = cursor // 8
            if rightSpace > 0 and downSpace > 0 and colour != getColour(b,cursor - 9):
                moves += [cursor - 9]
                if colour == "white":
                    if getColour(b,cursor - 9) == "black":
                        break
                if colour == "black":
                    if getColour(b,cursor - 9) == "white":
                        break
                cursor = cursor - 9
            else:
                break

    #rooks




    elif b[position] % 10 == 3:
        cursor = position
        while True:
            upSpace = 7 - (cursor // 8)
            if upSpace > 0 and getColour(b, Up(cursor)) != colour:
                moves += [Up(cursor)]
                if getColour(b, Up(cursor)) != 0:
                    break
                cursor = Up(cursor)
            else:
                break
        cursor = position
        while True:
            rightSpace = (cursor % 8)
            if rightSpace > 0 and getColour(b, Right(cursor)) != colour:
                moves += [Right(cursor)]
                if getColour(b, Right(cursor)) != 0:
                    break
                cursor = Right(cursor)
            else:
                break
        cursor = position
        while True:
            downSpace = cursor // 8
            if downSpace > 0 and getColour(b, Down(cursor)) != colour:
                moves += [Down(cursor)]
                if getColour(b, Down(cursor)) != 0:
                    break
                cursor = Down(cursor)
            else:
                break
        cursor = position
        while True:
            leftSpace = 7 - (cursor % 8)
            if leftSpace > 0 and getColour(b, Left(cursor)) != colour:
                moves += [Left(cursor)]
                if getColour(b, Left(cursor)) != 0:
                    break
                cursor = Left(cursor)
            else:
                break

 #queen
    elif b[position] % 10 == 4:
        # topleft
        cursor = position
        while True:
            leftSpace = 7 - (cursor % 8)
            upSpace = 7 - (cursor // 8)
            if leftSpace > 0 and upSpace > 0 and colour != getColour(b, cursor + 9):
                moves += [cursor + 9]
                if colour == "white":
                    if getColour(b, Left(Up(cursor))) == "black":
                        break
                if colour == "black":
                    if getColour(b, Left(Up(cursor))) == "white":
                        break
                cursor = cursor + 9
            else:
                break
        # top right
        cursor = position
        while True:
            rightSpace = (cursor % 8)
            upSpace = 7 - (cursor // 8)
            if rightSpace > 0 and upSpace > 0 and colour != getColour(b, cursor + 7):
                moves += [cursor + 7]
                if colour == "white":
                    if getColour(b, cursor + 7) == "black":
                        break
                if colour == "black":
                    if getColour(b, cursor + 7) == "white":
                        break
                cursor = cursor + 7
            else:
                break
        # bottom left
        cursor = position
        while True:
            leftSpace = 7 - (cursor % 8)
            downSpace = cursor // 8
            if leftSpace > 0 and downSpace > 0 and colour != getColour(b, cursor - 7):
                moves += [cursor - 7]
                if colour == "white":
                    if getColour(b, cursor - 7) == "black":
                        break
                if colour == "black":
                    if getColour(b, cursor - 7) == "white":
                        break
                cursor = cursor - 7
            else:
                break
        # bottom right
        cursor = position
        while True:
            rightSpace = (cursor % 8)
            downSpace = cursor // 8
            if rightSpace > 0 and downSpace > 0 and colour != getColour(b, cursor - 9):
                moves += [cursor - 9]
                if colour == "white":
                    if getColour(b, cursor - 9) == "black":
                        break
                if colour == "black":
                    if getColour(b, cursor - 9) == "white":
                        break
                cursor = cursor - 9
            else:
                break
     #rook movement
        cursor = position
        while True:
            upSpace = 7 - (cursor // 8)
            if upSpace > 0 and getColour(b, Up(cursor)) != colour:
                moves += [Up(cursor)]
                if getColour(b, Up(cursor)) != 0:
                    break
                cursor = Up(cursor)
            else:
                break
        cursor = position
        while True:
            rightSpace = (cursor % 8)
            if rightSpace > 0 and getColour(b, Right(cursor)) != colour:
                moves += [Right(cursor)]
                if getColour(b, Right(cursor)) != 0:
                    break
                cursor = Right(cursor)
            else:
                break
        cursor = position
        while True:
            downSpace = cursor // 8
            if downSpace > 0 and getColour(b, Down(cursor)) != colour:
                moves += [Down(cursor)]
                if getColour(b, Down(cursor)) != 0:
                    break
                cursor = Down(cursor)
            else:
                break
        cursor = position
        while True:
            leftSpace = 7 - (cursor % 8)
            if leftSpace > 0 and getColour(b, Left(cursor)) != colour:
                moves += [Left(cursor)]
                if getColour(b, Left(cursor)) != 0:
                    break
                cursor = Left(cursor)
            else:
                break

#king
    elif b[position] % 10 == 5:
        cursor = position
        if leftSpace > 0 and getColour(b, Left(cursor)) != colour:
            moves += [Left(cursor)]
        if downSpace > 0 and getColour(b, Down(cursor)) != colour:
            moves += [Down(cursor)]
        if rightSpace > 0 and getColour(b, Right(cursor)) != colour:
            moves += [Right(cursor)]
        if upSpace > 0 and getColour(b, Up(cursor)) != colour:
            moves += [Up(cursor)]
        if rightSpace > 0 and downSpace > 0 and colour != getColour(b, cursor - 9):
            moves += [cursor - 9]
        if leftSpace > 0 and upSpace > 0 and colour != getColour(b, cursor + 9):
            moves += [cursor + 9]
        if leftSpace > 0 and downSpace > 0 and colour != getColour(b, cursor - 7):
            moves += [cursor - 7]
        if rightSpace > 0 and upSpace > 0 and colour != getColour(b, cursor + 7):
            moves += [cursor + 7]

    return moves

def IsPositionUnderThreat(board,position,player):
    if player == "white":
        opponent = "black"
    else:
        opponent = "white"
    for i in range(0,len(board)):
        if getColour(board,i) == opponent:
            for j in GetPieceLegalMoves(board,i):
                if j == position:
                    return True
    return False

def genBoard():
    board = []
    for i in range(0,64):
        board = board + [0]
    for i in range(8,16):
        board[i] = 10
    for i in range(48,56):
        board[i] = 20
    board[0] = 13
    board[1] = 11
    board[2] = 12
    board[3] = 15
    board[4] = 14
    board[5] = 12
    board[6] = 11
    board[7] = 13

    board[0+56] = 13+10
    board[1+56] = 11+10
    board[2+56] = 12+10
    board[3+56] = 15+10
    board[4+56] = 14+10
    board[5+56] = 12+10
    board[6+56] = 11+10
    board[7+56] = 13+10
    return board

def printBoard(board):
    for i in range(7,-1,-1):
        row = []
        for j in range(8*i+7,8*(i)-1,-1):
            if board[j] == 10:
                piece = 'p'
            elif board[j] == 11:
                piece = 'n'
            elif board[j] == 12:
                piece = 'b'
            elif board[j] == 13:
                piece = 'r'
            elif board[j] == 14:
                piece = 'q'
            elif board[j] == 15:
                piece = 'k'
            #black
            elif board[j] == 20:
                piece = 'P'
            elif board[j] == 21:
                piece = 'N'
            elif board[j] == 22:
                piece = 'B'
            elif board[j] == 23:
                piece = 'R'
            elif board[j] == 24:
                piece = 'Q'
            elif board[j] == 25:
                piece = 'K'
            else:
                piece = ' '
            row += [piece]
        print(row)
    print()

    for i in range(7, -1, -1):
        row = []
        for j in range(7 + 8 * i, 8 * i - 1, -1):
            row = row+[j]
        print(row)

def check(board,player):
    cursor = 0
    if player == "white":
        king = 15
    else:
        king = 25
    while True:
        if board[cursor] == king:
            return IsPositionUnderThreat(board,cursor,player)
        elif cursor >62:
            print("Check function couldn't find the king")
            return None
        else:
            cursor += 1

def checkmate(board,player): #doesnt check for block/capture
    cursor = 0
    if player == "white":
        king = 15
    else:
        king = 25
    while True:
        if board[cursor] == king:
            if IsPositionUnderThreat(board,cursor,player) == False:
                return False
            else:
                kingMoves = GetPieceLegalMoves(board,cursor)
                for i in kingMoves:
                    if IsPositionUnderThreat(board,cursor,i) == False:
                        return False
                return True

        elif cursor >63:
            print("Checkmate function couldn't find the king")
            return None
        else:
            cursor += 1

def stalemate(board,player):
    pieces = GetPlayerPositions(board,player)
    for i in pieces:
        if GetPieceLegalMoves(board,i) != []:
            return False
    return True

def evaluator(board,player):
    if player == "white":
        opponent = "black"
    else:
        opponent = "white"
    pieces = GetPlayerPositions(board,player)
    oppPieces = GetPlayerPositions(board,opponent)
    score = 0.0
    boardWeight = []
    boardWeight += [0, 0, 0, 0, 0, 0, 0, 0]
    boardWeight += [0, 0, 0, 0, 0, 0, 0, 0]
    boardWeight += [0, 0, 1, 1, 1, 1, 0, 0]
    boardWeight += [0, 0, 1, 1, 1, 1, 0, 0]
    boardWeight += [0, 0, 1, 1, 1, 1, 0, 0]
    boardWeight += [0, 0, 1, 1, 1, 1, 0, 0]
    boardWeight += [0, 0, 0, 0, 0, 0, 0, 0]
    boardWeight += [0, 0, 0, 0, 0, 0, 0, 0]
    pawnCols = []
    oppPawnCols = []
    for i in pieces:
        pawnInCol = False
        val = board[i]
        if val % 10 == 0:
            score += 1.0 * (1 + 0.02 * boardWeight[i])
            for j in pawnCols: #double pawn checker
                if j == i%8:
                    score -= 0.1
                    pawnInCol = True
                if pawnInCol == False:
                    pawnCol += [j]
            if i // 8 == 7:
                score += 8.0
        elif val % 10 == 1:
            score += 3.0 * (1 + 0.02 * boardWeight[i])
        elif val % 10 == 2:
            score += 3.25* (1 + 0.01 * boardWeight[i])
        elif val % 10 == 3:
            score += 5.0#* (1+0.001*len(GetPieceLegalMoves(board,i)))
        elif val % 10 == 4:
            score += 9.0 #* (1+0.001*len(GetPieceLegalMoves(board,i)))
        elif val % 10 == 5:
            score += 900.0
    for i in oppPieces:
        val = board[i]
        pawnInCol = False
        if val % 10 == 0:
            score -= 1.0* (1 + 0.02 * boardWeight[i])
            if i // 8 == 0:
                score += 8.0
            for j in oppPawnCols: #double pawn checker
                if j == i%8:
                    score += 0.1
                    pawnInCol = True
                if pawnInCol == False:
                    oppPawnCols += [j]
        elif val % 10 == 1:
            score -= 3.0* (1 + 0.02 * boardWeight[i])
        elif val % 10 == 2:
            score -= 3.25* (1 + 0.001 * boardWeight[i])
        elif val % 10 == 3:
            score -= 5.0#* (1+0.001*len(GetPieceLegalMoves(board,i)))
        elif val % 10 == 4:
            score -= 9.0#* (1+0.01*len(GetPieceLegalMoves(board,i)))
        elif val % 10 == 5:
            score -= 900.0

        #passed pawns
        for pawn in pawnCols:
            passed = True
            for oPawn in oppPawnCols:
                if pawn == oPawn or pawn == oPawn+1 or pawn == oPawn-1:
                    passed = False
                    break
            if passed == True:
                score += 6

        for oPawn in oppPawnCols:
            passed = True
            for pawn in pawnCols:
                if oPawn == pawn or oPawn == pawn+1 or oPawn == pawn-1:
                    passed = False
                    break
            if passed == True:
                score -= 6

    return score

def getLegalMoves(board,player):
    possibleMoves = []
    myPieces = GetPlayerPositions(board, player)
    for i in myPieces:
        legalMoves = GetPieceLegalMoves(board, i)
        for j in legalMoves:
            fakeBoard = list(board)
            fakeBoard[j] = fakeBoard[i]
            fakeBoard[i] = 0
            if check(fakeBoard,player) == False:
                possibleMoves += [[i, j]]
    return possibleMoves

def predictor(board,move,player,opponent):
    bestOpponentMoveRating = 9999.9
    myMoveBoard = list(board)
    myMoveBoard[move[1]] = myMoveBoard[move[0]]
    myMoveBoard[move[0]] = 0
    opponentMoves = getLegalMoves(myMoveBoard,opponent)
    for i in opponentMoves:
        oppMoveBoard = list(myMoveBoard)
        oppMoveBoard[i[1]] = oppMoveBoard[i[0]]
        oppMoveBoard[i[0]] = 0
        rating = evaluator(oppMoveBoard,player)
        if rating < bestOpponentMoveRating:
            bestOpponentMoveRating = rating #best move for opponent - worst move for us
            bestOpponentBoard = list(oppMoveBoard)
    return [bestOpponentMoveRating,bestOpponentBoard]


def movePlayer(board,move):
    b = list(board)
    b[move[1]] = b[move[0]]
    b[move[0]] = 0
    return b

def bestBranch(tre,player,start):
    #print(tre.Get_LevelOrder())
    possible = tre.Get_Subtrees()
    if possible == []:
        print("error")
        return("error")
    possibleBoards = []
    bestMoveRating = -99999
    #print(possible)
    for i in possible:
        possibleBoards += [i.Get_Data()[0]]
    #print(possibleBoards)
    for i in range(0,len(possibleBoards)):
        rating = evaluator(possibleBoards[i],player)
        if rating > bestMoveRating:
            bestMoveRating = rating
            bestMoveIndex = i
        end = time.time()
        #print(end-start)
        if end - start > 9.5:
            break
    return [possible[bestMoveIndex],bestMoveRating]


def chessPlayer(board,player):
    start = time.time()
    candidateMoves = []
    status = True
    if player == "white":
        opponent = "black"
    else:
        opponent = "white"
    possibleMoves = getLegalMoves(board, player)
    possibleBoards = []
    for i in possibleMoves:
        possibleBoards = movePlayer(board,i)
        candidateMoves += [[i,0.0]]
    #print(candidateMoves)
    boardTree = tree(board)
    if possibleMoves == []:
        status = False
        return (False,[],[],[])

    #make tree!
    #print("First Layer:")
    for i in possibleMoves:
        if time.time() - start > 6.66:
            break
        newBoardOne = movePlayer(board,i)
        #print(newBoardOne)
        treeLayerOne = tree(newBoardOne)
        #print("Second Layer:")
        for j in getLegalMoves(newBoardOne,opponent):
            newBoardTwo = movePlayer(newBoardOne,j)
            #print(newBoardTwo)
            treeLayerTwo = tree(newBoardTwo)
            #print("Third Layer")
            for k in getLegalMoves(newBoardTwo,player):
                newBoardThree = movePlayer(newBoardTwo,k)
                #print(newBoardThree)
                treeLayerThree = tree(newBoardThree)
                treeLayerTwo.AddSuccessor(treeLayerThree)
            treeLayerOne.AddSuccessor(treeLayerTwo)
        boardTree.AddSuccessor(treeLayerOne)
    #print(boardTree.Get_LevelOrder())

    # find best branches! 2
    possibleTrees = boardTree.Get_Subtrees()
    # print(possibleTrees)
    bestMoveRating = -9999
    for i in range(0, len(possibleTrees)):
        bestOpponentMoveRating = 9999
        # print(i)
        # print(i.Get_LevelOrder())
        possibleOpponentMoves = possibleTrees[i].Get_Subtrees()
        if possibleOpponentMoves == []:
            return [True,possibleMoves[i],candidateMoves,boardTree]
        # print("This ran")
        for j in possibleOpponentMoves:
            myMove = bestBranch(j, player, start)
            if myMove == "error":
                #print("ERROR!")
                continue
                bestMoveIndex = i
                bestMove = possibleMoves[bestMoveIndex]
                candidateMoves[i][1] += bestMoveRating
                return [True, bestMove, candidateMoves, boardTree]
            if myMove[1] < bestOpponentMoveRating:
                bestOpponentMoveRating = myMove[1]
            if time.time() - start > 9.5:
                #print("out of time")
                break
        candidateMoves[i][1] += bestOpponentMoveRating
        if bestOpponentMoveRating > bestMoveRating:
            bestMoveRating = bestOpponentMoveRating
            bestMoveIndex = i
        if time.time() - start > 9.5:
            #print("out of time")
            break
    bestMove = possibleMoves[bestMoveIndex]
    candidateMoves[i][1] += bestMoveRating
    return[True,bestMove,candidateMoves,boardTree]




    #print(boardTree.Get_LevelOrder())



def selfChess():
    b = genBoard()

    player = "white"
    while True:
        printBoard(b)
        print("Thinking:")
        start = time.time()
        play = chessPlayer(b,player)
        candMoves = play[2]
        tre = play[3]
        move = play[1]
        end = time.time()
        print("Time:",end-start)
        print("move:",move)
        #print("candidates:",candMoves)
        #print("tree:",play[3].Get_LevelOrder())
        b[move[1]] = b[move[0]]
        b[move[0]] = 0
        if player == "white":
            player = "black"
        else:
            player = "white"






def playChess():
    b = genBoard()
    #printBoard(b)
    player = "white"
    while True:
        if player == "black":
            print("Thinking:")
            move = chessPlayer(b,player)[1]
            print("move:",move)
            b[move[1]] = b[move[0]]
            b[move[0]] = 0
            player = "white"
            continue
        printBoard(b)
        legalPiece = False
        legalMove = False
        print("%s to move: which piece?" %player)
        piece = int(input())
        for i in GetPlayerPositions(b,player):
            if piece == i:
                legalPiece = True
        if legalPiece == False:
            continue
        print("Legal moves:",GetPieceLegalMoves(b,piece))
        print("Where?")
        move = int(input())
        for j in GetPieceLegalMoves(b,piece):

            if move == j:
                legalMove = True
        if legalMove == False:
            continue
        print("move made")
        checkBoard = list(b)
        temp = checkBoard[piece]
        checkBoard[piece] = 0
        checkBoard[move] = temp
        if check(checkBoard,player) == True:
            print("You are in check! Make another move")
            continue
        temp = b[piece]
        b[piece] = 0
        b[move] = temp
        if player == "white":
            player = "black"
        else:
            player = "white"
        #if checkmate(b,player):
        #    print("%s is in checkmate!"%player)
        #    return 0
        if stalemate(b,player):
            print("%s is in stalemate!"%player)
            return 0
        if check(b,player):
            print("%s is in check!"%player)


playChess()
#b = genBoard()
#print(GetPieceLegalMoves(b,11))