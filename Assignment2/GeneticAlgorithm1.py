class GeneticAlgorithm1
    #Give this function a filename and delimiter
    def readcsv(self, name):
        temp_input = []
            with open( name, 'rb') as csvfile:
                map_reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
                for row in map_reader:
                    temp_map.append(row)
            self._raw_map = temp_map