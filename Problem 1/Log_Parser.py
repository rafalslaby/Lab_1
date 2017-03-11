import sys
import os

class LogParser:
    def IsValid(self, file):
        return os.path.isfile(file)

    def parse_log(self, input_file, string_to_be_found):
        if self.IsValid(input_file):
            with open(input_file, 'r') as f:
                counter=0
                linescounter=0
                List=[]
                for line in f:
                    if string_to_be_found in line:
                        counter = counter + 1
                        List.append(linescounter)
                    linescounter+=1
                print('string: "',string_to_be_found, '" was found ',counter,' times in the following lines:\n', List, sep='')
        else:
            print('Theres no such file :',input_file )

if __name__=='__main__':
    with open('log_parser_output.txt', 'w') as sys.stdout:
        parser = LogParser()
        parser.parse_log(sys.argv[1],sys.argv[2])
