import json
import os

from src.product import Category, Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def get_prod_data(data):
    categores = []
    for instance in data:
        products = []
        for product in instance["products"]:
            products.append(Product(**product))
        instance["products"] = products
        categores.append(Category(**instance))
    return categores


if __name__ == "__main__":
    prod_data = read_json("..\\data\\products.json")
    # print(prod_data)
    user_categores = get_prod_data(prod_data)
    for category in user_categores:
        print(category.name)
        print(category.description)
        print(f"category_count = {category.category_count}")
        print(f"product_count = {category.product_count}")
        for product in category.products:
            print(f"    {product.name}")
