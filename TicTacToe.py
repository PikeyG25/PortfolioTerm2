#Parker Gowans
#12/18
#TicTacToe

#Global Constants
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9

def display_instructions():
        print(
            """This is how you play,
    You need to find out who is going first, you or the computer.
    Once you find out who is going first, you need to find out who is X's and who is O's.
    A board will display and there will be nine spaces available to go in, you then
    place a piece down strategically, then the other person goes. You keep going till
    you get three pieces in a row or you and the other person tie.

    You will need to make your move by entering in number 0-8.

                                0 | 1 | 2
                                --------
                                3 | 4 | 5
                                --------
                                6 | 7 | 8







    """
            )

##############################################################################
def ask_yes_no(question):
    response = None
    while response not in("y","n"):
        response = input(question + " y or n").lower()
    return response


##############################################################################
def ask_number(question,low,high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high+1):
                break
            else:
                response = input(question)
        else:
            print("You must enter a number")
            response = input(question)
    return int(response)
            

##############################################################################
def pieces():
        """Decides who goes first"""
        go_first = ask_yes_no("Would you like to go first? (y/n)")
        if go_first == "y":
                ("You will go first")
                human = X
                computer = O
                         
        else:
                print("The computer will go first")
                computer = X
                human = O
        return computer, human

##############################################################################
def new_board():
        """Create a new game board"""
        board = []
        for squares in range(NUM_SQUARES):
                board.append(EMPTY)
        return board


##############################################################################
def display_board(board):
        """Display game board on screen"""
        print("\n\t", board[0],"|",board[1],"|", board[2])
        print("\t","---------")
        print("\n\t", board[3],"|",board[4],"|", board[5])
        print("\t","---------")
        print("\n\t", board[6],"|",board[7],"|", board[8])


##############################################################################
def legal_moves(board):
        """Create list of legal moves"""
        moves = []
        for square in range(len(board)):
                if board[square]==EMPTY:
                        moves.append(square)
        return moves


##############################################################################
def winner(board):
        """Determine the game winner"""
        WAYS_TO_WIN = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0,3,6),
                (1,4,7),
                (2,5,8),
                (0,4,8),
                (2,4,6))
        for row in WAYS_TO_WIN:
                if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                        winner = board[row[0]]
                        return winner

        if EMPTY not in board:
                return TIE
        
        return None

##############################################################################
def human_move(board):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where would you like to go? (0 - 8)", O, NUM_SQUARES)
        if move not in legal:
            print("That's not a legal move dummy")
    print("Okay...")
    return move
        
##############################################################################

def next_turn():
    """Switch turns."""
    if turn == x:
        return O
    else:
        return X

##############################################################################
def congrat_winner(winner, human, computer):
    """Congratulate the winner."""
    the_winner = winner
    if the_winner ==TIE:
        print(TIE)
        
    else:
        print(the_winner)
        
    if the_winner == computer:
        print("You got smoked by a computer??")
        
    elif the_winner == human:
        print("Wow, congrats, you beat computer.")
        
    elif the_winner == TIE:
        print("How do you tie to a computer?")
    
##############################################################################

def computer_move(board, computer, human):
    """Make computer move"""
    #Make a copy to work with since function will be changing list
    board = board[:]
    #The best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end="")


    #If computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #Done checking this move, undo it
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #Done checking this move, undo it
        board[move] = EMPTY
        
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
##############################################################################
def main(board):
    display_instructions()
    pieces()
    new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            human_move(board)
            display_board(board)
            next_turn()
        elif turn == computer:
            computer_move(board, computer, human)
            display_board(board)
            next_turn()
        else:
            the_winner()
            congrat_winner(winner, human, computer)
main(board)
