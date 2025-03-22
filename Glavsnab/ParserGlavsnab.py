import requests
from bs4 import BeautifulSoup
import csv 
from model import Product

def parser(url:str, max_item: int):
    create_csv()

    page = 1
    count_items = 0
    while max_item > count_items:

        list_product = []

        response = requests.get(f"{url}&p={page}")

        soup = BeautifulSoup(response.text, "lxml")
        products = soup.find_all("div", class_="product-card")

        for product in products:
            if count_items >= max_item:
                break

            count_items +=1

            name = product.get("data-product-name")

            product_key = product.find("span", class_="product-card__key").text

            name_elem = product.find("meta", itemprop="name")
            link = name_elem.findNext().get("href")

            price_elem = product.find("span", itemprop="price")
            if price_elem:
                price = price_elem.get("content")
            else:
                price = "On request"
                
            list_product.append(Product(product_key=product_key, name=name, link=link, price=price))

    write_csv(list_product)
    page+=1

def create_csv():
    with open(f"D:\SB Python\Parsing\Parsing\Glavsnab\glavsnab.csv", mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["product_key",
                        "name",
                        "link",
                        "price"
                    ])

def write_csv(products: list[Product]):
    with open(f"D:\SB Python\Parsing\Parsing\Glavsnab\glavsnab.csv", mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([product.product_key,
                        product.name,
                        product.link,
                        product.price
                    ])

if __name__ == "__main__":
    parser(url="https://glavsnab.net/elektrotehnicheskoe-oborudovanie-2/rozetki-i-vyklyuchateli.html?limit=100", max_item=611)