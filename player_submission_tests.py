#!/usr/bin/env python
import traceback
from isolation import Board, game_as_text
from test_players import RandomPlayer, HumanPlayer, Player
import platform
import MyTestCase

if platform.system() != 'Windows':
    import resource

from time import time, sleep


def play(yourAgent):
    #r = RandomPlayer()
    r = ABPlayer()
    p = yourAgent()
    MyTestCase.play(p, r)
    
def play_n_rounds(yourAgent):
    #r = RandomPlayer()
    r = ABPlayer()
    p = yourAgent()
    MyTestCase.play_n_rounds(p, r)
    

def correctOpenEvalFn(yourOpenEvalFn):
    print()
    try:
        sample_board = Board(RandomPlayer(), RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            ["Q1", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "Q2", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]
        sample_board.set_state(board_state, True)
        #test = sample_board.get_legal_moves()
        h = yourOpenEvalFn()
        print('OpenMoveEvalFn Test: This board has a score of %s.' % (h.score(sample_board, sample_board.get_active_player())))
    except NotImplementedError:
        print('OpenMoveEvalFn Test: Not implemented')
    except:
        print('OpenMoveEvalFn Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()

def beatRandom(yourAgent):

    """Example test you can run
    to make sure your AI does better
    than random."""

    print("")
    try:
        r = RandomPlayer()
        p = yourAgent()
        game = Board(r, p, 7, 7)
        output_b = game.copy()
        winner, move_history, termination = game.play_isolation(time_limit=1000, print_moves=True)
        print("\n", " total moves = ", game.move_count)
        print("\n", winner, " has won. Reason: ", termination)
        # Uncomment to see game
        # print game_as_text(winner, move_history, termination, output_b)
    except NotImplementedError:
        print('CustomPlayer Test: Not Implemented')
    except:
        print('CustomPlayer Test: ERROR OCCURRED')
        print(traceback.format_exc())
    
    print()

def minimaxTest(yourAgent, minimax_fn):
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states.
    Especially important to check alphabeta
    pruning"""

    # create dummy 5x5 board
    print("Now running the Minimax test.")
    print()
    try:
        def time_left():  # For these testing purposes, let's ignore timeouts
            return 10000

        player = yourAgent() #using as a dummy player to create a board
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            [" ", "X", "X", " ", "X", "X", " "],
            [" ", " ", "X", " ", " ", "X", " "],
            ["X", " ", " ", " ", " ", "Q1"," "],
            [" ", "X", "X", "Q2","X", " ", " "],
            ["X", " ", "X", " ", " ", " ", " "],
            [" ", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", " ", " ", " "]
        ]
        sample_board.set_state(board_state, True)

        test_pass = True

        expected_depth_scores = [(1, -2), (2, 0), (3, 3), (4, 4), (5, 1)]

        for depth, exp_score in expected_depth_scores:
            move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=True)
            if exp_score != score:
                print("Minimax failed for depth: ", depth)
                test_pass = False
            else:
                print("Minimax passed for depth: ", depth)

        if test_pass:
            player = yourAgent()
            sample_board = Board(player, RandomPlayer())
            # setting up the board as though we've been playing
            board_state = [
                [" ", " ", " ", " ", "X", " ", "X"],
                ["X", "X", "X", " ", "X", "Q2", " "],
                [" ", "X", "X", " ", "X", " ", " "],
                ["X", " ", "X", " ", "X", "X", " "],
                ["X", " ", "Q1", " ", "X", " ", "X"],
                [" ", " ", " ", " ", "X", "X", " "],
                ["X", " ", " ", " ", " ", " ", " "]
            ]
            sample_board.set_state(board_state, True)

            test_pass = True

            expected_depth_scores = [(1, -4), (2, 3), (3, -1), (4, 1), (5, -2)]

            for depth, exp_score in expected_depth_scores:
                move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=False)
                if exp_score != score:
                    print("Minimax failed for depth: ", depth)
                    test_pass = False
                else:
                    print("Minimax passed for depth: ", depth)

        if test_pass:
            print("Minimax Test: Runs Successfully!")

        else:
            print("Minimax Test: Failed")

    except NotImplementedError:
        print('Minimax Test: Not implemented')
    except:
        print('Minimax Test: ERROR OCCURRED')
        print(traceback.format_exc())

        
def alphabetaTest(yourAgent, alphbeta_fn):
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states.
    Especially important to check alphabeta
    pruning"""

    # create dummy 5x5 board
    print("Now running the Alphabeta test.")
    print()
    try:
        def time_left():  # For these testing purposes, let's ignore timeouts
            return 10000

        player = yourAgent() #using as a dummy player to create a board
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            [" ", "X", "X", " ", "X", "X", " "],
            [" ", " ", "X", " ", " ", "X", " "],
            ["X", " ", " ", " ", " ", "Q1"," "],
            [" ", "X", "X", "Q2","X", " ", " "],
            ["X", " ", "X", " ", " ", " ", " "],
            [" ", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", " ", " ", " "]
        ]
        sample_board.set_state(board_state, True)

        test_pass = True

        expected_depth_scores = [(1, -2), (2, 0), (3, 3), (4, 4), (5, 1)]

        for depth, exp_score in expected_depth_scores:
            move, score = alphbeta_fn(player, sample_board, time_left, depth=depth,alpha=float("-inf"), beta=float("inf"),  my_turn=True)
            if exp_score != score:
                print("Alphbeta failed for depth: ", depth)
                test_pass = False
            else:
                print("Alphbeta passed for depth: ", depth)

        if test_pass:
            player = yourAgent()
            sample_board = Board(player, RandomPlayer())
            # setting up the board as though we've been playing
            board_state = [
                [" ", " ", " ", " ", "X", " ", "X"],
                ["X", "X", "X", " ", "X", "Q2", " "],
                [" ", "X", "X", " ", "X", " ", " "],
                ["X", " ", "X", " ", "X", "X", " "],
                ["X", " ", "Q1", " ", "X", " ", "X"],
                [" ", " ", " ", " ", "X", "X", " "],
                ["X", " ", " ", " ", " ", " ", " "]
            ]
            sample_board.set_state(board_state, True)

            test_pass = True

            expected_depth_scores = [(1, -4), (2, 3), (3, -1), (4, 1), (5, -2)]

            for depth, exp_score in expected_depth_scores:
                move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=False)
                if exp_score != score:
                    print("Alphbeta failed for depth: ", depth)
                    test_pass = False
                else:
                    print("Alphbeta passed for depth: ", depth)

        if test_pass:
            print("Alphbeta Test: Runs Successfully!")

        else:
            print("Alphbeta Test: Failed")

    except NotImplementedError:
        print('Alphbeta Test: Not implemented')
    except:
        print('Alphbeta Test: ERROR OCCURRED')
        print(traceback.format_exc())
        
class OpenMoveEvalFn:
    def score(self, game, my_player=None):
        """Score the current game state
        Evaluation function that outputs a score equal to how many
        moves are open for AI player on the board minus how many moves
        are open for Opponent's player on the board.

        Note:
            If you think of better evaluation function, do it in CustomEvalFn below.

            Args
                game (Board): The board and game state.
                my_player (Player object): This specifies which player you are.

            Returns:
                float: The current state's score. MyMoves-OppMoves.

            """
        my_moves = len(game.get_player_moves(my_player))
        opp_moves = len(game.get_opponent_moves(my_player))

        return my_moves - opp_moves

        # TODO: finish this function!
        raise NotImplementedError

######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
################ END OF LOCAL TEST CODE SECTION ######################

class ABPlayer:
    # TODO: finish this class!
    """Player that chooses a move using your evaluation function
    and a minimax algorithm with alpha-beta pruning.
    You must finish and test this player to make sure it properly
    uses minimax and alpha-beta to return a good move."""

    def __init__(self, search_depth=9, eval_fn=OpenMoveEvalFn()):
        """Initializes your player.

        if you find yourself with a superior eval function, update the default
        value of `eval_fn` to `CustomEvalFn()`

        Args:
            search_depth (int): The depth to which your agent will search
            eval_fn (function): Evaluation function used by your agent
        """
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, time_left):
        """Called to determine one move by your agent

        Note:
            1. Do NOT change the name of this 'move' function. We are going to call
            this function directly.
            2. Call alphabeta instead of minimax once implemented.
        Args:
            game (Board): The board and game state.
            time_left (function): Used to determine time left before timeout

        Returns:
            tuple: (int,int,bool): Your best move

        """

        #active_moves = game.get_active_moves()
        #print("Active moves = ", active_moves)
        '''
        if game.move_count < 2:
            return random.choice(game.get_player_moves(self))
        '''
        '''
        if game.move_count > 15:
            print("Moves completed =", game.move_count )
            print("Spaces left for me = ", len(game.get_player_moves(self)))
            print("Spaces left for opponent = ", len(game.get_opponent_moves(self)))


            reflected_move = getReflectedMove(self, game)
            if reflected_move is not None:
                return reflected_move
        '''

        #best_move, utility = minimax(self, game, time_left, depth=self.search_depth)
        #implement iterative deepening

        #Set initial depth as 3 to always search with 3 levels
        init_depth = 4
        best_move_ab, utility_ab = alphabeta(self, game, time_left, depth=init_depth)

        curr_depth = init_depth + 1
        
        while(time_left() >= 200 and curr_depth <= self.search_depth):
            #print("Time left = ", time_left(), "Current depth = ", curr_depth)
            prev_move_ab, utility_ab = alphabeta(self, game, time_left, depth=curr_depth)

            if(utility_ab != float("-inf") and utility_ab != float("inf") ):

                best_move_ab = prev_move_ab

            #else:
            #    print("in time out")

            curr_depth = curr_depth + 1

        return best_move_ab



    def utility(self, game, my_turn):
        """You can handle special cases here (e.g. endgame)"""
        return self.eval_fn.score(game, self)

