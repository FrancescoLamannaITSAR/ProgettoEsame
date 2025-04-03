import requests
from bs4 import BeautifulSoup

def getClasse(classe):
    url = "https://example.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        headings = soup.find_all('h1') 
        for heading in headings:
            print(heading.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    