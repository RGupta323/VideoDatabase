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
def webscraper(phrase, n=10):
    phrase.lower()
    title=list()
    if("youtube" not in phrase):
        phrase+=" youtube"
    j=search(phrase,tld='com',num=n, stop=1,pause=2)
    a=[element for element in j]
    #now for each url in a, find the title
    driver=webdriver.Chrome()
    for url in a:
        driver.get(url)
        wait=WebDriverWait(driver,10)
        element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                    "h1.title yt-formatted-string"))).text
        title.append(element)
    driver.quit()
    return title
    
