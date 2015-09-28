from Population import *
from random import randint


def crossover(pop_list, num_lists):
    ret_list = []
    skip = False
    for i in range(0,len(pop_list),1):
        if not skip:
            l1,l2 = cross_pop(pop_list[i].getChildren(),pop_list[i+1].getChildren())
            ret_list.append(Population(l1))
            ret_list.append(Population(l2))
            skip = True
        else:
            skip = False
            continue

    # for i in ret_list:
    #     if not i.valid():
    #         print "INVALID! AHHHH"

        
    return ret_list

def crosspop2(pop_list, complete_set):
    """
    This is the crossover function for the second puzzle

    :param pop_list: Takes in a generation
    :param num_lists: Takes in the number of lists used.
    :return: the next generation
    """
    ret_list = []
    skip = False
    for i in range(0,len(pop_list),1):
        if not skip:
            l1 = []; l2 = []

            l1,l2 = cross_pop(pop_list[i].getAll(),pop_list[i+1].getAll())
            l1_d = {}; l2_d = {};
            l1_s = set(l1) ; l2_s = set(l2) ## Converting them to sets removes duplicates


            #Find the duplicates that exist.
            for val,i in zip(complete_set,range(0,len(complete_set))):
                if val not in l1_s:
                    l1_d[i] = val
                if val not in l2_s:
                    l2_d[i] = val

            #Insert the missing values where they would go << Psuedo random >>
            for i in l1_d.iterkeys():
                l1.insert(randint(i,len(complete_set)-1),l1_d[i])
            for i in l2_d.iterkeys():
                l2.insert(randint(i,len(complete_set)-1),l2_d[i])

            ret_list.append(Poptwo(l1[0:11],l1[11:21],l1[21:31]))
            ret_list.append(Poptwo(l2[0:11],l2[11:21],l2[21:31]))
            skip = True

        else:
            skip = False
            continue


    return ret_list




def cross_pop(list_1, list_2):
    list_1 = split_list(list_1,2)
    list_2 = split_list(list_2,2)
    list_1a = list_1[0]
    list_1b = list_1[1]
    list_2a = list_2[0]
    list_2b = list_2[1]

    ret_1 = []
    ret_1.extend(list_1a)
    ret_1.extend(list_2b)

    ret_2 = []
    ret_2.extend(list_2a)
    ret_2.extend(list_1b)

    return ret_1,ret_2



def split_list(alist, wanted_parts=1):
    """ This split lists function was found at:
    http://stackoverflow.com/questions/752308/split-list-into-smaller-lists
    """
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]


# ## Cross Pop Test
# a = [1,1,1,1,1,1,1,1,1]
# b = [2,2,2,2,2,2,2,2,2]
# c,d = cross_pop(a,b)
# print c
# print d