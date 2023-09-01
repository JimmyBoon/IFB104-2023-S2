
#-----Module Description - Data Set Generation-----------------------#
#
#  This module contains a function needed for Assignment 1 in
#  QUT's teaching unit IFB104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary element will then be imported
#  into your program automatically.
#
#  NB: Do NOT submit this file with your solution.  Changes made to
#  this module will have no effect when your assignment is graded
#  because the markers will use their own copy of the file.  If your
#  solution relies on changes made to this file it will fail to work
#  when assessed.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used for generating the
# data set.  Do not change any of the code in this section.
#

# Import standard Python functions needed to support this module.
from random import randint, choice, seed
from turtle import textinput
from re import sub

# A global variable used to ensure that the student doesn't call
# function "data_set" or "raw_data" in their code
already_called = False

#
#--------------------------------------------------------------------#



#-----Test Cases-----------------------------------------------------#
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the data generation function at the bottom of
# the assignment template file with a "seed" value which will force
# it to produce a known data set.  Of course, having completed your
# solution, your program must work for any list that can be returned
# by calling the data generation function with no argument.
#
# You can use also enter seed values or test numbers by activating
# the "pop-up tester" below.  The markers will use this facility to
# efficiently test your solution.
#

# Test no. / Seed / Description, including how many cells are
# captured by each competitor, A & B, respectively
test_cases = [
    # The shortest possible data set
    [0, 13710,   "Empty data set, no moves made. Cells captured: 0 & 0"],
    # Short data sets in which competitors do not block each
    # other or try to backtrack
    [-1, 32099,  "Both competitors move once. Cells captured: 0 & 0"],
    [-2, 76335,  "Only Competitor A moves, four times. Cells captured: 1 & 0"],
    [-3, 13829,  "Only Competitor B moves. Cells captured: 0 & 1"],
    [-4, 51958,  "A moves four times, B only once. Cells captured: 1 & 0"],
    [-5, 3199,   "A moves twice, B five times. Cells captured: 0 & 3"],
    [-6, 48793,  "Poor moves by A give B the advantage. Cells captured: 0 & 3"], 
    # Data sets in which competitors do not block each
    # other but waste moves trying to backtrack
    [-7, 39717,  "Competitor A wastes one move. Cells captured: 1 & 0"],
    [-8, 79000,  "Competitor A wastes its second move. Cells captured: 0 & 0"],
    [-9, 78156,  "Competitor B wastes its second move. Cells captured: 0 & 2"],
    [-10, 35842, "Competitor B wastes three moves. Cells captured: 0 & 0"],
    [-11, 58205, "A wastes one move and B wastes two. Cells captured: 2 & 4"],
    [-12, 4470,  "A wastes two moves and B wastes three. Cells captured: 0 & 0"],
    # Data sets in which competitors block one another
    [-13, 83855, "Competitor B blocks A's only move. Cells captured: 0 & 1"],
    [-14, 82570, "Competitor A blocks B's second move. Cells captured: 3 & 0"],
    [-15, 42501, "Competitor A blocks B's final move. Cells captured: 0 & 2"],
    [-16, 16223, "Competitor B blocks three of A's moves. Cells captured: 0 & 3"],
    [-17, 92398, "Competitor B blocks two of A's moves. Cells captured: 1 & 4"],
    [-18, 99506, "Competitors butt heads but A is quicker. Cells captured: 1 & 0"], 
    [-19, 52969, "Both competitors block the other one at the centre line. Cells captured: 0 & 2"],
    [-20, 99244, "Competitor B blocks all of A's moves. Cells captured: 0 & 6"],
    # Data sets in which a competitor tries to exit the grid
    [-21, 26796, "Competitor A tries to exit via the south border in Steps 12 and 15. Cells captured: 0 & 1"],
    [-22, 29359, "Competitor A tries to exit via both the north and east borders. Cells captured: 8 & 0"],
    [-23, 74235, "Competitor B tries to exit via the west border in the final step. Cells captured: 0 & 6"],
    [-24, 85053, "Competitor B tries to exit via the north border in Step 8. Cells captured: 0 & 5"],
    # Some long data sets with many cells captured
    [-25, 89068, "Competitors don't interact but both capture many cells. Cells captured: 6 & 5"],
    [-26, 47398, "Competitor B becomes trapped in cell D5. Cells captured: 1 & 3"],
    [-27, 11495, "Competitor A successfully invades B's territory! Cells captured: 8 & 0"],
    [-28, 94267, "A big victory for Competitor B! Cells captured: 0 & 10"]
    ]

