'''
Lea Angelakos UChicago web scraping code

This code should go through the job market candidates for the economics department
of U Chicago. Then it will put the data scraped in a pandas dataframe and export 
into a csv file to append to the main one. Hopefully this will also be able to 
guess the gender of the names on this list

'''

# importing pandas to make a data frame and importing beautiful soup to be able to 
# web scrape and other things to make the code work


import os
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
#import gender_guesser.detector as gender

# changing the working directory


# the url for uchicago econ job market
url = "https://economics.uchicago.edu/people/job-market-candidates"

'''
with open('2023-24 Job Market Candidates _ Kenneth C. Griffin Department of Economics.html','r') as uchicago:
    content = uchicago.read()

    print(content)'''

#making the soup 
url = "https://economics.uchicago.edu/people/job-market-candidates"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

data = []
#grabbing data from only the division i want
values = soup.find_all("div", class_="paragraph paragraph--type--uc-text-block paragraph--view-mode--default")

#print(values)


#creating item columns
#the following code runs through the data in the divider that has the attributes
#that associate with the value
for people in values:
    
    item = {}
    
    name = people.find("a").text # pulls name
    full_name = name.split(' ')
    item['first_name'] = full_name[0]
    item['last_name'] = full_name[1]
    # i found a page that has this years placements, but i am short on time so I am putting in in
# manually

    # all academic tenure track positions
    if 'Santiago' in item['first_name']:
        item['placement'] = 'Boston University'

    if 'Sangmin' in item['first_name']:
        item['placement'] = 'Colmbia GSB'

    if 'Sulagna' in item['first_name']:
        item['placement'] = 'Cornell University'

    if 'Toshiaki' in item['first_name']:
        item['placement'] = 'National Taiwan University'

    if 'Aleksei' in item['first_name']:
        item['placement'] = 'Princeton University'

    if 'Estéfano' in item['first_name']:
        item['placement'] = 'Universidad Adolfo Ibanez'

    if 'Marcos' in item['first_name']:
        item['placement'] = 'University of Illinois at Urbana-Champaign'

    if 'Michael' in item['first_name']:
        item['placement'] = 'University of Kentucky'

    if 'Zhiyu' in item['first_name']:
        item['placement'] = 'Washington University in St. Louis'

    # all academic non tenure track
    if 'Ivan' in item['first_name']:
        item['placement'] = 'Brown University'

    if 'Sidharth' in item['first_name']:
        item['placement'] = 'New York University Center for Data Science'

    # public sector
    if 'Michael' in item['first_name']:
        item['placement'] = 'Dapartment of Justice Expert Analysis Group'

    if 'Hazen' in item['first_name']:
        item['placement'] = 'National Security Agency'

    if 'Harshil' in item['first_name']:
        item['placement'] = 'World Bank Young Professionals'

    # private sector
    if 'Maria' in item['first_name']:
        item['placement'] = 'Amazon'

    if 'Nadia' in item['first_name']:
        item['placement'] = 'Amazon'

    if 'Jingtao' in item['first_name']:
        item['placement'] = 'Citadel Securities'

    if 'Scott' in item['first_name']:
        item['placement'] = 'RAND'

    # post doc
    if 'Shanon' in item['first_name']:
        item['placement'] = 'The University of Chicago'

    if 'Elena' in item['first_name']:
        item['placement'] = 'The University of Chicago'
    item['school'] = "University of Chicago" # school is the same for everyone
    item['year'] = 2024 # year is the same for everyone
    #item['prim_research_focus'] = people.find("span").strong
    extra = people.find("p").text # getting job market paper, research focuses, advisors, email, and personal website

    links = people.find_all('a', href = True) #finds all links 
    for link in links: # stripping the links and sorting them
        if "pdf" in link['href']:
            item['paper_link'] = link['href']

        elif "drive" in link['href']:
            item['paper_link'] = link['href']

        elif "economics.uchicago" in link['href']:
            item['school_website'] = link['href']

        else:
            item['personal_website'] = link['href']
    
    #defining words to split
    words_to_split_at = ["Primary Research Focus:", "Secondary Research Focus:", "References:", \
                         "Job Market Paper Title:", "Email:"]
    
    if item['first_name'] == 'Scott':
        print(words_to_split_at)
    #creating a regular expression pattern
    pattern = '|'.join(re.escape(word) for word in words_to_split_at)

    split_text = re.split(pattern, extra)

    if 1< len(split_text) < 6 :
        item['research_focus'] = split_text[1]
        item['committee_member'] = split_text[2]

    elif 5<len(split_text):
        item['research_focus'] = split_text[1]
        item['committee_member'] = split_text[3]

    elif item['first_name'] == 'Scott':
        item['committee_member'] = split_text[5]




    data.append(item)

if item['first_name'] == 'Ufuk':
    data.remove(item)

df = pd.DataFrame(data)



df.to_csv("uchicago_econ24.csv")