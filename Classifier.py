import os
import math
import operator
import itertools
from collections import Counter

def counter(element, seq):
    return sum(1 for i in seq if i == element)

#########################################################################
# Tokenizes the input file and retunrs it
def tokenize_file(file_name):
    tokens = []
    with open(file_name, 'r') as f:
        link_file = [line.strip() for line in f]

    for entry in link_file:
        temp_tokens = entry.split()
        tokens.extend(temp_tokens)
    return tokens


def trainer(training_dir, model_file):

    training_data = {}

    for dir_entry in os.listdir(training_dir):

        dir_entry_path = os.path.join(training_dir, dir_entry)

        filenames = next(os.walk(dir_entry_path))[2]
        file_data = {}
        print("Total filenames", len(filenames))
        sum= 0
        for files in filenames:
            new_file_name = os.path.join(dir_entry_path, files)
            if os.path.isfile(new_file_name):
                tokenzied_data = tokenize_file(new_file_name)
            file_data[files] = tokenzied_data
            sum += len(tokenzied_data)
        training_data[dir_entry] = file_data
        print(sum)

    # Write to an output file. The file name is the one provided.
    f = open(model_file, 'w')
    f.write(str(training_data))
    f.close()

def find_words_to_be_ignored(dict_file):
    ignore_words = []
    total_words = []
    for key, value in dict_file.items():
        for key2, value2 in value.items():
            total_words += value2

    word_dict = Counter(total_words)
    ignore_words = {k for k, v in word_dict.items() if v < 5}

    vocab_count = len(set(total_words)-set(ignore_words))

    print("Vocab count is - ", vocab_count)
    return ignore_words, vocab_count, set(total_words)

def classifier(model_file, classify_file, ignore_words, vocab_count):

    result = {}
    first_param = {}

    # Calculate the total docs for each key
    for key, value in model_file.items():
        first_param[key] = len(value)


    # Calculate the total size
    total_size = 0
    for key, value in first_param.items():
        total_size += value

    # Calculate the first P(C) value
    for key, value in first_param.items():
        result[key] = math.log(value/total_size, 2)

    # Get the tokens for the input file which is to be classified
    classify_tokens = tokenize_file(classify_file)

    # Iterate over the classification keys and return the log value
    for key, value in model_file.items():

        word_present = []
        for key2, value2 in value.items():
            for word in value2:
                if word in ignore_words:
                    continue
                else:
                    word_present.append(word)

        word_counter = Counter(word_present)

        for c_token in classify_tokens:
            #c_count = word_present.count(c_token)
            #c_count = counter(c_token, word_present)
            c_count = word_counter[c_token]
            c_value = math.log((c_count + 1)/(len(word_present) + vocab_count), 2)
            result[key] += c_value

    print("And the output is --- ", result)
    return result


def tester(model_file, test_directory, predictions_file):

    model = eval(open(model_file).read())
    ignore_words, vocab_count, total_words = find_words_to_be_ignored(model)

    f = []
    files = next(os.walk(test_directory))
    for filename in files[2]:
        f.append(os.path.join(test_directory, filename))
    for dir in files[1]:
        temp_test_directory = os.path.join(test_directory, dir)
        temp_files = next(os.walk(temp_test_directory))
        print(temp_files)
        for filename in temp_files[2]:
            f.append(os.path.join(temp_test_directory, filename))

    result = {}
    for filename in f:
        value = classifier(model, filename, ignore_words, vocab_count)
        result[filename] = value

    f = open(predictions_file, 'w')

    for key, value in result.items():

        valueP = value["pos"]
        valueN = value["neg"]
        if valueP > valueN:
            value = "Positive"
        else:
            value = "Negative"

        f.write("{0} Overall={1} Pos Score- {2} Neg Score-{3}\n".format(key, value, valueP, valueN))

    f.close()
    temp_result ={}

    for key, value in model.items():

        word_present = []
        for key2, value2 in value.items():
            for word in value2:
                if word in ignore_words:
                    continue
                else:
                    word_present.append(word)

        word_counter = Counter(word_present)

        for word in total_words:
            #c_count = word_present.count(c_token)
            #c_count = counter(c_token, word_present)
            c_count = word_counter[word]
            c_value = math.log((c_count + 1)/(len(word_present) + vocab_count), 2)
            if key.find("neg") > 0:
                c_value = - c_value
            temp_result[word] += c_value


    sorted_score = sorted(sorted(temp_result.items()), key=operator.itemgetter(1), reverse=True)
    count = 0
    for value in itertools.islice(sorted_score, 0, 20):
        count += 1
        print("{0} {1:.5f}\n".format(count, value))
    f.close





#################################################################################
#
# THIS IS THE START OF THE PROGRAM
#
#################################################################################
while True:
    i = input("Please enter the command or any other key to exit ")
    try:
        args = i.split(" ")

        if args[0] == "nbtrain":
            trainer(args[1], args[2])
            break

        elif args[0] == "nbtest":
            tester(args[1], args[2], args[3])
            break

        # else break from the loop and exit
        else:

            print("Exiting the program..")
            break

    #except IndexError:
    #    print("Incorrect number of arguments")
    except FileNotFoundError:
        print("File not found. Please check the file name and try again")
