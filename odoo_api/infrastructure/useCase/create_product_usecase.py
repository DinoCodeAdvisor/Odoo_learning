import csv
import os
from infrastructure.domain.dto.product_dto import ProductDTO
from infrastructure.domain.repository.product_repository import ProductRepository

class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, csv_file_path):
        abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), csv_file_path)
        if not os.path.exists(abs_path):
            print(f"File not found: {abs_path}")
            return
        
        products = []
        with open(abs_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                image_path = os.path.join(os.path.dirname(abs_path), row['image']) if row['image'] else None
                
                product_dto = ProductDTO(
                    name=row['name'],
                    default_code=row['default_code'],
                    list_price=float(row['list_price']),
                    standard_price=float(row['standard_price']),
                    category_id=int(row['category']),
                    image_path=image_path
                )
                products.append(product_dto)

        for product_dto in products:
            response = self.product_repository.create_product(product_dto)
            print(f'Created product ID: {response}')
