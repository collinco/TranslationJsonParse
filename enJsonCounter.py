# Assuming the json file has a depth of one..

# This program finds the longest "value" with most words
# This program finds "values" that are duplicates
# This program finds if the "keys" exist in given files
# Case sensitive atm

def main():

    import json
    import time
    import copy
    import re
    import collections
    import datetime

    #class imports
    from classes.steps import Step3
    from classes.steps import Step1and2

    import glob
    import os
    from pathlib import Path

    from pprint import pprint


    file = open('StatsReport.txt','w' )

    # get this in a function
    currentDateTime = str(datetime.datetime.now())

    # TODO add report name (made it from cmd args)
    file.write("Statistics Report for \n\n")
    file.write("This report was ran on: " + currentDateTime + "\n")
    # TODO get last modified date
    # file.write("The json file read was last updated on: \n")

    JsonData = json.load(open('exampleJSON.json', encoding='utf-8'))
    # JsonData = json.load(open('exampleJSON.json'))

    consumedData = []

    def bubbleSortByLength(listBoi) :

        arr = copy.deepcopy(listBoi)

        n = len(arr)

        # Traverse through all array elements
        for i in range(n) :

            # Last i elements are already in place
            for j in range(0, n-i-1) :

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j].wordCount < arr[j+1].wordCount :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def step1and2func():

        print("running report")
        wordsList = []
        total = 0


        for key in JsonData:

            # cast to string otherwise error
            # print(JsonData[key])
            # re.sub('<.*>',' ',str(JsonData[key]))

            # create object and deconstruct
            item = Step1and2()
            item.wordCount = len(str(JsonData[key]).split(' '))
            item.text = JsonData[key]
            item.key = key
            item.words = str(JsonData[key]).split(' ')

            # looping logic
            consumedData.append(item)
            wordsList.append(str(JsonData[key]))
            total += 1

        sortedList = bubbleSortByLength(consumedData)

        file.write("Total Number or Key Value Pairs: " + str(total) + '\n\n\n')
        file.write("The top 5 longest strings by word count: \n")

        counter = 0
        while(counter < 5):
            file.write("   " + sortedList[counter].key + " : " + str(sortedList[counter].wordCount) + "\n")
            counter += 1

        # count duplicatees
        WordDupes = dict(collections.Counter(wordsList))
        KeyDupes = {}
        finalDict = {}

        for key, val in WordDupes.items() :
            if val >= 2 :
                KeyDupes[key] = val

        # find all keys that match a dupe string
        for key, val in KeyDupes.items() :
            for ele in consumedData :
                if key == ele.text :
                    if key in finalDict :
                        finalDict[key].append(ele.key)
                    else :
                        finalDict[key] = [ele.key]

        file.write("\n\n")
        file.write("The following string values are duplicated. Underneath the value are the keys it is found in: \n")

        # This is just printing items that are duplicated (>=2)
        for ele in finalDict :
            file.write("   \"" + ele + "\" : " + str(len(finalDict[ele])) + "\n")
            for ele2 in finalDict[ele]:
                file.write("      " + ele2 + "\n")

        file.write("\n")
        # file.write("The top 5 duplicated string are: ")

    # just going to return files for now and not worry about doing the totalling here as of now
    def recursion(filepath, key, ArrayOfFiles, ArrayOfOccurences):

        if(filepath.is_dir()) :
            for item in filepath.iterdir():
                recursion(Path(item), key, ArrayOfFiles, ArrayOfOccurences)
        else:
            openItem = open(filepath, "r")
            readItem = openItem.read()
            occurences = re.findall(key, readItem)
            ArrayOfFiles.append(filepath)
            ArrayOfOccurences.append(len((occurences)))

    def step3():

        ArrayOfFiles = []

        wordsList = []
        total = 0

        start_time = time.time()

        for key in JsonData:

            #cast to string otherwise error
            # re.sub('<.*>',' ',str(JsonData[key]))

            # create object to append to list
            item = Step1and2()
            item.wordCount = len(str(JsonData[key]).split(' '))
            item.text = JsonData[key]
            item.key = key
            item.words = str(JsonData[key]).split(' ')

            consumedData.append(item)
            wordsList.append(str(JsonData[key]))
            total += 1

        key = []
        keysWithoutRef = []

        folders = ['test']

        # TODO reuse older consumed data
        for obj in consumedData:
            grandTotal = 0
            ArrayOfOccurences = []

            # TODO ArrayOfFiles keeps getting appended to unnecessarily
            for folder in folders:
                NumInFolder = 0
                p = Path(folder)
                recursion(p, obj.key, ArrayOfFiles, ArrayOfOccurences)
                for ele in ArrayOfOccurences:
                    grandTotal += ele
                    NumInFolder += ele
                # print("in " + folder + " There were " + str(NumInFolder))

            print("The key " + obj.key + " appears " + str(grandTotal) + " times")

            if (obj.key == 0) :
                keysWithoutRef.append(obj.key)

        elapsed_time = time.time() - start_time
        print(elapsed_time)

    step1and2func()
    step3()

    print("finished running")
main()
