#FileParser.py
#This is going to be a python file with all functions needed to parse a .txt
#file and .csv file
#Get the data:  title, url, and tags.
#These can be viewed as helper functions for readFiles()
##############################################################################
import csv
#main function that shoots out a list or dictionary that contains the title,
#url, and tags. This is what we'll be using for, readFiles()

#iterate through the file, get rid of the new line characters and return
#a dictionary with title, url, and tags being keys.
#so it should return something like this: [{title:"a",url:"b",tags:"cd"},{..}]
#only works for .txt files 
def parseTxtFile(fileName):
    alist=list()
    f=open(fileName,"r")
    file=f.readLines()
    for line in file:
        line=line.split(",")
        line=getRidOfNewLines(line)
        d={'title':line[0],'url':line[1],'tags':line[2:]}
        alist.append(d)
    return alist

#Helper function that takes in a list and takes out the "\n" character
def getRidOfNewLines(a):
    for n in range(len(a)):
        a[n]=a[n].replace("\n","")
    return a
            
            
        
