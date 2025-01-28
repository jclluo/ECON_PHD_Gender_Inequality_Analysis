
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
 
# Open the URL and read the HTML page
resp = urllib.request.urlopen("https://web.archive.org/web/20231210235753/https://economics.stanford.edu/graduate/job-market-candidates")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

# Find all <h2> tags
h2_tags= soup.find_all("h2") 
 
# Create a list to hold the data
candidates = []

for h2_tag in h2_tags:
    a_tag = h2_tag.find('a', href=True)
    if a_tag:  # Ensure that an <a> tag was found
        name = a_tag.get_text().strip()  # Get the text and strip whitespace
        url = a_tag['href'].strip()  # Get the href attribute
        candidates.append({'Name': name, 'Website': url})  # Add the dictionary to the list

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(candidates)

# Print the DataFrame to see the table
print(df)

    