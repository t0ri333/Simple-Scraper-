import requests
from bs4 import BeautifulSoup
# Set the user-agent string to identify the scraper as a web browser
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

# Send a GET request to the website using the specified user-agent string
response = requests.get('https://www.starterstory.com/one-person-business-ideas', headers={'User-Agent': user_agent})

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all p elements on the page
paragraphs = soup.find_all('h2')

# Loop through the paragraph elements and print their text
for p in paragraphs:
    print(p.text)


