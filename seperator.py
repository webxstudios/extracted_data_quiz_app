#this code is written for extracting data from files and then creating a csv
#from it
import os
import csv

filenames = os.listdir(path="OpenTriviaQA/categories")

print(filenames)
print(len(filenames))



for filename in filenames:
  question = ""
  answer = ""
  listOfQuestions = []
  file = open("OpenTriviaQA/categories/"+filename,"r",encoding='latin-1')

  for line in file.readlines():
    if line[:2]=="#Q":
      question = line[3:-1]
    elif line[0]=="^":
      answer = line[2:-1]
    elif line[0]=="A":
      A = line[2:-1]
    elif line[0]=="B":
      B = line[2:-1]
    elif line[0]=="C":
      C = line[2:-1]
    elif line[0]=="D":
      D = line[2:-1]
    elif line[:2]=="\n":
      if(question!=""):
        mcq = {"question":question,"answer":answer,"A":A,"B":B,"C":C,"D":D}
        A = ""
        B = ""
        C = ""
        D = ""
        listOfQuestions.append(mcq)
  print(filename+" "+str(len(listOfQuestions)))
  
  with open(filename+".csv","w") as csvfile:
    fieldnames = ["question","answer","A","B","C","D"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for every in listOfQuestions:
      writer.writerow(every)
    
  
