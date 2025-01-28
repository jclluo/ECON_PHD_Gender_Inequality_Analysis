
import urllib.request
from bs4 import BeautifulSoup
 
resp = urllib.request.urlopen("https://economics.stanford.edu/graduate/job-market-candidates")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
tags= soup.find_all("h2")
 
#for link in tags.find('a', href=True):
    #print(link['href'])
for h2_tag in tags:
    a_tag = h2_tag.find('a', href=True)
    if a_tag:  # Ensure that an <a> tag was found
        print(a_tag['href'])