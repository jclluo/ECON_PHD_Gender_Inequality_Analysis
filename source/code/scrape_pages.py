import os
import requests
import time
from urllib.parse import urlparse
import pandas as pd
from bs4 import BeautifulSoup

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_filename(url):
    """Create a clean filename from URL"""
    parsed = urlparse(url)
    # Remove common extensions and special characters
    filename = parsed.path.rstrip('/').split('/')[-1]
    if not filename:
        filename = 'index'
    return filename

def fetch_page(url, headers):
    """Fetch webpage content with error handling"""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_html(content, filepath):
    """Save HTML content to file"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully saved: {filepath}")
    except Exception as e:
        print(f"Error saving {filepath}: {e}")

def scrape_ucsd_candidates(filepath):
    """
    Scrape candidate information from UCSD's job market page.
    
    Args:
        filepath: Path to the UCSD job market HTML file
        
    Returns:
        pandas DataFrame containing candidate information
    """
    # Read and parse HTML file
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    candidates = []
    
    # Find all candidate cards
    cards = soup.find_all('li', class_='profile-listing-card')
    
    for card in cards:
        candidate = {}
        
        # Get name
        name_elem = card.find('h3')
        candidate['name'] = name_elem.text.strip() if name_elem else None
        
        # Get all paragraphs containing information
        info_paras = card.find_all('p')
        
        for para in info_paras:
            text = para.text.strip()
            
            # Extract advisor information
            if text.startswith('Advisor(s):'):
                candidate['advisors'] = text.replace('Advisor(s):', '').strip()
                
            # Extract research fields
            elif text.startswith('Field of Research:'):
                candidate['research_fields'] = text.replace('Field of Research:', '').strip()
        
        # Get personal website
        website_link = card.find('a')
        candidate['personal_website'] = website_link['href'] if website_link else None
        
        # Get image URL if present
        img_elem = card.find('img')
        candidate['image'] = img_elem['src'] if img_elem else None
        
        # Add university
        candidate['university'] = 'UCSD'
        
        candidates.append(candidate)
    
    # Create DataFrame
    df = pd.DataFrame(candidates)
    
    # Reorder columns
    column_order = ['name', 'university', 'advisors', 'research_fields', 'personal_website', 'image']
    df = df[column_order]
    
    return df

def scrape_ucsd_placement(filepath):
    """
    Scrape placement history from UCSD's placement history page.
    
    Args:
        filepath: Path to the UCSD placement history HTML file
        
    Returns:
        pandas DataFrame containing placement history information
    """
    # Read and parse HTML file
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    placements = []
    
    # Find all tables in the document
    tables = soup.find_all('table', class_='styled')
    
    for table in tables:
        # Get all rows except header
        rows = table.find_all('tr')[1:]  # Skip header row
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:  # Ensure row has all required columns
                placement = {
                    'year': cols[0].text.strip(),
                    'name': cols[1].text.strip(),
                    'field': cols[2].text.strip(),
                    'placement': cols[3].text.strip(),
                    'university': 'UCSD'
                }
                placements.append(placement)
    
    # Create DataFrame
    df = pd.DataFrame(placements)
    
    # Reorder columns
    column_order = ['name', 'university', 'year', 'field', 'placement']
    df = df[column_order]
    
    return df

def scrape_ucsc_candidates(filepath):
    """
    Scrape candidate information from UC Santa Cruz's job market page.
    
    Args:
        filepath: Path to the UC Santa Cruz job market HTML file
        
    Returns:
        pandas DataFrame containing candidate information
    """
    # Read and parse HTML file
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    candidates = []
    
    # Find the main table containing candidate information
    table = soup.find('table')
    if not table:
        return pd.DataFrame()
    
    # Get all rows except header
    rows = table.find_all('tr')[1:]  # Skip header row
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 4:  # Ensure row has all required columns
            candidate = {}
            
            # Extract name from the link in the first column
            name_link = cols[0].find('a')
            if name_link:
                candidate['name'] = name_link.text.strip()
                candidate['personal_website'] = name_link['href']
            else:
                # If no link, try to get just the text
                name_text = cols[0].get_text(strip=True)
                if name_text:
                    candidate['name'] = name_text
                    candidate['personal_website'] = None
            
            # Get fields of interest
            candidate['research_fields'] = cols[1].get_text(strip=True)
            
            # Get job market paper
            candidate['job_market_paper'] = cols[2].get_text(strip=True)
            
            # Get references
            candidate['advisors'] = cols[3].get_text(strip=True)
            
            # Get image URL if present
            img = cols[0].find('img')
            candidate['image'] = img['src'] if img else None
            
            # Add university
            candidate['university'] = 'UC Santa Cruz'
            
            candidates.append(candidate)
    
    # Create DataFrame
    df = pd.DataFrame(candidates)
    
    # Reorder columns
    column_order = ['name', 'university', 'advisors', 'research_fields', 'job_market_paper', 'personal_website', 'image']
    df = df[column_order]
    
    return df

def scrape_ucsc_placement(filepath):
    """
    Scrape placement history from UC Santa Cruz's placement history page.
    
    Args:
        filepath: Path to the UC Santa Cruz placement history HTML file
        
    Returns:
        pandas DataFrame containing placement history information
    """
    # Read and parse HTML file
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    placements = []
    
    # Find the content div
    content_div = soup.find('div', class_='content contentBox')
    if not content_div:
        return pd.DataFrame()
    
    # Initialize variables
    current_year = None
    
    # Process all paragraphs and divs
    for element in content_div.find_all(['p', 'div']):
        text = element.get_text(strip=True)
        if not text:
            continue
            
        # Check if this is a year header
        if text.startswith('20') and len(text) == 4:
            current_year = text
            continue
            
        # Look for strong tags which typically contain names
        strong_tags = element.find_all('strong')
        for strong in strong_tags:
            name = strong.get_text(strip=True)
            if name and name != current_year:  # Skip if it's just the year
                # Get the placement info - it's typically after the dash or hyphen
                full_text = strong.parent.get_text(strip=True)
                placement_parts = full_text.split('-', 1)
                if len(placement_parts) > 1:
                    placement = placement_parts[1].strip()
                else:
                    placement = ''
                
                placement_info = {
                    'name': name,
                    'year': current_year,
                    'placement': placement,
                    'university': 'UC Santa Cruz'
                }
                placements.append(placement_info)
    
    # Create DataFrame
    df = pd.DataFrame(placements)
    
    # Reorder columns
    column_order = ['name', 'university', 'year', 'placement']
    df = df[column_order]
    
    return df

def main():
    # Create data directory
    data_dir = "data"
    create_directory(data_dir)

    # Headers for requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Dictionary of universities and their URLs
    universities = {
        'UCSD': {
            'placement': 'https://economics.ucsd.edu/graduate-program/jobmarket-tab/placement-history.html',
            'candidates': 'https://economics.ucsd.edu/graduate-program/jobmarket-tab/index.html'
        },
        'Stanford': {
            'placement': 'https://economics.stanford.edu/graduate/student-placement',
            'candidates': 'https://economics.stanford.edu/graduate/job-market-candidates'
        },
        'Princeton': {
            'placement': 'https://economics.princeton.edu/graduate-program/job-market-and-placements/statistics-on-past-placements/',
            'candidates': 'https://economics.princeton.edu/graduate-program/job-market-and-placements/2024-job-market-candidates/'
        },
        'Northwestern': {
            'placement': 'https://economics.northwestern.edu/graduate/prospective/placement.html',
            'candidates': 'https://economics.northwestern.edu/people/phd-job-market-candidates/'
        },
        'UC_Davis': {
            'placement': 'https://economics.ucdavis.edu/graduate-student-placements',
            'candidates': 'https://economics.ucdavis.edu/people/on-the-job-market'
        },
        'UC_Riverside': {
            'placement': 'https://economics.ucr.edu/graduate-program/placement/',
            'candidates': 'https://economics.ucr.edu/graduate-job-candidates/'
        },
        'UC_Santa_Cruz': {
            'placement': 'https://economics.ucsc.edu/academics/graduate-program/PhD/placement.html',
            'candidates': 'https://economics.ucsc.edu/academics/graduate-program/PhD/job-market/candidates_24-25.html'
        },
        'UC_Santa_Barbara': {
            'placement': 'https://econ.ucsb.edu/programs/graduate/placement',
            'candidates': 'https://econ.ucsb.edu/programs/graduate/candidates'
        }
    }

    # Scrape and save pages for each university
    for univ, urls in universities.items():
        print(f"\nProcessing {univ}...")
        
        # Create university directory
        univ_dir = os.path.join(data_dir, univ)
        create_directory(univ_dir)

        # Process placement page
        print("Fetching placement page...")
        placement_content = fetch_page(urls['placement'], headers)
        if placement_content:
            placement_file = os.path.join(univ_dir, f"{univ}_Placement.html")
            save_html(placement_content, placement_file)

        # Add delay between requests
        time.sleep(2)

        # Process candidates page
        print("Fetching candidates page...")
        candidates_content = fetch_page(urls['candidates'], headers)
        if candidates_content:
            candidates_file = os.path.join(univ_dir, f"{univ}_Candidate.html")
            save_html(candidates_content, candidates_file)

        # Add delay before next university
        time.sleep(2)

if __name__ == "__main__":
    main()
    print("\nScraping completed!") 