###################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE CLASS! ################
###### IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ###########
###################################################################

def minimax(player, game, time_left, depth, my_turn=True):
    """Implementation of the minimax algorithm.

    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you
            need from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer()).
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """
    # TODO: finish this function!

    if(my_turn):
        move, utility = max_value(player, game, time_left, depth, my_turn=True)
        #print("here 3 - ", "move = ", move, "value = ",utility)
        return move, utility

    else:
        move, utility = min_value(player, game, time_left, depth, my_turn=False)
        #print("here 4 - ", "move = ", move, "value = ",utility)
        return move, utility


    raise NotImplementedError

#Returns utility
def max_value(player, game, time_left, depth, my_turn):
    if (depth == 0 or time_left() <= 10):
        #print("here 1")
        return None, player.utility(game, my_turn)

    value = float("-inf")
    best_move = None
    active_moves = game.get_active_moves()

    for move in active_moves:
        new_board, is_over, winner = game.forecast_move(move)
        temp_move, temp_val = min_value(player, new_board, time_left, depth -1, my_turn)
        #print("here 2 - ", "move = ", temp_move, "value = ",temp_val)
        if (temp_val > value):
            best_move = move

        value = max(value, temp_val)

    return best_move, value



def min_value(player, game, time_left, depth, my_turn):
    best_move = None
    if (depth == 0 or time_left() <= 10):
        #print("here 1")
        return None, player.utility(game, my_turn)

    value = float("inf")
    active_moves = game.get_active_moves()

    for move in active_moves:
        new_board, is_over, winner = game.forecast_move(move)
        temp_move, temp_val = max_value(player, new_board, time_left, depth -1, my_turn)
        #print("here 3 - ", "move = ", temp_move, "value = ",temp_val)
        if (temp_val < value):
            best_move = move

        value = min(value, temp_val)

    return best_move, value






