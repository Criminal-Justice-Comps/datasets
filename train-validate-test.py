"""
Used to randomly divide a dataset (in csv format) into:
    - training set (80%)
    - validation set (10%)
    - test set (10%)

Directions for use:
    1: set LOAD_FILENAME, FILE_PATH to the proper file path
    2: set TRAIN_FILENAME, VALIDATE_FILENAME, and TEST_FILENAME to desired name
    2: run "python3 train-validate-test.py"

"""
from random import randint

LOAD_FILENAME = "categoricalfeaturesdata.csv" # load data from this file
FILE_PATH = "TrainValidateTest/" # location for the files you create

TRAIN_FILENAME = "TrainCategoricalFeatures.csv"
VALIDATE_FILENAME = "ValidateCategoricalFeatures.csv"
TEST_FILENAME = "TestCategoricalFeatures.csv"


def main():
    with open(LOAD_FILENAME) as file:
        line = file.readline()
        headers = line.split(',')
        headers[-1] = headers[-1].rstrip('\n')
        train = [headers]
        validate = [headers]
        test = [headers]

        for line in file:
            split_line = line.split(',')
            split_line[-1] = split_line[-1].rstrip('\n')
            rand_num = randint(1,10)
            if rand_num == 1:
                validate.append(split_line)
            elif rand_num == 2:
                test.append(split_line)
            else:
                train.append(split_line)

        create_file(FILE_PATH + TRAIN_FILENAME, train)
        create_file(FILE_PATH + VALIDATE_FILENAME, validate)
        create_file(FILE_PATH + TEST_FILENAME, test)

# borrowed from split-cat-num.py
def create_filestring(data):
    # creates a string to write to a file based on the passed list
    string = ''
    for person in data:
        for attribute in person:
            string += str(attribute)
            string += ","
        string = string[:-1]
        string += "\n"
    return string

# borrowed from split-cat-num.py
def create_file(filename, data):
    # writes a csv file in `filename` based containing `data`
    string = create_filestring(data)
    with open(filename, 'w') as file:
        file.write(string)


if __name__ == "__main__":
    main()
