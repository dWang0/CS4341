from run_p1 import *
from run_p2 import *
from Puzzle3 import *
import sys
from sys import argv


#############################################################
#                     Input Parsing                         #
#############################################################
global WHICH_FUNCTION
try:
    WHICH_FUNCTION = argv[1]
except IndexError:
    sys.exit()

WHICH_FUNCTION = int(WHICH_FUNCTION)


WHICH_FILE = "list2.txt"

if WHICH_FUNCTION == 1:
    run_p1(WHICH_FILE,MAX_GENERATION=50,GENERATION_SIZE=10)
if WHICH_FUNCTION == 2:
    run_p2(WHICH_FILE,MAX_GENERATION=50,GENERATION_SIZE=10)
if WHICH_FUNCTION == 3:
    # run_p3(WHICH_FILE,MAX_GENERATION=50,GENERATION_SIZE=10)
    puzzle3()