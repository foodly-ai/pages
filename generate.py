import csv
import os
import re
from tqdm import tqdm 
# Create the output directory if it doesn't exist
output_dir = 'products'
os.makedirs(output_dir, exist_ok=True)

# Function to clean the product title
def clean_title(title):
    # Remove non-English characters and special characters
    cleaned_title = re.sub(r'[^a-zA-Z0-9\s\-]', '', title)
    # Replace spaces with dashes
    cleaned_title = cleaned_title.replace(" ", "-")
    # Truncate to 90 characters
    return cleaned_title[:90]

html_content_base = open("html_content.html").read()

# Open the CSV file
with open("/root/.cache/kagglehub/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/versions/17/amazon_products.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read the header
    headers = next(reader)
    
    # Display the headers for debugging
    print("Headers:", headers)

    # Iterate over the rows in the CSV file
    for i, row in tqdm(enumerate(reader), total = 500000):
        # Define parameters based on CSV structure
        product_title = row[1]
        image_url = row[2]
        product_url = row[3]
        price = float(row[6])

        # Clean the product title to create a valid filename
        filename = clean_title(product_title)

        # Prepare the HTML content
        html_content = str(html_content_base)
        html_content = html_content.replace("${product_title}", product_title)
        html_content = html_content.replace("${image_url}", image_url)
        html_content = html_content.replace("${product_url}", product_url)
        html_content = html_content.replace("${price}", str(price))
        html_content = html_content.replace("$${price.toFixed(2)}", str(price)+ " $")

        # Create the full file path using the cleaned title
        file_path = os.path.join(output_dir, f'{filename}.html')

        # Save the HTML content to the file
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        if i == 50000:  # Stop after processing 100,000 products
            break
        #break