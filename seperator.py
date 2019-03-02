#this code is written for extracting data from files and then creating a csv
#from it

import os
import csv

filenames = os.listdir(path="OpenTriviaQA/categories")

print(filenames)
print(len(filenames))


for filename in filenames:
  listOfQuestions = []
  file = open("OpenTriviaQA/categories/"+filename,"r",encoding='latin-1')

  for line in file.readlines():
    if line[0]=="#":
      question = line[3:-1]
    if line[0]=="^":
      answer = line[2:-1]
    if line[0]=="A":
      A = line[2:-1]
    if line[0]=="B":
      B = line[2:-1]
    if line[0]=="C":
      C = line[2:-1]
    if line[0]=="D":
      D = line[2:-1]
      mcq = {"question":question,"answer":answer,"A":A,"B":B,"C":C,"D":D}
      listOfQuestions.append(mcq)

  print(filename+" "+str(len(listOfQuestions)))
  
  with open(filename+".csv","w") as csvfile:
    fieldnames = ["question","answer","A","B","C","D"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for every in listOfQuestions:
      writer.writerow(every)
