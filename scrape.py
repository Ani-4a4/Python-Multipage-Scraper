from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

column_headers = [
    'Titles',
    'Ratings',
    'Price',
    'Availability'
]


def scrape_all_pages():
    all_books = []
    for page_num in range(1,51):
        if page_num == 1:
            url = 'https://books.toscrape.com/'

        else:
            url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
        
        print('Scraping page number -> ', page_num)
        books = scrape_page(url)
        all_books.extend(books)

    return all_books
    
def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    
    books_data = []

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # Titles
        h3 = book.find('h3')
        title = h3.find('a').get('title')

        # Ratings
        p = book.find('p', class_='star-rating')
        rating = p.get('class')[1]

        # Price
        x = book.find('div', class_='product_price')
        price = x.find('p').text

        # Availability
        w = book.find('p', class_='instock availability')
        available = w.text.strip()

        books_data.append([title, rating, price, available])

    return books_data

# Data analysis
def price_analysis(all_books):
    # Average
    total = 0
    highest = 0
    lowest = 10000
    expensive = [] 
    cheapest = []
    for book in all_books:
        price = float(book[2].replace('Â£',''))
        total = price + total

        # Most expensive
        if price >= highest:
            highest = price
            expensive.append(book[0])

        # Least expensive
        if price <= lowest:
            lowest = price
            cheapest.append(book[0])


    avg = round(total/len(all_books))
    print('Average price of books are: ',avg)
    print('Most expensive books are:', expensive, 'at the price of: £',highest) 
    print('The least expensive books are: ',cheapest, 'at the price of: £',lowest)

# Filter and Sort
def filter_by_rating(all_books, specific_rating):
    # Filter books by specific rating
    filtered = []
    for book in all_books:
        if book[1] == specific_rating:
            filtered.append(book)
    return filtered

def sort_by_price(all_books):
    # Sort books by price (ascending order)
    sorted_books = sorted(all_books,
                              key = lambda book: float(book[2].replace('Â£','')))
    return sorted_books

if __name__ == "__main__":
    all_books = scrape_all_pages()
    price_analysis(all_books)

    with open('Books.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_headers)
        writer.writerows(all_books)

    # Save books with specific rating
    five_star = filter_by_rating(all_books, specific_rating='Five')
    with open('5_Star_Books.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_headers)
        writer.writerows(five_star)

    # Save and sort by cheapest books
    cheap = sort_by_price(all_books)
    with open('Cheapest_Books.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_headers)
        writer.writerows(cheap)

# for i in range(len(books_data)):
#     print('Title', i + 1, ':', books_data[i][0])
#     print('Rating:', books_data[i][1])
#     print('Price:', books_data[i][2])
#     print('Availability:', books_data[i][3])
# print(books.prettify())


# Added features:
# Data analysis: 
# Price analysis - Average price, most expensive and cheapest


# Filter and sort:
# Filter books with specific rating
# Sort books by price (Ascending order)

# Create separate CSV files for different things
# Books with specific ratings
# 20 cheapest books
