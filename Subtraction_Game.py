from math import inf


def minimax(state:int, depth:int, maximizing_player:bool) -> int :
    """
    A recursive function implementing the Minimax search algorithm on a Subtraction Game.
    Reference 
    
    Parameters:
    state (int): The current number of stones.
    depth (int): The depth of the search tree.
    maximizing_player (bool): A boolean indicating whether the current player is the maximizing player.

    Returns:
    int: The optimal score for the current player.

    The function also prints a tuple of [state, depth, maximizing_player, best_score, best_move] 
    before returning the optimal score for the current player.
    """
    
    # There is no stone left, game is over(Also the last step in recursioin)
    if state == 0:
        result = (state, depth, maximizing_player, 1 if maximizing_player else -1, 0)
        print(result)
        return(result[3])
    
    # The depth limit is reached, return a tie(Also the last step in recursioin)