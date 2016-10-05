#compare.py - Program to read 2 csv files and compare the two row by row

import csv

#Ask user for file names
input_file = input("Input new file: ")
input_file2 = input("Input old file file: ")
output_file = input("Output Filename: ")

#Open input files and create readers
fileOne = open(input_file)
fileTwo =  open(input_file2)
fileOneReader = csv.reader(fileOne)
fileTwoReader = csv.reader(fileTwo)

#create output file
outputFile = open(output_file,'w',newline='')
outputWriter = csv.writer(outputFile)
count = 0
refund = []
newLine = []
refundFound = False
position = 0
      
netDonations = 0

print("Finding new donations....") 

#Loop through first csv file row by row
for row in fileOneReader:
   stringList = row

   #Print the headers from first csv file to outputfile
   if position == 0:
      outputWriter.writerow(stringList)
   position+=1
   
   
   
   line = False

  
   
   
   #Loop through second csv file row by row
   for rowTwo in fileTwoReader:
      line = True
      stringTwoList = rowTwo
      
      #Verify same line number from each csv file
      if fileOneReader.line_num == fileTwoReader.line_num:
        #Add donation to output file if lines don't match, matches DonationID's
         if stringList[0] != stringTwoList[0]:
            print("New Donation")
            donations = stringList[6]
            netDonations += float(donations[1:])
            outputWriter.writerow(stringList)
            
         #Check for refunded donation, add refund to list
         if stringList[0] == stringTwoList[0] and stringList[4] != stringTwoList[4]:
            print("refund found")
            refund.append(stringList)
            refundFound = True
      break #exit loop after the line is read

   #Add row to output file if new donation line found
   if not line:
      print("New Donation")
      outputWriter.writerow(stringList)
      donations = stringList[6]
      netDonations += float(donations[1:])

#output of total new donations
print("Net Donations: $%.2f" % netDonations)
  

   
         

      
         
#Check if refunds exist   
if refundFound:
   outputWriter.writerow(newLine)

   #Write refunds to end of output file
   for row in refund:
      stringRefund = row
      outputWriter.writerow(stringRefund)
      #print("refund")
         

  
#close input and output files
outputFile.close()
fileOne.close()
fileTwo.close()
