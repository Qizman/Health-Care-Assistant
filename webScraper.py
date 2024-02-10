#import library
import json
#!pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def update_Diseases():
    #get json list
    with open('diseases.json') as f:
        try:
            data = json.load(f)
        except ValueError:
            print("File is empty")
            data = []
            exit()
    #for loop to go through the list
    for i in data:
        try:
            print(i)
            #open browser
            browser = webdriver.Firefox()
            #go to the website
            browser.get(i["url"])
            #print main content from element class
            i["info"] = browser.find_element(By.CLASS_NAME, "inner-article-container").text
            #save json file
            with open('diseases.json', 'w') as f:
                json.dump(data, f)
            #quit the browser
            browser.quit()
        except Exception as e:
            print("Error: ", e)
            browser.quit()
            continue

def get_Diseases():
    #get json list
    string = ""
    with open('diseases.json') as f:
        try:
            data = json.load(f)
        except ValueError:
            print("File is empty")
            data = []
            exit()
    #for loop to go through the list
    for i in data:
        string += i["info"] + "\n"
    return string