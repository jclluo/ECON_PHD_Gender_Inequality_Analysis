# need to install pandas and lxml before running this code for a website that has a table

import pandas as pd
import ssl


ssl._create_default_https_context=ssl._create_unverified_context


scraper = pd.read_html('https://economics.northwestern.edu/people/phd-job-market-candidates/')

selected_table=scraper[0]

selected_table.to_csv('selected_table_data.csv', index=False)

#if you need to just pull one table

'''for indx, table in enumerate(scraper):
    print("*************************") #this is just a seperator
    print(idx)
    print(table)
    
print(scraper[])''' #in the brackets put the index of the table you want

print(scraper)


#this is just pull the elements of the table, it can't pull the website URLs

