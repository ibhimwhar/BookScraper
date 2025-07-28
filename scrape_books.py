# scrape_books.py
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

BASE_URL = "http://books.toscrape.com/"

def get_books_from_page(soup):
    books = []
    book_elements = soup.select("article.product_pod")

    for book in book_elements:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        availability = book.select_one(".availability").text.strip()
        rating_class = book.select_one("p.star-rating")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "None"
        book_url = urljoin(BASE_URL, book.h3.a["href"])
        image_url = urljoin(BASE_URL, book.find("img")["src"])

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "url": book_url,
            "image": image_url
        })
    return books

def scrape_all_books():
    all_books = []
    next_page = "catalogue/page-1.html"

    while next_page:
        url = urljoin(BASE_URL, next_page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        all_books += get_books_from_page(soup)

        next_btn = soup.select_one("li.next > a")
        if next_btn:
            next_page = urljoin("catalogue/", next_btn["href"])
        else:
            next_page = None

    return all_books

books_data = scrape_all_books()
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books_data, f, indent=2, ensure_ascii=False)

print(f"Scraped {len(books_data)} books into books.json")
