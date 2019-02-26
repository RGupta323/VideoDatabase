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
    conn=sqlite3.connect("VideoDatabase2.db")
    cur=conn.cursor()
    #iterate through all the tags and create a table based on each unique tag.
    #keep in mind that there can be no repeating table with a different tag 
    d=getTags();
    print(d)
    index=0
    #now create all teh tables with the tags from d
    for tags in d:
        #print(tags)
        try:
            cur.execute('''CREATE TABLE "{}"
                         (TITLE TEXT NOT NULL,
URL TEXT NOT NULL);'''.format(tags,))
        except:
            print("Table already created")
        #insert data of dictionary 
        product="INSERT INTO " + tags+" (TITLE, URL) \ VALUES (?,?)"
        print(product)
        print(d[tags])
        #conn.execute(product, (d[tags][0],d[tags][1]))
        #conn.execute("""INSERT INTO """+tags+"""(TITLE,URL)\
#VALUES("""+d[tags][0]+""","""+d[tags][1]+""")""")
        #cur.execute('INSERT INTO "{}" VALUES(?,?)'.format(tags,d[tags][0],
        print(tags);                                                   # d[tags][1],))
        cur.execute('''INSERT INTO
                    "{}" (TITLE, URL)  VALUES(?,?);'''.format(tags), (d[tags][0],
                                                             d[tags][1],))
        #print('about to commit')
        conn.commit()
    #ending connection
    conn.close()



#user input
#Status: TESTED! Works! 
#SUCCESS
def userInput():
    print("""Hello! This program will automatically fill in the table based
on your responses. You will enter a title (name of the video), a url, and tags
(these will be things that can help us search for your video when you which
to watch it. Please enter done when you wish to be finished""")
    index=0;
    d=dict()
    conn=sqlite3.connect("VideoDatabase2.db")
    cur=conn.cursor()
    while(True):
        title=input("Please enter title: ")
        if(title=='done'):
            break
        url = input("Please enter url: ")
        if(url=='done'):
            break
        tags=input("Please enter all tags that you can think of separated by commas: ")
        if(title=='done' or url=='done' or tags=='done'):
            break;
        conn.execute("""INSERT INTO VIDEOS (TITLE,URL,TAGS) \
VALUES(?,?,?)""",(title, url, tags,))
        conn.commit()
    conn.close()
    
       

#reading from a .txt file
#Status: UNTESTED
#Needs some work.... 
def readFiles():
    fileName=input("Please enter file name: ")
    if(".txt" not in fileName and ".csv" not in fileName): 
        fileName=fileName+".txt"
    conn=sqlite3.connect("VideoDatabase2.db")
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
    conn.close()

#main functions to get all teh tags and return a list of all teh tags;
#should have no duplicates
#needs to iterate through the database, all teh tables and get teh tags
#SUCCESS!!
def getTags():
    d=list()
    di=dict(); 
    con=sqlite3.connect("VideoDatabase2.db")
    cur=con.cursor()
    cur.execute('SELECT TITLE,URL,TAGS FROM VIDEOS')
    results = cur.fetchall()
    for row in results:
        print(row)
        d.append(row)
        di[row[2]]=[row[0],row[1]]
    print(d);
    print(di)
    return getTagsDict(di);

#Helper function for getTags()
#Takes in a dictionary, and modifies it so that all teh keys that have commas
#are now all separate dictionaries in one nested dictionary which have the
#same value.
#SUCCESS
def getTagsDict(d):
    a=dict()
    for keys in d.keys():
        astr=keys.split(',')
        for element in astr:
            a[element]=d[keys]
    return a;

#Helper function
#Just getting the tags, as a string
def justTags():
    d=list()
    con=sqlite3.connect("VideoDatabase2.db")
    cur=con.cursor()
    cur.execute('SELECT TAGS FROM VIDEOS')
    results=cur.fetchall()
    for row in results:
        d.append(row)
    con.close()
    return d
        
    

    
