import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"

response = requests.get(URL)

# Creating a BeautifulSoup object for parsing the received HTML
soup = BeautifulSoup(response.text, "html.parser")

# Searching for all <div> elements with the "quote" class
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text # Find the text of the quote
    author = quote.find("small", class_="author").text # Find the author's name
    tags = []
    # Finding all <a> tags with the "tag" class
    for tag in quote.find_all("a", class_="tag"):
        tags.append(tag.text)

    print(f"Quote: {text}\nAuthor: {author}\nTags: {', '.join(tags)}\n{'-'*50}")