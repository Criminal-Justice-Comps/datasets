"""
Used to:
    remove individuals with a -1 for is_resid or is_violent_recid
    split the data into just categorical features (stored in CategoricalFeaturesData.csv)
        and just numerical features (stored in NumericFeaturesData.csv)

Directions for use:
    1: set the column numbers for numeric features and features that you want to be
        in every file by changing NUMERIC and GROUND
    2: set LOAD_FILENAME to the proper file path
    3: set IGNORE_QUOTED_COMMAS and QUOTES_TO_IGNORE as required
    4: run `python split-cat-num.py`

========================================== IMPORTANT ==========================================
BE SURE THAT THERE IS NOTHING YOU NEED TO SAVE IN CategoricalFeaturesData.csv,
NumericFeaturesData.csv, or CleanedFeaturesData.csv
========================================== IMPORTANT ==========================================
"""

NUMERIC = [3, 4, 5, 6, 7, 8] # all numeric features
GROUND = [0, 11, 15] # features to include in all
LOAD_FILENAME = "TrainValidateTest/ValidateFeatures.csv" # load data from this file
IGNORE_QUOTED_COMMAS = True # ignore commas in quotation marks
QUOTES_TO_IGNORE = [7264] # ignore quotes on this line w.r.t. commas

def main():
    all_categorical = []
    all_numeric = []
    all_data = []
    with open(LOAD_FILENAME) as file:
        j = 0
        for line in file:
            split_line = []
            if IGNORE_QUOTED_COMMAS and ('\"' in line) and (j not in QUOTES_TO_IGNORE):
                # sometimes there are quote-escaped commas in the csv file, but
                #   those commas are always in the same 'column' except in row 7264
                #   so they are mostly easy to remove
                half_split_line = line.split('\"')
                split_line = []
                split_line += half_split_line[0][:-1].split(",")
                split_line.append(half_split_line[1])
                split_line += half_split_line[2][1:].split(",")
                split_line[-1] = split_line[-1].rstrip('\n')
            else:
                split_line = line.split(',')
                split_line[-1] = split_line[-1].rstrip('\n')
            cat_person = []
            num_person = []
            person = split_line
            for i in range(len(split_line)):
                #seperate numeric and categorical features
                if i in GROUND:
                    cat_person.append(split_line[i])
                    num_person.append(split_line[i])
                elif i in NUMERIC:
                    num_person.append(split_line[i])
                else:
                    cat_person.append(split_line[i])

            #if j == 0 or not(int(split_line[11]) == -1 or int(split_line[15]) == -1):
            all_categorical.append(cat_person)
            all_numeric.append(num_person)
            all_data.append(person)
            j += 1

    create_file('TrainValidateTest/ValidateFeaturesNumeric.csv', all_numeric)
    create_file('TrainValidateTest/ValidateFeaturesCategorical.csv', all_categorical)
    #create_file('CleanedFeaturesData.csv', all_data)


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

def create_file(filename, data):
    # writes a csv file in `filename` based containing `data`
    string = create_filestring(data)
    with open(filename, 'w') as file:
        file.write(string)

if __name__ == "__main__":
    main()
