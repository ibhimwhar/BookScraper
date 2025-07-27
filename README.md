# 📚 Book Scraper - Python Web Scraping Project

This project scrapes all books from [Books to Scrape](http://books.toscrape.com/) and saves the data into a structured `books.json` file. It extracts each book's title, price, availability, rating, and product URL using Python and BeautifulSoup.

---

## 🚀 Features

- Scrapes all pages (1000 books)
- Extracts key details for each book:
  - ✅ Title
  - ✅ Price
  - ✅ Availability
  - ✅ Rating
  - ✅ Product URL
- Saves results in a clean `books.json` file
- Uses a virtual environment (`venv`) for dependency isolation

---

## 🛠 Tech Stack

- Python 3.x
- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
- JSON
- `venv` (Python's built-in virtual environment)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/book-scraper.git
cd book-scraper
```
### 2. Create and activate a virtual environment

#### Create virtual environment
`python -m venv venv`

#### Activate on Windows
`venv\Scripts\activate`

#### Activate on macOS/Linux
`source venv/bin/activate`

### 3. Install dependencies
`pip install -r requirements.txt`

### 4. Example Output `books.json`

```json

[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "availability": "In stock",
    "rating": "Three",
    "url": "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  },
  {
    "title": "Tipping the Velvet",
    "price": "£53.74",
    "availability": "In stock",
    "rating": "One",
    "url": "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
  },
  ...
]
```
#### Deactivate your virtual environment
`deactivate`

```yaml
You can save this as `README.md` in your project root and it’s good to go! Let me know if you want me to generate a matching `requirements.txt` or `LICENSE` file too.

