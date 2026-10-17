# Python Multipage Book Scraper

A Python web-scraping project that collects book information from [Books
to Scrape](https://books.toscrape.com/) across 50 catalogue pages. It
extracts book details, analyses prices, filters by rating, sorts by
price, and exports the results to CSV files.

## Features

* **Multipage scraping** across 50 catalogue pages.
* **Book detail extraction**, including title, star rating, price, and
availability.
* **Price analysis** to identify average, highest, and lowest prices.
* **Rating filter** to isolate books with a selected rating.
* **Price sorting** from lowest to highest.
* **CSV export** for the full catalogue, five-star books, and
price-sorted results.

## Tech Stack

* Python
* `requests` for HTTP requests
* `BeautifulSoup` with `lxml` for HTML parsing
* Python's built-in `csv` module for exporting data

## Project Structure

``` text
Python-Multipage-Scraper/
├── scrape.py   # Scrapes, analyses, filters, sorts, and exports book data
└── .gitignore
```

The script creates CSV output files when it runs.

## Requirements

* Python 3.9 or later recommended
* Internet access

## Setup

### 1\. Clone the repository

``` bash
git clone https://github.com/Ani-4a4/Python-Multipage-Scraper.git
cd Python-Multipage-Scraper
```

### 2\. Create and activate a virtual environment 

**Windows (PowerShell):**

``` powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3\. Install dependencies

``` bash
python -m pip install requests beautifulsoup4 lxml
```

## Usage

Run the scraper from the repository root:

``` bash
python scrape.py
```

The script visits the catalogue pages, extracts book information, prints
a price analysis, and writes the results to CSV files.

## Output Files

File                   Contents

\---

`Books.csv`            All scraped books
`5\_Star\_Books.csv`     Books with a five-star rating
`Cheapest\_Books.csv`   All scraped books sorted by price, ascending

Each record includes the book title, rating, price, and availability.

## How It Works

1. **Build page URLs:** the scraper starts at the catalogue homepage
and then visits pages 2 through 50.
2. **Fetch HTML:** `requests` retrieves each page.
3. **Parse listings:** BeautifulSoup and `lxml` locate each book card
and extract its title, star rating, price, and availability.
4. **Analyse prices:** the script calculates summary statistics and
identifies the least and most expensive books.
5. **Filter and sort:** it selects five-star books and sorts the
catalogue by price.
6. **Export results:** the full list, filtered list, and sorted list
are saved as CSV files.

## Example Use Cases

* Explore book prices across a catalogue.
* Find all five-star-rated books.
* Compare low-priced and high-priced titles.
* Practise web scraping, HTML parsing, data filtering, and CSV
workflows.

## Notes and Limitations

* The scraper relies on the current HTML structure of Books to Scrape;
changes to the website may require selector updates.
* Prices are interpreted from the site's displayed values, so parsing
may need adjustment if the currency format changes.
* Network errors or site availability can interrupt a scrape.
* Use responsible request rates and respect the source website's
terms.

## Possible Improvements

* Add request timeouts and retry handling.
* Save results to a database as well as CSV.
* Make the page range configurable.
* Add automated tests for parsing, filtering, and price calculations.

