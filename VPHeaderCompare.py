# VPHeaderCompare.py - Finds matching and unique headers and outputs groups of matching & unique 
# headers to the shell. Ability to write to a csv file.

import csv

# Get input files from user
input_file1 = input("Input first file name: ")
input_file2 = input("Input second file name: ")
output_file = input("Enter output file name: ")

# Create file readers
fileOne = open('C:/Users/Bryce/Desktop/python/HD99 Live + IVR Combined 20160906.csv')
fileTwo = open('C:/Users/Bryce/Desktop/python/HD111 Live + IVR Combined Round 2 20160906 (1).csv')
fileOneReader = csv.reader(fileOne)
fileTwoReader = csv.reader(fileTwo)

# Create output file writer
outputFile = open(output_file, 'w', newline = '')
outputWriter = csv.writer(outputFile)

rowNumber = 0
MatchListOne = []
MatchListTwo = []
FileOneUnique = []
FileTwoUnique = []

# Read rows from file one
for row in fileOneReader:
    stringOneList = row
    
    # Read row from file two
    for row in fileTwoReader:
        stringTwoList = row

        
        for i in stringOneList:
            # Save index of matching header from file one
            if i in stringTwoList:
                print("Match Found")
                print(i)
                MatchListOne.append(stringOneList.index(i))
            # Save index of unique header from file one
            else:
                FileOneUnique.append(stringOneList.index(i))
                print("Unique One")
                print(i)

        for i in stringTwoList:
            # Save index of matching header from file two
            if i in stringOneList:
                MatchListTwo.append(stringTwoList.index(i))
                print("Match Found")
                print(i)
            # Save index of unique header from file two
            else:
                FileTwoUnique.append(stringTwoList.index(i))
                print("Unique Two")
        break
    break

print("")
print("Match from file one")
for i in MatchListOne:
    print(stringOneList[i])

print("")

print("Match from file two")
for a in MatchListTwo:
    print(stringTwoList[a])

print("")
print("File One Unique")
for i in FileOneUnique:        
    print(stringOneList[i])

print("")
print("File Two Unique")
for i in FileTwoUnique:
    print(stringTwoList[i])

fileOne.close()
fileTwo.close()
outputFile.close()
                

        
