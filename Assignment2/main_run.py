from run_p1 import *
from run_p2 import *





WHICH_FUNCTION = 2
WHICH_FILE = "list2.txt"

for i in range(0,10):
    if WHICH_FUNCTION == 1:
        run_p1(WHICH_FILE,MAX_GENERATION=50,GENERATION_SIZE=10)
    if WHICH_FUNCTION == 2:
        run_p2(WHICH_FILE,MAX_GENERATION=100,GENERATION_SIZE=10)
