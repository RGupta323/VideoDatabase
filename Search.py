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
    def get(i):
        return self.d[i]; 
    def __repr__(self):
        return [element.repr() for element in self.d]

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
        return tags;
    #function to open the url
    def openURL(self):
        return webbrowser.open(self.url)
    def __repr__():
        return "Title: {}, URL: {}, Tags: {}".format(
            self.title,self.url,self.tags)