######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######
################ END OF LOCAL TEST CODE SECTION ######################

def alphabeta(player, game, time_left, depth, alpha=float("-inf"), beta=float("inf"), my_turn=True):
    """Implementation of the alphabeta algorithm.

    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you need
            from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer())
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        alpha (float): Alpha value for pruning
        beta (float): Beta value for pruning
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """
    # TODO: finish this function!
    max_utility_dict = {}
    min_utility_dict = {}
    if(my_turn):
        move, utility = max_value_ab(player, game, time_left, depth, alpha, beta, my_turn=True)
        return move, utility

    else:
        #print("**I am here dont remove me**")
        move, utility = min_value_ab(player, game, time_left, depth, alpha, beta, my_turn=False)
        return move, utility



#Returns utility
def max_value_ab(player, game, time_left, depth, alpha, beta, my_turn):
    if (depth == 0):
        #print("here 1")
        return None, player.utility(game, my_turn)

    if (time_left() <= 70):
        #return None, player.utility(game, my_turn)
        return None, float("-inf")

    value = float("-inf")
    best_move = None
    active_moves = game.get_active_moves()

    #active_moves = get_sorted_moves(game.get_active_moves(), my_turn, max_utility_dict)
    if(len(active_moves) == 1):
        return active_moves[0], player.utility(game, my_turn)

    for move in active_moves:
        new_board, is_over, winner = game.forecast_move(move)
        temp_move, temp_val = min_value_ab(player, new_board, time_left, depth -1, alpha, beta, my_turn)
        if (temp_val > value):
            best_move = move

        value = max(value, temp_val)

        if (value >= beta):
          return move, value

        alpha = max(alpha, value)

    return best_move, value


def min_value_ab(player, game, time_left,  depth, alpha, beta, my_turn):
    best_move = None
    if (depth == 0):
        return None, player.utility(game, my_turn)

    if (time_left() <= 70):
        return None, float("inf")

    value = float("inf")
    active_moves = game.get_active_moves()
    #active_moves = get_sorted_moves(game.get_active_moves(), my_turn, min_utility_dict)


    if(len(active_moves) == 1):
        return active_moves[0], player.utility(game, my_turn)

 
    for move in active_moves:
        new_board, is_over, winner = game.forecast_move(move)
        temp_move, temp_val = max_value_ab(player, new_board, time_left,  depth -1, alpha, beta, my_turn)
        if (temp_val < value):
            best_move = move

        value = min(value, temp_val)

        if (value <= alpha):
            return move, value

        beta = min(beta, value)

    return best_move, value


def getOpeningMoves(game):
        active_moves = game.get_active_moves()

        if (3,3) in active_moves:
            return (3,3)
        elif (3,2) in active_moves:
            return (3,2)
        elif (3,4) in active_moves:
            return (3,4)
        else:
            return None





