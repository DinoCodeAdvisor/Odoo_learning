from infrastructure.domain.repository.product_repository import ProductRepository
from infrastructure.useCase.create_product_usecase import CreateProductUseCase

class ProductAdapter:
    def __init__(self, odoo_url, db, username, password):
        self.repository = ProductRepository(odoo_url, db, username, password)
        self.create_product_usecase = CreateProductUseCase(self.repository)

    def import_products_from_csv(self, csv_file_path):
        self.create_product_usecase.execute(csv_file_path)
