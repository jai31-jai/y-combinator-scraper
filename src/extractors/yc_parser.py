thonimport requests
from bs4 import BeautifulSoup

def parse_yc_data(url):
    # Send request to the Y Combinator URL
    response = requests.get(url)
    
    # Check if the request is successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data from {url}")
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    companies = []
    # Example of extracting data (this should be adapted based on actual HTML structure)
    for company_div in soup.find_all('div', class_='company-listing'):
        company = {
            "company_name": company_div.find('h3').text.strip(),
            "company_location": company_div.find('span', class_='location').text.strip(),
            "company_website": company_div.find('a', href=True)['href'],
            # Other fields as necessary
        }
        companies.append(company)
    
    return companies