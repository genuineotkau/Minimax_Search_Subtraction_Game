from math import inf


def minimax(state:int, depth:int, maximizing_player:bool) :
    """
    A recursive function implementing the Minimax search algorithm on a Subtraction Game.
    Score: 1 - maximizing player wins
    Score: 0 - a tie
    Score: -1 - minimizing player wins
    
    Parameters:
    state (int): The current number of stones.
    depth (int): The depth of the search tree.
    maximizing_player (bool): A boolean indicating whether the current player is the maximizing player.

    Returns:
    int: The optimal score for the current player.

    The function also prints a tuple of [state, depth, maximizing_player, best_score, best_move] 
    before returning the optimal score for the current player.
    """
    ## Baseline Part
    # There is no stone left, game is over(Also the last step in recursioin)
    if state == 0:
        result = (state, depth, maximizing_player, 1 if maximizing_player else -1, 0)
        return(result)
    
    # The depth limit is reached, return a tie(Also the last step in recursioin)
    if depth == 0:
        #The best move = 1 here doesn't mean anything, it's a garbage return since we don't know the game state
        result = (state, depth, maximizing_player, 0, 1)
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
        return(result)
    

def main():
    print(minimax(5, 5, True))
    print(minimax(7, 7, True))
    print(minimax(15, 5, True))

if __name__ == "__main__":
    main()      
            
        