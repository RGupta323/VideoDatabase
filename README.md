# VideoDatabase
Creates a database using python and sqlite3 that just has a bunch of video links which can be played through the same program. 

Status: FINISHED!!!

How to use it: 
To use this: 
1. Download the repository as a zip file
2. Once you've opened it up, run Main.py. 
3. Main.py is a script so there are no functions to call. 
4. From there follow the directions, when it says "enter 0" or "enter 1", just enter 1, the actual number. 
5. When choosing videos if you choose to search, the videos would appear like: 

0.) ###, ###, ### 
1.) ###, ##,#####, 
2.) ####, #####, #####

Then just enter 1 or 0 or 2, the number. 

Another thing to note is that if you have .txt file or .csv you want to load up into the database, then you have to type .txt or .csv with your file name. 

Enjoy!



My Progress Documented 
(2/24/18)
Able to connect to database successfully
Able to make tables, get information, and insert information
Able to create a dictionary of all the tags within the VIDEOS table and have those tags via loop to have their own table. 
Those tables created now have the title and url of the video inserted. 

(2/25/18) 
Classes of Playlist and Entry created in Search.py. 
Implemented the opening of URLs in webbrowser via webbrowser library 
Search.py has been finished and tested. 
Project mostly done, just need to implement user interface. 

(2/26/18)
Worked on main.py
Edited user interface and successfully works! 
User able to enter data manually and is able to successfully be added to the database. 
Search() function also works from main.py, user is able to search for a video, successfully. 

(2/27/18)
Created Test1_TEXT.txt file, filled it with 5 video entries. Then worked on readFiles() function. 
Created FileParser.py that has functions to effectively parse through a .txt or .csv file and return a list of dictionaries from that file. 
Finished FileParser.py, tested readFile() works successfully! 

(2/28/18)
Created Test1_CSV.csv file, filled it with entries. Worked on readFiles(). 
Tested whole project. Works!!! 

Bugs: At times, the program will open urls in bing and not in chrome. 