# For markers (or interested students): Set the following constant
# to True to enable the pop-up seed/test no. prompt.  Positive
# values entered are interpreted as seeds for the random number
# generator.  Zero or negative numbers are interpreted as one of the
# test cases listed above.  Any other values entered are ignored and
# a random seed is used instead.
pop_up_tester = False
           
#
#--------------------------------------------------------------------#


#-----Data Set Function for Assessing Your Solution------------------#
#
# The function in this section is called by the assignment template
# to generate the data sets used by your program.  Do not change
# any of the code in this section.

# The following function creates a random data set defining the
# overall image to draw.  Your program must work for ANY data set that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the data set generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def raw_data(given_seed):

    # Confirm that this is the first time functions "data_set" or
    # "raw_data" have been called, otherwise abort the program
    global already_called
    assert not already_called, "Program attempts to create a second data set - Aborting!"
    already_called = True

    # Decide which seed to use
    if pop_up_tester:
        # Get the seed number from the user
        markers_choice = textinput('Seed or test case selection',
                                   'Enter seed or test case number')
        try:
            number_entered = int(markers_choice)
            if number_entered > 0:
                # Use the number entered as the seed
                chosen_seed = number_entered
                description = 'Manually-entered seed'
            else:
                # Get the seed from the list of test cases
                chosen_seed = test_cases[abs(number_entered)][1]
                description = test_cases[abs(number_entered)][2]
        except:
            # User's input is not a number or is not in the
            # range of test cases, so ignore it
            print('Invalid seed or test number ignored ...\n')
            chosen_seed = given_seed
            description = 'Randomly-chosen seed'            
    else:
        # Use the argument given to raw_data
        chosen_seed = given_seed
        description = 'Randomly-chosen data set'
    # Set the random number seed and inform the user
    print(f'Using seed {chosen_seed}\n({description}) ...\n')
    seed(chosen_seed)

    # Define the competitors
    competitors = ['Competitor A', 'Competitor B']
    # Define the various ways the competitors can move, biased
    # towards Competitor A moving east and Competitor B moving
    # west
    directions_a = ['Move north', 'Move south', 'Move west',
                    'Move east', 'Move east', 'Move east']
    directions_b = ['Move north', 'Move south', 'Move east',
                    'Move west', 'Move west', 'Move west']
    # Keep track of how many moves have been created in total
    move_no = 0
    # Initialise the data set
    moves = []

    # Create the random moves
    total_moves = randint(0, 25)
    while move_no < total_moves:
        # Choose which competitor to move
        competitor = choice(competitors)
        # Choose how to move
        if competitor == 'Competitor A':
            move = choice(directions_a)
        else:
            move = choice(directions_b)
        # Add the move to the data set
        moves.append([move_no, competitor, move])
        # Increment move number
        move_no = move_no + 1

    # Print the whole data set to the shell window, laid out
    # one move per line, and with Competitor B indented to
    # aid readability
    print("The competitors' attempted moves are:\n")
    print(sub(r"\[([0-9]),", r"[0\1,", str(moves).replace("'Competitor B'", "    'Competitor B'").replace('],', '],\n')) + '\n')
    # Return the data set to the caller
    return moves

#
#--------------------------------------------------------------------#

