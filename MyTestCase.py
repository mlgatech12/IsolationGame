import unittest

from isolation import Board
from player_submission_tests import RandomPlayer

from multiprocessing import Pool

class MyTestCase(unittest.TestCase):
    def test_RandomPlayer_vs_RandomPlayer(self):
        Q1 = RandomPlayer()
        Q2 = RandomPlayer()
        play_n_rounds(Q1, Q2, print_moves=False)
        # play(Q1, Q2, print_moves=False)


def play_n_rounds(mine, theirs, size=7, time_limit=1000, print_moves=False, rounds=10):
    from collections import defaultdict
    from multiprocessing import Pool

    winners = defaultdict(int)
    pool_Q1_mine = Pool()
    results_Q1_mine = []
    for idx in range(rounds):
        results_Q1_mine.append(
            pool_Q1_mine.apply_async(play, (mine, theirs, size, time_limit, print_moves, str(idx) + "Q1")))
    data_Q1_mine = [result.get() for result in results_Q1_mine]
    for d_Q1_mine in data_Q1_mine:
        winners['Games'] += 1
        winners["mine" if "Q1" in d_Q1_mine[0] else "theirs"] += 1

    pool_Q2_mine = Pool()
    results_Q2_mine = []
    for idx in range(rounds):
        results_Q2_mine.append(
            pool_Q2_mine.apply_async(play, (theirs, mine, size, time_limit, print_moves, str(idx) + "Q2")))
    data_Q2_mine = [result.get() for result in results_Q2_mine]
    for d_Q2_mine in data_Q2_mine:
        winners['Games'] += 1
        winners["mine" if "Q2" in d_Q2_mine[0] else "theirs"] += 1

    print("rounds {} winners {}".format(rounds * 2, winners))


def play(Q1, Q2, size=7, time_limit=1000, print_moves=False, seed=None):
    import random
    if seed is not None:
        random.seed(seed)
    game = Board(Q1, Q2, size, size)
    # assign a random move to each player before playing
    for idx in range(2):
        moves = game.get_active_moves()
        random.shuffle(moves)
        game = game.forecast_move(moves[0])[0]
    winner, move_history, termination = game.play_isolation(time_limit=time_limit, print_moves=print_moves)
    #print("\n" , " Game finished in moves: ", game.move_count)
    print("\n", winner, " has won. Reason: ", termination)
    return winner, move_history, termination


if __name__ == '__main__':
    unittest.main()