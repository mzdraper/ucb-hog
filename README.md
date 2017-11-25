# Hog Project

## Overview and Rules
This Python project is a bit of spin off the original Pig dice game. It is a two player game with both players' objective to be the first to earn at least 100 points. The spins are the rules include the following:
* Pig Out

 ...- If any of the dice outcomes is a 1, the current player's score for the turn is the number of 1's rolled. Pig Out may award a maximum of 11 points minus the number of dice rolled on a turn.
 ...- Example 1: The current player rolls 7 dice, 5 of which are 1's. They score min(11 - 7, 5) = 4 points for the turn.
 ...- Example 2: The current player rolls 5 dice, 3 of which are 1's. They score min(11 - 5, 3) = 3 points from Pig Out. Hogtimus Prime (described below) will increase the score for the turn to 5.
 - Example 3: The current player rolls 4 dice, all of which are 3's. Since Pig Out did not occur, they score 12 points for the turn.
 
* Free Bacon

 ...- A player who chooses to roll zero dice scores one more than the largest digit in the opponent's total score.
 ...- Example 1: If the opponent has 42 points, the current player gains 1 + max(4, 2) = 5 points by rolling zero dice.
 ...- Example 2: If the opponent has 48 points, the current player gains 1 + max(4, 8) = 9 points by rolling zero dice.
 ...- Example 3: If the opponent has 7 points, the current player gains 1 + max(0, 7) = 8 points by rolling zero dice.

* Hogtimus Prime

 ...- If a player's score for the turn is a prime number, then the turn score is increased to the next larger prime number. For example, if the dice outcomes sum to 11, the current player scores 13 points for the turn. This boost only applies to the current player. Note: 1 is not a prime number!

* Hog Wild

 ...- If the sum of both players' total scores is a multiple of seven (e.g., 0, 7, 14, 21, 35), then the current player rolls four-sided dice instead of the usual six-sided dice.

* Swine Swap

 ...- After the turn score is added, if one of the scores is double the other, then the two scores are swapped.
 ...- Example 1: The current player has a total score of 37 and the opponent has 92. The current player rolls two dice that total 9. The current player's new total score (46) is half of the opponent's score. These scores are swapped! The current player now has 92 points and the opponent has 46. The turn ends.
 ...- Example 2: The current player has 91 and the opponent has 55. The current player rolls five dice that total 17, a prime that is boosted to 19 points for the turn. The current player has 110, so the scores are swapped. The opponent ends the turn with 110 and wins the game.

## Starter Files
All of the starter files can be found [here](http://inst.eecs.berkeley.edu/~cs61a/sp17/proj/hog/hog.zip "hog.zip"). The autograder will occasionally ask for your CalID/Berkeley e-mail. You can just hit enter & then leave the redirect browser. You do not need to be enrolled in this class to use all its materials.

## Testing
In order to test your code through the `ok` grader, you have to first pass a series of tests. The tests are simple in that they're just confirming you truly understand what the functions are supposed to do before you write them. Expect a lot of tests!
To begin the tests, type `python3 ok -u` into the terminal. Once you would like to test your own code, type in `python3 ok`. Use `python3 ok -q function-name>` for testing specific parts of your code. The tests may annoyingly ask for your Berkeley credentials, so you may want to type `--local` whenever envoking ok.

## The Actual Project
I won't go through each grueling detail here, as I feel the code and supplementary comments should be sufficient. But if you would like the original scaffolding, [certainly](http://inst.eecs.berkeley.edu/~cs61a/su17/proj/hog/ "enjoy!").
