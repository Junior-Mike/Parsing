import requests
from bs4 import BeautifulSoup

url = "https://www.avito.ru/moskva/avtomobili?cd=1&radius=0&searchRadius=0"

response = requests.get(url)

def parse_car_page(url):
    if response.status_code == 200:
        print(f"Error {response.status_code} when uploading the {url}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("")

