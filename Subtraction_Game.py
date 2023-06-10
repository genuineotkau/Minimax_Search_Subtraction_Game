from math import inf


def minimax(state:int, depth:int, maximizing_player:bool) :
    """
    A recursive function implementing the Minimax search algorithm on a Subtraction Game.
    Score: 1 - maximizing player wins
    Score: -1 - minimizing player wins
    
    Parameters:
    state (int): The current number of stones.
    depth (int): The depth of the search tree.
    maximizing_player (bool): A boolean indicating whether the current player is the maximizing player.

    Returns:
    The function prints a tuple of [state, depth, maximizing_player, best_score, best_move] 
    before returning this tuple for the current player.
    """
    ## Baseline Part
    # There is no stone left, game is over(Also the last step in recursioin)
    if state == 0:
        result = (state, depth, maximizing_player, -1 if maximizing_player else 1, 0)
        print(result)
        return(result)
    
    if depth == 0:
        #This was my original implementation: result = (state, depth, maximizing_player, -1, 1)
        #result = (state, depth, maximizing_player, -1, 1)
        #The following one is the improved version:
        #If the move is divisible by 4, the maximizing player will lose
        #If the move is not divisible by 4, the maximizing player try to make the remaining stones divisible by 4
        if (state % 4 == 0):
            result = (state, depth, maximizing_player, -1 if maximizing_player else 1, 1)
        else:
            result = (state, depth, maximizing_player, 1 if maximizing_player else -1, (state % 4))
        print(result)
        return(result)
    
    ## Recursive Part
    if maximizing_player:
        max_score = -100
        best_move = -1
        for move in range(1, 4): # move 1-3 stones
            if (state - move) < 0:
                #If the move value is larger than state, we don't do anything
                #This if statement indicates that we already have the answer in previous rounds
                break
            new_score = minimax(state - move, depth - 1, False)[3]
            if new_score > max_score:
                max_score = new_score
                best_move = move
        result = (state, depth, maximizing_player, max_score, best_move)
        print(result)
        return(result)
    else:
        min_score = 100
        best_move = -1
        for move in range(1, 4): # move 1-3 stones
            if (state - move) < 0:
                #If the move value is larger than state, we don't do anything
                #This if statement indicates that we already have the answer in previous rounds
                break
            new_score = minimax(state - move, depth - 1, True)[3]
            if new_score < min_score:
                min_score = new_score
                best_move = move
        result = (state, depth, maximizing_player, min_score, best_move)
        print(result)
        return(result)

def main():
    minimax(5, 5, True)
    #minimax(7, 7, True)
    #minimax(8, 8, True)
    #minimax(15, 5, True)
    #minimax(12, 5, True)

if __name__ == "__main__":
    main()      
            
        