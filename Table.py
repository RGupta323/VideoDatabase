#Table.py
#This is going to create tables either from user input or is going to take in
#a text file and create a nested dictionary of all the videos with
#their title, tags, url links, etc.
#its also to going to fill out this table.
#For each of the tags this will create a new table with the tag as the name and fill it out
#with videos that have the same tag 
#Part of the video database project

##############################################################
import sqlite3
from db_utils import db_connect


#functions to fill in the table
#main funciton table(), creates teh tables and fill in the tables
def table():
    #connecting to database
    conn=sqlite3.connect("VideoDatabase.db")
    #iterate through all the tags and create a table based on each unique tag.
    #keep in mind that there can be no repeating table with a different tag 
    d=getTags(); 

    
    #ending connection
    conn.close()



#user input
def userInput():
    print("""Hello! This porgram will automatically fill in the table based
on your responses. You will enter a title (name of the video), a url, and tags
(these will be things that can help us search for your video when you which
to watch it. Please enter done when you wish to be finished""")
    index=0;
    d=dict()
    while(True):
        title=input("Please enter title: ")
        url = input("Please enter url: ")
        tags=input("Please enter all tags that you can think of separated by commas: ")
        if(title=='done' or url=='done' or tags=='done'):
            break;
        d[index]={'title': title, 'url: ': url, 'tags': tags}
        index+=1
    return d;

#reading from a .txt file
def readFiles():
    fileName=input("Please enter file name: ")
    fileName=fileName+".txt"
    file=open(fileName,'r');
    #from here remove the /n new line when using file.readLines() and in addition create a dictionary
    d=dict()
    f=file.readLines()
    index=0
    for element in f:
        title=input("Please enter title or enter done if you wish to be done: ")
        url = input("Please enter url or enter done if you wish to be done: ")
        tags=input("Please enter all tags that you can think of seaprated by commas or enter done ")
        if(title=='done' or url=='done' or tags=='done'):
            break;
        d[index]={'title': title, 'url': url, 'tags':tags}
        index+=1
    return d;

#main functions to get all teh tags and return a list of all teh tags;
#should have no duplicates
#needs to iterate through the database, all teh tables and get teh tags 
def getTags():
    d=list()
    conn = sqlite3.connect("VideoDatabase.db")
    cur = conn.cursor()
        #d=[t for table in conn.execute('SELECT TAGS FROM VIDEOS WHERE TAGS = "table" ORDER BY TITLE').
        #fetchall() for t in conn.execute('SELECT TAGS FROM ' +table).fetchall()]
    conn.execute('SELECT TAGS FROM VIDEOS')
    tables = cur.fetchall()
    for table in tables:
        print(table)
        d.append(table)
    conn.close()
    return d; 

def getTags2():
    d=list()
    con=sqlite3.connect("VideoDatabase.db")
    cur=con.cursor()
    cur.execute('SELECT TAGS FROM VIDEOS')
    results = cur.fetchall()
    for row in results:
        print(row)
        d.append(row)
    return d; 
    
