"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times. Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    sum, i = 0, 0
    while num_rolls > i:
        score = dice()
        if score == 1:
            return 1
        elif sum != 1:
            return sum = sum + score
        i++
        return sum
  

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'

    if num_rolls != 0:
        runscore = roll_dice(num_rolls, dice)
    else:
        # not sure if the HOF version would work, but I like the concept more
        # def free_bacon(opponent_score): 
        # if num_rolls = 0:
            opponent_scoreFirstDigit = opponent_score // 10
            opponent_scoreSecondDigit = opponent_score % 10
            #example: if opponent_score == 23, becomes 2, 3
            runscore = 1 + max(opponent_scoreFirst, opponent_scoreSecond)
        return score


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    sum_combined = score + opponent_score
    if sum_combined % 7 == 0:
        dice = four-sided
    else:
        dice = six-sided
    return dice


def is_prime(n):
    """Return True if a non-negative number N is prime, otherwise return
    False. 1 is not a prime number!
    """
    assert type(n) == int, 'n must be an integer.'
    assert n >= 0, 'n must be non-negative.'
    
    k = 2
    if n == 0 or 1:
        return False
    while k <= 3:
        if n % k == 0:
            return False
    else:
        return True


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1

    Implement the play function, which simulates a full game of Hog. Players 
    alternate turns, each using their respective strategy function (Player 0 
    uses strategy0, etc.), until one of the players reaches the goal score. 
    When the game ends, play returns the final total scores of both players, 
    with Player 0's score first, and Player 1's score second.

    Here are some hints:

    -You should use the functions you have already written! 
    -You will need to call take_turn with all three arguments.
    -Enforce the remaining special rules: Perfect Piggy and Swine Swap.
    -You can get the number of the other player (either 0 or 1) by calling 
    the provided function other.
    -A strategy is a function that, given a player's score and their opponent's 
     score, returns how many dice the player wants to roll. A strategy function
     (such as strategy0 and strategy1) takes two arguments: scores for the current 
     player and opposing player, which both must be non-negative integers. A strategy 
     function returns the number of dice that the current player wants to roll in the turn. 
    -Each strategy function should be called only once per turn. Don't worry about the 
     details of implementing strategies yet. You will develop them in Phase 2.

    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
  
    while score_p1 < goal and score_p2 < goal:

        dice = select_dice(score0, score1)
            if who == 0:
                runscore = take_turn(strategy0(score0, score1), score1, dice)
                score0 += runscore 

            if who == 1:                   
                runscore = take_turn(strategy1(score1, score0), score0, dice)
                score1 += runscore 

            if is_prime(score0 + score1) and score0 != score1:
                if score0 > score1:
                    score0 += runscore
                else:
                    score1 += runscore  

            who = other(who)

        return score0, score1

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice no matter the scores.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.
    *args accepts an abritrary number of arguments, then calls another funciton
    using those same arguments

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    
    def average(*args)
        result, i = 0, 0
        while i =< num_samples: 
            # =< to account for base case of 1 die argument
            result = result + f(*args)
            i++
        return result
    return average


def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Assume that dice always
    return positive outcomes.

    Implement the max_scoring_num_rolls function, which runs an experiment to 
    determine the number of rolls (from 1 to 10) that gives the maximum average 
    score for a turn. Your implementation should use make_averaged and roll_dice.

    If two numbers of rolls are tied for the maximum average score, return the 
    lower number. For example, if both 3 and 6 achieve a maximum average score, 
    return 3.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """

    i, the_average = 1, 0
    averaged_dice = make_average(roll_dice, 1000)
    while i =< 10:
        if averaged_dice(i, dice) > the_average:
            the_average = averaged_dice(i, dice)
            number_of_dice = i
        i++
    return number_of_dice


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""

    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1
  

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    
    # I am confused

    # rate0 = stuff that finds the win rate
    # rate1 = 1 - stuff that finds the win rate
    # return max(rate0, rate 1)
    # OR
    # is it returning the average wins between rate0 and rate1 
    # --> return (rate0 + rate) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True: # Change to True to test prime_strategy
        print('prime_strategy win rate:', average_win_rate(prime_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.

    A player who chooses to roll zero dice scores one more than the 
    largest digit in the opponent's total score.
    If opponent has 42 points, current player gains 1 + max(4, 2) = 5 
    points by rolling zero dice.
    """

    dice = select_dice(score, opponent_score)
    bacon = take_turn(0, opponent_score, dice)
    if bacon < margin:
        return num_rolls
    else:
        return 0

def prime_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial boost and
    rolls NUM_ROLLS if rolling 0 dice gives the opponent a boost. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    
    dice = select_dice(score, opponent_score)
    bacon = take_turn(0, opponent_score, dice)

    if is_prime(score + bacon + opponent_score):
        if bacon + score > opponent_score:
            return 0
        elif bacon + score < opponent_score:
            return num_rolls
    return bacon(score, opponent_score, margin num_rolls)


def final_strategy(score, opponent_score):

    # uhhhh, maybe later

##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
