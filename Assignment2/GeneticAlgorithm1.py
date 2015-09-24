import csv
import math


def readcsv(name):
    temp_input = []
    with open( name, 'rt') as csvfile:
        input_reader = csv.reader(csvfile, quotechar='|')
        for row in input_reader:
            temp_input.append((int(row[0])))
    # print ("Temp is:",temp_input)
    return temp_input


def readcsv_float(name):
    temp_input = []
    with open( name, 'rt') as csvfile:
        input_reader = csv.reader(csvfile, quotechar='|')
        for row in input_reader:
            temp_input.append((float(row[0])))
    # print ("Temp is:",temp_input)
    return temp_input

###main
# response = readcsv("list1.txt")
# print (response)
