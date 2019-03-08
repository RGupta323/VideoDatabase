#Main.py
#going to be the main function that will run and exeecute the actual project

##Video Database Project
#So this is going to create a database of video links
#Initially its going to be manually entered but what will eventually occur
#is that things will be read from a file, assembled into a dictionary or
#can be used via user input
#Then using SQLite the database will be opened, tables will be created and
#the idea is that a user can search through the database entering search terms
#and then get a list of videos that match those search terms and then
#can get the link to those videos
#if those videos have been downloaded then a video player can be initiated
#but other than taht hopefully the program should open it initially.

###########################################################################
import sqlite3
from Search import *
from Table import * 
#connecting to database
conn = sqlite3.connect("VideoDatabase2.db")
#print("Connected to database successfully!") #connected successfully

#creating table inside database
try: 
    conn.execute('''CREATE TABLE VIDEOS
(TITLE TEXT NOT NULL,
URL TEXT NOT NULL,
TAGS TEXT NOT NULL);''')
except:
    print("Table already created")
#print("Table created successfully") #table created successfully
conn.commit()
conn.close()
#Okay so from here we can fill the table
#This can be done via file, user input, but for now I'm just going to manaully
#enter them in.
option=input("""Welcome! If you would like to search, enter 0, if you would
like to enter data into a database enter 1.
input: """)
#for searching
if(int(option)==0):
    userInput=input("Please enter what you would like to search: ")
    search(userInput)
#entering stuff into a database
else:
    option=input("""Please enter 0 if you would like to manually
input the title, url and tags of the video or enter 1 if you have a text
 file that already has those things. Or enter 2, if you would like to auto add
 essentially what that is, is that this program will search teh type of videos
 you want, like you would normally serach on google and youtube, it collects
 those urls for you, and puts them into the database itself. 
input: """)
    #entering manually
    if(int(option)==0):
        userInput() #this function works!!!
        table()
    #entering via text file
    if(int(option)==1):
        readFiles() 
        table()
    #auto add function
    if(int(option)==2):
        phrase=input('''Please enter what you would like to google search,
or a phrase you would like for the program to search. An example is: "linear
algebra basis youtube".''')
        n=input('''Please enter the number of urls or videos you would like to
                be put inside the database, if you don't wish to put a number
                the default will be 10. If you don't want to provide a number
                put -1 instead.''')
        n=int(n)
        if(n==-1):
            webscraper(phrase)
        else:
            webscraper(phrase,n)



print("Records created successfully!") #records created successfully

#from here we can access the data in the table, which will be the implementation of the search function



