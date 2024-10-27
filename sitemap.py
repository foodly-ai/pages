import os

# Directory containing the product HTML files
product_dir = 'products'

# Output file for the sitemap
sitemap_file = 'sitemap.txt'

# Open the sitemap file for writing
with open(sitemap_file, 'w', encoding='utf-8') as sitemap:
    # Iterate through each file in the product directory
    for filename in os.listdir(product_dir):
        # Check if the file is an HTML file
        if filename.endswith('.html'):
            # Create the URL format (assuming the base URL is http://example.com/pages/)
            product_url = f"http://example.com/{product_dir}/{filename}"
            # Write the product URL to the sitemap file
            sitemap.write(product_url + '\n')

print(f"Sitemap saved to {sitemap_file}")
