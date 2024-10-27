import csv
import os

# Create the output directory if it doesn't exist
output_dir = 'products'
os.makedirs(output_dir, exist_ok=True)

# Open the CSV file
with open("amazon_products.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read the header
    headers = next(reader)
    
    # Display the headers for debugging
    print("Headers:", headers)

    # Iterate over the rows in the CSV file
    for i, row in enumerate(reader):
        # Define parameters based on CSV structure
        asin = row[0]
        product_title = row[1]
        image_url = row[2]
        product_url = row[3]
        price = float(row[6])

        # Prepare the HTML content
        html_content = f"""

        
<div class="container">
    <div class="product">
        <div class="product-image">
            <img src="{image_url}" alt="{product_title}">
        </div>
        <div class="product-info">
            <span class="usa-badge">Free US Shipping</span>
            <h1 class="product-title">{product_title}</h1>
            <p class="product-description" id="description">
                Experience premium travel comfort with our expandable roller luggage. Perfect for both domestic and international travel, this 29-inch checked bag features durable softside construction, smooth-rolling wheels, and expandable capacity for those extra souvenirs. TSA-approved locks ensure your belongings stay secure throughout your journey.
            </p>
            <div class="price">${price:.2f}</div>
            <a href="{product_url}" class="buy-button">Add to Cart</a>
        </div>
    </div>

    <div class="similar-items">
        <h2>You May Also Like</h2>
        <div class="items-grid">
            <div class="item">
                <img src="{image_url}" alt="Similar Item 1">
                <div class="item-info">
                    <a href="#">Carry-On Spinner</a>
                </div>
            </div>
            <div class="item">
                <img src="{image_url}" alt="Similar Item 2">
                <div class="item-info">
                    <a href="#">Travel Backpack</a>
                </div>
            </div>
            <div class="item">
                <img src="{image_url}" alt="Similar Item 3">
                <div class="item-info">
                    <a href="#">Hardside Luggage</a>
                </div>
            </div>
            <div class="item">
                <img src="{image_url}" alt="Similar Item 4">
                <div class="item-info">
                    <a href="#">Duffel Bag</a>
                </div>
            </div>
        </div>
    </div>
</div>

        """

        # Save the HTML content to a file named 'asin.html'
        file_path = os.path.join(output_dir, f'{asin}.html')
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Saved {file_path}")  # Print confirmation

        if i == 10000:  # Stop after processing 5 products
            break
