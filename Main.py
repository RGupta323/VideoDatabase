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
#connecting to database
conn = sqlite3.connect("VideoDatabase.db")
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

#Okay so from here we can fill the table
#This can be done via file, user input, but for now I'm just going to manaully
#enter them in.

conn.execute("""INSERT INTO VIDEOS (TITLE,URL,TAGS) \
VALUES('Sith Inquisitor Ending - Full Darth Revan Set',
             "https://www.youtube.com/watch?v=-Jr_uKfbsWA%t=124",
             "Star Wars, SWTOR, Sith Inquisitor, Sith Inquistor Story Ending, Full Darth Revan Set, MMO,Game")""")
#would get user input or read from a text file from here...

conn.commit()
print("Records created successfully!") #records created successfully

#from here we can access the data in the table, which will be the implementation of the search function


conn.close()
