import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import gender_guesser.detector as gender


url = "https://economics.uchicago.edu/people/job-market-candidates"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

data = []

#grabbing data from only the division i want
values = soup.find_all("div", class_="paragraph paragraph--type--uc-text-block paragraph--view-mode--default")

#for value in values:
    #print(value.get_text(strip=True))

#creating item columns
#the following code runs through the data in the divider that has the attributes
#that associate with the value
for people in values:
    
    item = {}
    item['name'] = people.find("a").text
    item['school'] = "University of Chicago"
    item['year'] = 2024
    item['school_website'] = people.find("a").attrs["href"]
    item['extra'] = people.find("p").text


    data.append(item)

#print(data)

#make data into data frame
df=pd.DataFrame(data)

#print(df)

#download to csv file
df.to_csv("uchicago_econ24.csv")


