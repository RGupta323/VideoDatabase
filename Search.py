#Search.py
#This file is going to contain the search implementation
#Basically a user can input a phrase or a title of a video adn then
#this will search through the database and then print out all possible
#videos that match or contain that phrase, then the user can select
#what option of video they want, and then that will be played.
#But this file, will only cover all functions and classes associated with
#searching.
#######################################################################
from Table import * #importing all functions from Table.py
import sqlite3
from db_utils import db_connect
import webbrowser
#Searches through all the function to see if any match the userInput
#Then prints out the url. 
def search(userInput):
    conn=sqlite3.connect("VideoDatabase.db")
    cur=conn.cursor()
    #iterate through database and create the objects first.
    d=getTags()
    cur.execute('SELECT TITLE,URL,TAGS FROM VIDEOS')
    results=cur.fetchall()
    p=Playlist()
    for row in results:
        e=Entry(row[0],row[1],row[2])
        #print(e)
        p.add(e)
    #print(p.length())
    #from here need to iterate through all the tables within the VideoDatabase
    for table in d:
        e=Entry(d[table][0],d[table][1],"")
        p.add(e)
    #now search through Playlist and all the entry objects.
    #print(p.getTags()); 
    final = Playlist()
    #print(p)
    for n in range(p.length()):
        #now begin searching.
        if(p.get(n).getTitle()==userInput or p.get(n).getUrl()==userInput
           or p.get(n).getTags()==userInput or userInput in p.get(n).getTags()):
            print(str(n)+".) "+p.toString(n))
            final.add(p.get(n))
        
    #now that final has been built which is a playlist object of all things
    #that match the user input.

    index=input("""Please select an option, by the number which the video appear
        next to: """)
    index=int(index)
    #print(index)
    #print(final.length())
    return final.select(index)
#in order to carry out the search() more efficiently a playlist object will
#be made.
#This will have the ability to select an option for videos,
#to add stuff in a database if need be,
class Playlist:
    d=[]
    def __init__(self):
        self.d=[]
    #methods: add(), repr(),

    #the argument in add() is going to be an entry object 
    def add(self,a):
        self.d.append(a)
    def remove(self,a):
        self.d.remove(a)
    def get(self,i):
        return self.d[i];
    def length(self):
        return len(self.d)
    def select(self,i):
        return self.d[i].openURL()
    def __repr__(self):
        for element in self.d:
            print(element)
    def toString(self,i):
        return "{}, {}, {}".format(self.d[i].getTitle(),
                                   self.d[i].getUrl(),
                                   self.d[i].getTags())

#Playlist is going to be a collection of theese entry objects
#which are gonna contain title, url, and tags for each video per say
class Entry:
    def __init__(self,title, url, tags):
        self.title=title
        self.url=url
        self.tags=tags
    #get methods
    def getTitle(self):
        return self.title
    def getUrl(self):
        return self.url;
    def getTags(self):
        return self.tags;
    #function to open the url
    def openURL(self):
        path="C:/Program Files (x86)/Google/Chrome/Application.chrome.exe"
        #return webbrowser.open(self.url)
        return webbrowser.get(path).open(self.url)
    def __repr__(self):
        return "Title: {}, URL: {}, Tags: {}".format(
            self.title,self.url,self.tags)
