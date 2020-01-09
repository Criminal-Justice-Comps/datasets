import re

NUMERIC = [3, 4, 5, 6, 7, 8]
GROUND = [0, 11, 15]

def main():
    all_categorical = []
    all_numeric = []
    all_data = []
    with open("FeaturesData.csv") as file:
        j = 0
        for line in file:
            if '\"' in line:
                # sometimes there are quote-escaped commas in the csv file, but
                #   those commas are always in the same 'column', so they are easy
                #   to remove
                half_split_line = line.split('\"')
                print(half_split_line)
                split_line = []
                contains_comma = False
                for i in range(len(half_split_line)):
                    if i == 0:
                        split_line += half_split_line[i].split(",")[:-1]
                    elif i == 1:
                        split_line.append(half_split_line[i])
                    else:
                        half_split_line[i] = half_split_line[i].replace("\n", '')
                        split_line += half_split_line[i].split(",")[1:]
            else:
                split_line = line.split(',')
                split_line[-1] = split_line[-1].rstrip('\n')
                
                cat_person = []
                num_person = []
                person = split_line
                for i in range(len(split_line)):
                    if i in GROUND:
                        cat_person.append(split_line[i])
                        num_person.append(split_line[i])
                    elif i in NUMERIC:
                        num_person.append(split_line[i])
                    else:
                        cat_person.append(split_line[i])
                if j == 0 or not(int(split_line[11]) == -1 or int(split_line[15]) == -1):
                    all_categorical.append(cat_person)
                    all_numeric.append(num_person)
                    all_data.append(person)
            j += 1

    create_file('NumericFeaturesData.csv', all_numeric)
    create_file('CategoricalFeaturesData.csv', all_categorical)
    create_file('CleanedFeaturesData.csv', all_data)


def create_filestring(data):
    string = ''
    for person in data:
        for attribute in person:
            string += str(attribute)
            string += ","
        string = string[:-1]
        string += "\n"
    return string

def create_file(filename, data):
    string = create_filestring(data)
    with open(filename, 'w') as file:
        file.write(string)

if __name__ == "__main__":
    main()
