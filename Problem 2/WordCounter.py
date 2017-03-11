import sys
import os

class WordCounter:
    def IsValid(self, file):
        return os.path.isfile(file)

    def word_count(self, input_file):
        if self.IsValid(input_file):
            with open(input_file, 'r') as f:
                counter=0
                for line in f:
                    for word in line.split():
                        counter = counter + 1
                print('Found ',counter,' words in ', input_file, sep='')
        else:
            print('Theres no such file :',input_file )

if __name__=='__main__':
  with open('word_counter_output.txt', 'w') as sys.stdout:
    word_counter = WordCounter()
    word_counter.word_count(sys.argv[1])
