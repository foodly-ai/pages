import requests
from bs4 import BeautifulSoup
import json

def scrape_amazon_product(url):
    # Set the headers to mimic a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send a GET request to the Amazon product page
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the product page.")
        return

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product details
    product_details = {}

    # Extract title
    title = soup.find(id='productTitle')
    product_details['title'] = title.get_text(strip=True) if title else 'N/A'

    # Extract price
    price = soup.find('span', class_='a-price')
    product_details['price'] = price.get_text(strip=True) if price else 'N/A'

    # Extract product description
    description = soup.find('div', id='productDescription')
    product_details['description'] = description.get_text(strip=True) if description else 'N/A'

    # Extract other details (you can add more fields as needed)
    product_details['url'] = url

    # Save the details to a JSON file
    with open('product_details.json', 'w', encoding='utf-8') as f:
        json.dump(product_details, f, ensure_ascii=False, indent=4)

    print("Product details scraped and saved to product_details.json")

# Example usage
scrape_amazon_product("https://www.amazon.com/dp/B014TMV5YE?th=1")
