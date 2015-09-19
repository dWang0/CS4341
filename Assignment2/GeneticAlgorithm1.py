import csv
import math

class GeneticAlgorithm1
    #Give this function a filename and delimiter
    target = 0
    
    def readcsv(self, name):
        temp_input = []
            with open( name, 'rb') as csvfile:
                input_reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
                for row in map_reader:
                    temp_input.append(row)
            self._raw_map = temp_input


