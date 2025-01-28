# Overview of Possible Gender Inequality Among TOP 20 Economics PhD Programs
## Table of Content
- [Project Overview](#project-overview)

- [Targeted Institutions](#targeted-institutions)

- [Data Processing Steps](#data-processing-steps)

- [Code Guide - refer to files with brief description](#code-guide---refer-to-files-with-brief-description)

- [Analysis](#analysis)

## Project Overview
### About
For this project, we collected comprehensive data on job market candidates from the top 20 Economics PhD programs in the United States, including information on gender, fields of study, and dissertation topics. Additionally, we gathered job placement data from the same institutions to analyze the employment outcomes (e.g., company or institution, position) of graduating PhD students.

Our analysis involved generating summary statistics and conducting regression analyses to examine the relationship between gender and job placement outcomes.
### Contributions:
- Lea Angelakos
- Samantha Chan
- Amy Dao
- Chris Luo
- Jia Yi (Tracy) Zhao


## Targeted Institutions
### Top 20  Economics Schools (US News, 2022)
A majority of the data are from the very best Economics institution ranked by the US News:
- Harvard
- MIT
- Stanford
- Princeton
- University of California, Berkeley
- University of Chicago
- Yale University
- Northwestern University
- Columbia University
- University of Pennsylvania
- New York University
- University of California, Los Angeles
- University of Michigan, Ann Arbor
- California Institute of Technology
- Cornell University
- University of California, San Diego
- University of Wisconsin, Madison
- Duke University
- University of Minnesota, Twin Cities
- Brown University

### Additional Schools:
In addition, we also include the other institutions in the UC system:
- University of California, Davis
- University of California, Merced
- University of California, Riverside
- University of California, Irvine

### Schools & Departments
|University                            |department       |
|--------------------------------------|-----------------|
|Harvard University                    |Economics        |
|Massachusetts Institute of Technology |Economics        |
|Stanford                              |Economics        |
|Princeton                             |Economics        |
|University of California, Berkeley    |Economics        |
|University of California, Berkeley    |HASS             |
|University of California, Berkeley    |ARE              |
|University of Chicago                 |Buisness         |
|University of Chicago                 |Economics        |
|Yale University                       |Economics        |
|Northwestern                          |Economics        |
|Northwestern                          |Economics        |
|Columbia University                   |Economics        |
|University of Pennsylvania            |Economics        |
|New York Univiersity                  |Economics        |
|University of California, Los Aangeles|Economics        |
|University of Michigan, Ann Arbor     |Economics        |
|California institue of Technology     |Economics        |
|Cornell University                    |Economics        |
|UC San Diego                          |Business         |
|UC San Diego                          |Economics        |
|UC San Diego                          |Political Science|
|University of Wisconsin, Madison      |Economics        |
|Duke University                       |Economics        |
|University of Minnesota, Twin Cities  |Economics        |
|Brown University                      |Economics        |
|UC Merced                             |Economics        |
|UC Merced                             |Political Science|
|UC Davis                              |Economics        |
|UC Davis                              |Political Science|


## Data Processing Steps
### Identifying the attribute
Before gathering data, we first decided the targarted variables for each dataset:

| Column Name         | Description                            |
|---------------------|----------------------------------------|
| name                | Full name                             |
| gender_guess        | Gender using `gender_guesser`         |
| school_website      | School website                        |
| field               | Field of interest                     |
| paper_name          | Job market paper name                 |
| paper_link          | Link to job market paper              |
| chair               | Chair                                 |
| committee_members   | Committee members                     |
| year                | Year of completion                    |
| university          | University name                       |
| department          | Department                            |
| cv_link             | Link to CV                            |
| thesis              | Dummy if thesis is downloaded         |
| personal_website    | Personal website                      |
| placement           | Where candidates were placed          |
| placement_type      | Type of placement                     |
| academic            | Dummy if `placement_type` is academic |
| postdoc             | Dummy if placement was postdoc        |
| gender_manual       | Manual fixes for gender               |
| thesis_name         | Name of thesis                        |

### Data Scraping 
This table shows our result with retrieving the relevant data:

|school                                |department       |jmc available?|jmc years available|have we scraped it?(JMC|placement available?(name,instituion,job title)|placement years available|have we scraped it?(historical placements)|Contributor        |jmc link                                                                                                             |placement link                                                                  |
|--------------------------------------|-----------------|--------------|-------------------|-----------------------|-----------------------------------------------|-------------------------|------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
|Harvard University                    |Economics        |1             |[2024]             |0                      |name. institution                              |[2005,2023]              |0                                         |Chris Luo          |https://www.economics.harvard.edu/job-placement                                                                      |                                                                                |
|Massachusetts Institute of Technology |Economics        |1             |[2024]             |0                      |institution                                    |[2019,2023]              |0                                         |Chris Luo          |https://economics.mit.edu/academic-programs/phd-program/job-market                                                   |                                                                                |
|Stanford                              |Economics        |              |[2023]             |1                      |name, institution                              |[2005,2025]              |0                                         |                   |                                                                                                                     |                                                                                |
|Princeton                             |Economics        |              |                   |                       |                                               |[2010,2024]              |0                                         |                   |                                                                                                                     |                                                                                |
|University of California, Berkeley    |Economics        |1             |[2024]             |1                      |institution, job title                         |[2006,2024]              |1                                         |Chris Luo          |https://econ.berkeley.edu/graduate/professional-placement                                                            |                                                                                |
|University of California, Berkeley    |HASS             |1             |[2024]             |1                      |name, institution, job title                   |[2013,2024]              |1                                         |Chris Luo          |https://haas.berkeley.edu/phd/careers/                                                                               |                                                                                |
|University of California, Berkeley    |ARE              |0             |[]                 |0                      |name, institution, job title                   |[2003,2024]              |1                                         |Chris Luo          |https://are.berkeley.edu/job-candidates                                                                              |                                                                                |
|University of Chicago                 |Buisness         |1             |[2024]             |1                      |0                                              |0                        |0                                         |Chris Luo          |https://www.chicagobooth.edu/phd/career-outcomes                                                                     |                                                                                |
|University of Chicago                 |Economics        |1             |[2024]             |1                      |0                                              |0                        |0                                         |Chris Luo          |https://economics.uchicago.edu/people/2024-25-job-market-candidates                                                  |                                                                                |
|Yale University                       |Economics        |1             |[2024]             |1                      |name, institution                              |[1998,2024]              |1                                         |Samantha Chan      |Reference yale_econ_jm_candidates_wayback_links.csv                                                                  |https://economics.yale.edu/phd-program/placement/outcomes                       |
|Northwestern                          |Economics        |              |[2024]             |1                      |                                               |[2005,2024]              |0                                         |Lea Angelakos      |https://economics.northwestern.edu/people/phd-job-market-candidates/                                                 |https://economics.northwestern.edu/graduate/prospective/placement.html          |
|Northwestern                          |Economics        |              |[2023]             |1                      |                                               |                         |0                                         |                   |                                                                                                                     |                                                                                |
|Columbia University                   |Economics        |1             |[2024]             |1                      |name, institution                              |[2011,2024]              |1                                         |Jia Yi (Tracy) Zhao|                                                                                                                     |                                                                                |
|University of Pennsylvania            |Economics        |1             |[2024]             |1                      |name, institution                              |[2006,2024]              |1                                         |Jia Yi (Tracy) Zhao|                                                                                                                     |                                                                                |
|New York Univiersity                  |Economics        |1             |[2024]             |0                      |institution                                    |[2012, 2023]             |0                                         |Chris Luo          |https://as.nyu.edu/departments/econ/job-market.html                                                                  |                                                                                |
|University of California, Los Aangeles|Economics        |1             |[2024]             |0                      |name, institution, job title                   |[1999, 2023]             |0                                         |Chris Luo          |https://economics.ucla.edu/                                                                                          |                                                                                |
|University of Michigan, Ann Arbor     |Economics        |1             |[2024]             |0                      |name, institution                              |[2014, 2023]             |0                                         |Chris Luo          |https://lsa.umich.edu/econ/doctoral-program/                                                                         |                                                                                |
|California institue of Technology     |Economics        |1             |[2024]             |0                      |0                                              |0                        |0                                         |Chris Luo          |https://www.hss.caltech.edu/graduate-studies/job-market-candidates                                                   |                                                                                |
|Cornell University                    |Economics        |1             |[2024]             |0                      |name, job title                                |[2007.2023]              |0                                         |Chris Luo          |https://economics.cornell.edu/node/4828                                                                              |                                                                                |
|UC San Diego                          |Business         |1             |[2023]             |1                      |                                               |                         |1                                         |Amy Dao            |https://web.archive.org/web/20230128160900/https://rady.ucsd.edu/programs/phd/phd-students/job-market-candidates.html|https://rady.ucsd.edu/programs/phd/phd-alumni.html                              |
|UC San Diego                          |Economics        |1             |[2024]             |1                      |                                               |                         |1                                         |Amy Dao            |https://economics.ucsd.edu/graduate-program/jobmarket-tab/index.html                                                 |https://economics.ucsd.edu/graduate-program/jobmarket-tab/placement-history.html|
|UC San Diego                          |Political Science|1             |[2024]             |1                      |                                               |                         |1                                         |Amy Dao            |https://polisci.ucsd.edu/grad/hire-a-phd/index.html                                                                  |https://polisci.ucsd.edu/grad/placement/Graduate-Placement-Table.pdf            |
|University of Wisconsin, Madison      |Economics        |1             |[2024]             |0                      |name, institution, job title                   |[2010, 2023]             |0                                         |Chris Luo          |https://econ.wisc.edu/doctoral/                                                                                      |                                                                                |
|Duke University                       |Economics        |1             |[2024]             |0                      |0                                              |0                        |0                                         |Chris Luo          |https://econ.duke.edu/graduate/hire-duke-phd                                                                         |                                                                                |
|University of Minnesota, Twin Cities  |Economics        |0             |[]                 |0                      |name, institution, job title                   |[2012, 2023]             |0                                         |Chris Luo          |https://cla.umn.edu/economics/graduate/job-placement-achievements                                                    |                                                                                |
|Brown University                      |Economics        |1             |[2024]             |0                      |0                                              |0                        |0                                         |Chris Luo          |https://economics.brown.edu/job-market-candidates-0                                                                  |                                                                                |
|UC Merced                             |Economics        |              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |https://economics.ucmerced.edu/graduate-students                                                                     |                                                                                |
|UC Merced                             |Political Science|              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |https://polisci.ucmerced.edu/hire-phd                                                                                |https://polisci.ucmerced.edu/people/graduate-student-placements                 |
|UC Davis                              |Economics        |              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |https://economics.ucdavis.edu/people/on-the-job-market                                                               |https://economics.ucdavis.edu/graduate-student-placements                       |
|UC Davis                              |Political Science|              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |https://ps.ucdavis.edu/job-market-0                                                                                  |https://ps.ucdavis.edu/placement-record                                         |
|UC Riverside                          |Economics        |              |                   |                       |                                               |                         |                                          |Amy Dao            |https://economics.ucr.edu/graduate-job-candidates/                                                                   |https://economics.ucr.edu/graduate-program/placement/                           |
|UC Riverside                          |Political Science|              |                   |                       |                                               |                         |                                          |Amy Dao            |https://business.ucr.edu/phd-students                                                                                |https://politicalscience.ucr.edu/placement                                      |
|UC Riverside                          |Business         |              |                   |                       |                                               |                         |                                          |Amy Dao            |https://politicalscience.ucr.edu/hire-ucr-phd                                                                        |https://politicalscience.ucr.edu/placement                                      |
|UC Santa Cruz                         |Economics        |              |                   |                       |                                               |                         |                                          |Amy Dao            |https://economics.ucsc.edu/academics/graduate-program/PhD/job-market/candidates_23-24.html                           |                                                                                |
|UC Santa Barbara                      |Economics        |              |                   |                       |                                               |                         |                                          |Amy Dao            |https://econ.ucsb.edu/programs/graduate/candidates                                                                   |                                                                                |

### Data Cleaning
Here is an excerpt of our merged dataset, refer to [this](data/clean/gender_gap_PhD_STEM.csv) for detail information: 
| Name               | Gender Guess | School Website                                   | Field                                      | Paper Name                                         | Paper Link                                   | Chair                          | Committee Member                            | Year  | University           | Placement                                      | Placement Type   | Academic | Postdoc | Degree | References |
|--------------------|--------------|------------------------------------------------|-------------------------------------------|---------------------------------------------------|----------------------------------------------|-------------------------------|---------------------------------------------|-------|----------------------|------------------------------------------------|------------------|----------|---------|--------|-----------|
| Dong Woo Hahm      | andy         | http://dongwoohahm.com                         | Applied Microeconomics, Economics of Education, Labor | Leveraging Uncertainties to Infer Preferences: An Application | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Yeon-Koo Che, Miguel Urquiola | Pierre-André Chiappori, YingHua He           | 2024  | Columbia University  | University of Southern California (Teaching) | Academic         | 1.0      | 0.0     | NaN    | NaN       |
| Susannah Scanlan   | female       | https://econ.columbia.edu/e/susannah-scanlan/ | Macroeconomics, Econometrics              | Attention Allocation and the Factor Structure     | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Serena Ng, Michael Woodford   | Hassan Afrouzi, Jennifer La'O               | 2024  | Columbia University  | Capital Fund Management                       | International Org | 0.0      | 0.0     | NaN    | NaN       |
| Seung-hun Lee      | unknown      | https://seunghunlee918.github.io              | Development Economics, Political Economy, Public Policy | Organized Crime, Local Politicians, and State Capacity | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Suresh Naidu                  | Michael Best, Rodrigo Soares                | 2024  | Columbia University  | Post-doc HKUST-SNUTaipei School of Economics | Academic         | 1.0      | 1.0     | NaN    | NaN       |
| Qianyang Zhang     | unknown      | http://qianyangz.github.io                    | Industrial Organization, Microeconomics, Urban Economics | Equilibrium Effects of Energy Efficiency Disclosures | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Don Davis, David Weinstein    | Gautam Gowrisankaran                         | 2024  | Columbia University  | Amazon                                        | Industry         | 0.0      | 0.0     | NaN    | NaN       |
| Parijat Lal        | male         | http://www.parijatlal.com                     | Development Economics, Public Economics, Labor | Cooperatives, Competition, and Compensation: Evidence from... | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Michael Best                   | Joseph Stiglitz, Eric Verhoogen, Jack Willis | 2024  | Columbia University  | Post-doc Columbia Business School            | Academic         | 1.0      | 1.0     | NaN    | NaN       |


## Code Guide 
### Data Scraping using Python
Here is a **very** brief overview of how data scraping works with Python.
1. **Import Required Packages**:
    - To start, you should install and import required packages.
    - Use `requests` to fetch webpage content.
    - Use `BeautifulSoup` from `bs4` for parsing HTML data.
   ```python
   import requests
   from bs4 import BeautifulSoup
   ```
2. **Fetch Webpage Content**:
    - Use requests.get(URL) to retrieve the HTML or text from a website.
    ```python
    response = requests.get("https://example.com")
    html_content = response.text
     ```
3. **Parse HTML Content**:
    - Use BeautifulSoup to convert raw HTML into a navigable object.
    ```python
    soup = BeautifulSoup(html_content, "html.parser")
    ```
4. **Extract Data**:
    - Locate elements using tags, classes, or IDs (e.g., soup.find_all('tag')).
    ```python
    data = soup.find_all('div', class_='data-class')
    ```
5. **Clean and Structure Data**:
    - Process extracted data into a structured format (e.g., list or dictionary).
6. **Save Data to CSV**:
    - Use pandas or csv to save data for analysis.
    ```python
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False)
    ```

### Corresponding files
Please refer to file_guide spreadsheet to see a more specific format of this section of the Readme:
| School                              | File name                                  | Description                                                                  |
|------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------|
| NYU                                 | [NYU_code.py](code/build/NYU_code.py)                              | Scrapes NYU JMC data and performs analysis.                                  |
| UCB and UChicago                    | [UCB_UCHICAGO_SCRAPE.ipynb](code/build/UCB_UCHICAGO_SCRAPE.ipynb)  | Scrapes JMC information and processes data.                                  |
| UC Davis Economics PhD              | [UCD_EconPhD.ipynb](code/build/UCD_EconPhD.ipynb)                  | Extracts and processes Economics PhD data.                                   |
| UC Davis Political Science PhD      | [UCD_PoliSciPhD.ipynb](code/build/UCD_PoliSciPhD.ipynb)            | Handles Political Science PhD data scraping and processing.                  |
| UC Merced Economics PhD             | [UCM_EconPhD.ipynb](code/build/UCM_EconPhD.ipynb)                  | Analyzes Economics PhD data.                                                 |
| UC Merced Political Science PhD     | [UCM_PoliSciPhD.ipynb](code/build/UCM_PoliSciPhD.ipynb)            | Scrapes and processes Political Science PhD data.                            |
| UCSD Business PhD                   | [UCSD_BusinessPhD.ipynb](code/build/UCSD_BusinessPhD.ipynb)        | Analyzes Business PhD data.                                                  |
| UCSD Economics PhD                  | [UCSD_EconPhD.ipynb](code/build/UCSD_EconPhD.ipynb)                | Extracts and cleans Economics PhD data.                                      |
| UCSD Political Science PhD          | [UCSD_PoliSciPhD.ipynb](code/build/UCSD_PoliSciPhD.ipynb)          | Analyzes Political Science PhD candidate data.                               |
| University of Chicago               | [chicago8.py](code/build/chicago8.py)                              | Processes PhD candidate information.                                         |
| Northwestern Economics              | [nwecon2.py](code/build/nwecon2.py)                                | Processes Economics candidate data.                                          |
| Stanford                            | [stanford.py](code/build/stanford.py)                              | Scrapes PhD candidate data and extracts personal website links.              |
| General-purpose                     | [test6.py](code/build/test6.py)                                    | Extracts data and performs processing.                                       |
| University of Chicago (advanced)    | [u_chicago_v9.py](code/build/u_chicago_v9.py)                      | Handles advanced data processing for PhD candidates.                         |
| University of Pennsylvania Economics| [upenn_econ.csv](code/build/upenn_econ.csv)                        | Contains Economics PhD candidate data.                                       |
| Yale                                | [yale_econ_jm_candidates.ipynb](code/build/yale_econ_jm_candidates.ipynb) | Script for current (2023-2024) Yale Economics PhD candidate website scraping. |
| Yale                                | [yale_econ_jm_candidates_v2.ipynb](code/build/yale_econ_jm_candidates_v2.ipynb) | Script for past (2019-2022) Yale Economics PhD candidate web scraping.       |
| Yale                                | [yale_econ_jm_placements.ipynb](code/build/yale_econ_jm_placements.ipynb) | Script for Yale Economics PhD job placements.                                |
| Yale                                | [yale_econ_jm_candidates_wayback_links.csv](code/build/yale_econ_jm_candidates_wayback_links.csv) | CSV file with Wayback Machine links for past Yale Economics PhD candidates   |


## Analysis
### Key Insights
**Placement by Type**:
- 60.48% of candidates were placed in academic positions.
- 13.73% went to industry roles.
- 11.08% of candidates became postdocs.

**Tabular Representation of Gender Composition**
| Gender  | Overall (%) | Academic (%) | Postdoc (%) |
|---------|-------------|--------------|-------------|
| Male    | 70.65       | 69.60        | 68.57       |
| Female  | 29.35       | 30.40        | 31.43       |

The table presents the gender composition across three categories: overall, academic positions, and postdoc positions. It shows that males comprise approximately 70% of the overall dataset, with a slightly lower percentage in academic and postdoc roles (69.6% and 68.6%, respectively). Conversely, females represent about 29.3% overall, with a slightly higher proportion in academic (30.4%) and postdoc (31.4%) roles, indicating a modest increase in female representation in these specific positions.

For detailed results, see [Gender Gap PhD STEM Analysis](data/clean/gender_gap_PhD_STEM_analysis.txt).

