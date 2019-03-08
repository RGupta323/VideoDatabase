#WebScraper.py
#So essentially the whole point of the branch called WebScraper is to
#basically have a continous adding function.
#So the user would run the main.py script, and well if they got lazy and didn't
#want to supply a .txt file or type in stuff the program would just essentailly
#search the internet by itself and webscrape the urls it would visit, and
#then by itself add those videos into the database
#Essentially they would just type what they want, like "Star Wars" or "SWTOR"
#or whatever they want and then specify how many entries they wanted.
#If they didn't specify the default would be 10.

#Programming wise it would use search() from googles interface, and essentially
#look for a title and the url, because that's all I would need.
#############################################################################
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
#Works fine!
#Bug: This only works sometimes. Literally its been tested, and sometimes a
#timeout exception will occur and other times it will run perfectly with
#literally zero change. 
def webscraper(phrase, n=5):
    phrase.lower()
    title=list()
    if("youtube" not in phrase):
        phrase+=" youtube"
    j=search(phrase,tld='com',num=n, stop=1,pause=2)
    a=[element for element in j]
    #a=list(j)
    print(a)
    #now for each url in a, find the title
    driver=webdriver.Chrome(executable_path=
                            r"C:\Users\gupta\Downloads\chromedriver.exe")
    for url in a:
        driver.get(url)
        wait=WebDriverWait(driver,10)
        element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                    "h1.title yt-formatted-string"))).text
        print(element)
        title.append(element)
    driver.quit()
    #works up till here...
    print(title)
    #adding titles and urls into the database 
    for n in range(len(title)):
        add(title[n],a[n])
    return title

#function to add a title and url to a database 
def add(title, url):
    conn=sqlite3.connect("VideoDatabase2.db")
    #insert data into videos
    print("title: {} \n url: {}".format(title,url))
    conn.execute('''INSERT INTO VIDEOS (TITLE,URL,TAGS) VALUES (?,?,?);''',
                 (title,url,"",))
    conn.commit()
    conn.close()
