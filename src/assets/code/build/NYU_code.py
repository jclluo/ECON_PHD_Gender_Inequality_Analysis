#import packages
import pandas as pd
from bs4 import BeautifulSoup
import gender_guesser.detector as gender

#Specify the path to the HTML file, need to download HTML as webscrapping with URL is blocked
file_path = 'C:\\Users\\Shawn\\Documents\\Python\\Stem Gender\\Job Market Candidates 2023.html'

#Load the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

#Create lists for data storing
names = []
emails = []
fields = []
websites = []
cv_links = []
papers = []
paper_links = []
advisors = []
chairs = []

#Find all the relevant sections
candidate_blocks = soup.find_all("div", class_="generic-content__content theme-content-rte")

#Iterate through each block to extract the desired information
for block in candidate_blocks:

#Extract name
    name = ''
    p_tag = block.find("p")
    if p_tag:
        b_tag = p_tag.find("b")
        if b_tag:
            name = b_tag.text.strip()
    names.append(name)

#Extract email
    email = ''
    email_tag = block.find("a", href=lambda href: href and "mailto:" in href)
    if email_tag:
        email = email_tag['href'].replace('mailto:', '').strip()
    emails.append(email)

#Extract fields
    field = ''
    field_tag = block.find(string=lambda string: "Fields:" in string)
    if field_tag:
        parent = field_tag.find_parent("p") 
        if parent:
            field_text = parent.get_text(separator=" ", strip=True).replace("Fields:", "").strip()
            field = field_text
    fields.append(field)

#Extract advisors
    advisor = ''
    advisor_tag = block.find(string=lambda string: "Advisors:" in string)
    if advisor_tag:
        parent = advisor_tag.find_parent("p")
        if parent:
            advisor_text = parent.get_text(separator=" ", strip=True).replace("Advisors:", "").strip()
            advisor = advisor_text
    advisors.append(advisor)

#Extract personal website
    website = ''
    website_tag = block.find("a", string="Website")
    if website_tag and 'href' in website_tag.attrs:
        website = website_tag['href']
    else:
        div_tag = block.find("div")
        if div_tag:
            website_tag = div_tag.find("a", href=lambda href: href and "http" in href)
            if website_tag and 'href' in website_tag.attrs:
                website = website_tag['href']
    websites.append(website)

#Extract CV link
    cv_link = ''
    cv_tag = block.find("a", string="CV")
    if cv_tag and 'href' in cv_tag.attrs:
        cv_link = cv_tag['href']
    cv_links.append(cv_link)

#Extract job market paper title and link
    paper = ''
    paper_link = ''
    paper_tag = block.find(string=lambda string: string and "Job Market Paper:" in string)
    if paper_tag:
        a_tag = paper_tag.find_next("a")
        if a_tag and 'href' in a_tag.attrs:
            paper_link = a_tag['href']
            paper = a_tag.text.strip()
    papers.append(paper)
    paper_links.append(paper_link)

#Ensure all lists are of the same length and add empty string for blank entries
max_len = max(len(names), len(emails), len(fields), len(advisors), len(websites), len(cv_links), len(papers), len(paper_links))
names += [''] * (max_len - len(names))
emails += [''] * (max_len - len(emails))
fields += [''] * (max_len - len(fields))
advisors += [''] * (max_len - len(advisors))
websites += [''] * (max_len - len(websites))
cv_links += [''] * (max_len - len(cv_links))
papers += [''] * (max_len - len(papers))
paper_links += [''] * (max_len - len(paper_links))

#Create a DataFrame to store the extracted data
data = {
    "name": names,
    "email": emails,
    "field": fields,
    "committee_member": advisors,
    "personal_website": websites,
    "cv_link": cv_links,
    "paper_name": papers,
    "paper_link": paper_links 
}

#Create new DataFrame
df = pd.DataFrame(data)

#Create and call gender guesser function
d = gender.Detector()
def guess_gender(name):
    if not name: 
        return 'unknown'
    first_name = name.split()[0]
    return d.get_gender(first_name)

#Create new gender column
df['gender'] = df['name'].apply(guess_gender)

#Add other columns
df['school'] = 'NYU'
df['school_website'] = 'https://as.nyu.edu/departments/econ/job-market/candidates1.html'
df['year'] = '2023'
df['chair'] = 'NA'
df['department'] = 'Economics'
df['disseratation'] = 'NA'

#Reorder columns
df = df[['name', 'email', 'school', 'gender', 'year', 'department','school_website', 'personal_website', 'chair', 'committee_member', 'field', 'cv_link', 'paper_name', 'paper_link', 'disseratation']]

#Save the DataFrame to a CSV file
output_path = 'C:\\Users\\Shawn\\Documents\\Python CSE 8a\\Stem Gender\\NYU_job_market_candidates.csv'
df.to_csv(output_path, index=False)

#Check first few columns
print(df.head())
