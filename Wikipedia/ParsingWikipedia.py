import requests
from bs4 import BeautifulSoup

# We get the headlines of articles from the main page
def get_headlines():
    URL = 'https://ru.wikipedia.org/wiki/Заглавная_страница'

    response = requests.get(URL) # Sending an HTTP request to the specified URL
    if response.status_code != 200:
        return f'Mistake: could not get the page (code {response.status_code})' 
    
    soup = BeautifulSoup(response.text, 'html.parser') # Creating a BeautifulSoup object for HTML parsing
    headlines = [] # Empty list to which we will add titles.

    block_article = soup.find('div', id="main-tfa") # Searching for the first <div> element

    for headline in block_article.find_all("a"): # In the found block, looking for all the links <a>.
        headlines.append(headline.text) # Go through them in a for loop and add their text to the list.

    return headlines

if __name__ == "__main__":
    headlines = get_headlines()
    for i, title in enumerate(headlines, 1):
        print(f"{i}. {title}")
       