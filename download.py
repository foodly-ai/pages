import kagglehub

# Download latest version
path = kagglehub.dataset_download("asaniczka/amazon-products-dataset-2023-1-4m-products")

print("Path to dataset files:", path)

# /root/.cache/kagglehub/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products/versions/17
#  amazon_categories.csv  amazon_products.csv