import os
import xml.etree.ElementTree as ET

def create_sitemap(sitemap_filename, urls):
    # Create the root element for the sitemap
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap-image/1.1")

    # Add each URL to the sitemap
    for url in urls:
        url_element = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(url_element, 'loc')
        loc.text = url
    
    # Write the sitemap to a file
    tree = ET.ElementTree(urlset)
    with open(sitemap_filename, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)

def create_root_sitemap(sitemaps_directory, sitemap_count):
    # Create the root element for the root sitemap
    root_urlset = ET.Element('sitemapindex', xmlns="http://www.sitemaps.org/schemas/sitemap-image/1.1")

    # Add each sitemap file to the root sitemap
    for i in range(1, sitemap_count + 1):
        sitemap_element = ET.SubElement(root_urlset, 'sitemap')
        loc = ET.SubElement(sitemap_element, 'loc')
        loc.text = f"https://foodly.ai/sitemaps/sitemap_{i}.xml"
    
    # Write the root sitemap to a file
    root_sitemap_filename = os.path.join(sitemaps_directory, 'sitemap.xml')
    tree = ET.ElementTree(root_urlset)
    with open(root_sitemap_filename, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)

def main():
    products_directory = 'products'  # Path to your products directory
    sitemaps_directory = 'sitemaps'  # Directory where sitemap files will be saved
    os.makedirs(sitemaps_directory, exist_ok=True)

    max_urls_per_sitemap = 50000  # Maximum URLs per sitemap file
    sitemap_count = 0  # Initialize sitemap file count
    current_urls = []  # List to hold URLs for the current sitemap

    # Traverse the products directory
    for file in os.listdir(products_directory):
        if file.endswith('.html'):
            # Construct the full URL
            url = f"https://foodly.ai/products/{file}"
            current_urls.append(url)

            # If the current sitemap exceeds the max limit, create a new sitemap file
            if len(current_urls) >= max_urls_per_sitemap:
                sitemap_count += 1
                sitemap_filename = os.path.join(sitemaps_directory, f'sitemap_{sitemap_count}.xml')
                create_sitemap(sitemap_filename, current_urls)
                print(f"Sitemap generated: {sitemap_filename}")
                current_urls = []  # Reset the current URLs for the next sitemap

    # Create the last sitemap if there are remaining URLs
    if current_urls:
        sitemap_count += 1
        sitemap_filename = os.path.join(sitemaps_directory, f'sitemap_{sitemap_count}.xml')
        create_sitemap(sitemap_filename, current_urls)
        print(f"Sitemap generated: {sitemap_filename}")

    # Create the root sitemap.xml
    create_root_sitemap(sitemaps_directory, sitemap_count)
    print(f"Root sitemap generated: {os.path.join(sitemaps_directory, 'sitemap.xml')}")

if __name__ == '__main__':
    main()
