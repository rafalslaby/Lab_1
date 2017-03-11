from sys import argv
import os

class LogParser:
    def IsValid(self, file):
        return os.path.isfile(file)

    def parse_log(self, input_file, string_to_be_found):
        if self.IsValid(input_file):
            with open(input_file, 'r') as f:
                counter=0
                linescounter=0
                for line in f:
                    if string_to_be_found in line:
                        counter = counter + 1
                        print (linescounter)
                    linescounter+=1
                print(string_to_be_found, ' was found ',counter,' times')
        else:
            print('Theres no such file :',input_file )
parser = LogParser()
parser.parse_log(argv[1],argv[2])
