#Search.py
#This file is going to contain the search implementation
#Basically a user can input a phrase or a title of a video adn then
#this will search through the database and then print out all possible
#videos that match or contain that phrase, then the user can select
#what option of video they want, and then that will be played.
#But this file, will only cover all functions and classes associated with
#searching.
#######################################################################
def search(userInput):
    #iterate through database and see what matches teh user input
    pass;

#in order to carry out the search() more efficiently a playlist object will
#be made.
#This will have the ability to select an option for videos,
#to add stuff in a database if need be,
class Playlist:
    d=[]
    def __init__(self):
        self.d=d
    #methods: add(), repr(),

    #the argument in add() is going to be an entry object 
    def add(a):
        pass
    def __repr__():
        pass

#Playlist is going to be a collection of theese entry objects
#which are gonna contain title, url, and tags for each video per say
class Entry:
    def __init__(self,title, url, tags):
        self.title=title
        self.url=url
        self.tags=tags
    #get methods
    def getTitle():
        return self.title
    def getUrl():
        return self.url;
    def getTags():
        return tags; 
