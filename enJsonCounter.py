# Assuming the json file has a depth of one..

# This program finds the longest "value" with most words 
# This program finds "values" that are duplicates
# This program finds if the "keys" exist in given files


def main():

    import json
    import time
    import copy
    import re 
    import collections

    import glob
    import os

    from pprint import pprint


    os.chdir("your file here")
    for file in glob.glob("*.js"):
        print(file)

    with open('common.js','r') as myfile:
        data=myfile.read().replace('\n','')
    
    class Step3:
        def __init__(self) :
            self.numberOfOccurences = 0
            self.filesFoundin = []

    # fix these hideous names
    wordSearchedinProject = Step3()

    # find all the right thing here?
    lol = re.findall('isChildOnly', data)
 
    wordSearchedinProject.numberOfOccurences += len(lol)
    wordSearchedinProject.filesFoundin.append('this.file')


    file = open('testfile.txt','w' )
    
    JsonData = json.load(open('en.json', encoding='utf8'))

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


    class RowRecord:
        def __init__(self) :
            self.wordCount = 0
            self.text = ""
            self.key = ""
            self.words = []

    start_time = time.time()
    wordsList = []
    total = 0

    for key in JsonData:
        #cast to string otherwise error
        re.sub('<.*>',' ',str(JsonData[key]))

        # create object to append to list
        item = RowRecord()
        item.wordCount = len(str(JsonData[key]).split(' '))
        item.text = JsonData[key]
        item.key = key
        item.words = str(JsonData[key]).split(' ')

        consumedData.append(item)
        wordsList.append(str(JsonData[key]))
        total += 1

    print(total)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(consumedData[0].wordCount)

    #x = bubbleSortByLength(consumedData)
    #print(x[0].key)

    y=collections.Counter(wordsList)
    f = dict(y)

    z = {}

    # move this to a generator
    for key, val in f.items() :
        if val >= 2 :
            z[key] = val

    finalDict = {}
    
    # move this to a generator
    #for key, val in z.items() :
     #   for ele in consumedData :
      #      if key == ele.text :
       #         if key in finalDict :
        #            finalDict[key].append(ele.key)
         #       else :
          #          finalDict[key] = [ele.key]
    
    #print(finalDict)    

main()

