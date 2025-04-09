import xmlrpc.client
from domain.repository.ProductRepository import ProductRepository
from domain.model.Product import Product
from .dto.OdooProductDTO import OdooProductDTO

class OdooAdapter(ProductRepository):
    def __init__(self, url: str, db: str, username: str, password: str):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        
        # Odoo endpoints
        self.common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common')
        self.models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object')

        # Authentication
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})

    def find_by_reference(self, reference: str) -> Product:
        # Search for the product by its default code (reference)
        product_ids = self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'search', [[('default_code', '=', reference)]])
        
        if not product_ids:
            return None
        
        # Get the product data
        product = self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'read', [product_ids], {'fields': ['id','default_code', 'name', 'list_price', 'description']})
        
        data = product[0]
        dto = OdooProductDTO(
            id=data['id'],
            reference=data['default_code'],
            name=data['name'],
            price=float(data['list_price']),
            description=data.get('description', '')
        )

        return dto.to_domain()  # Converts Odoo DTO to domain Product object

    def save(self, product: Product) -> None:
        existing = self.find_by_reference(product.reference)
        dto = OdooProductDTO.from_domain(product)  # Convert Product to Odoo DTO

        if existing:
            # Update existing product
            product_id = existing.id
            self.models.execute_kw(self.db, self.uid, self.password,
                'product.product', 'write', [[product_id], {
                    'default_code': dto['default_code'],
                    'name': dto['name'],
                    'list_price': dto['list_price'],
                    'description': dto['description']
            }])
        else:
            # Create new product
            self.models.execute_kw(self.db, self.uid, self.password,
                'product.product', 'create', [{
                    'default_code': dto['default_code'],
                    'name': dto['name'],
                    'list_price': dto['list_price'],
                    'description': dto['description']
            }])

    def find_all(self) -> list[Product]:
        # Get all products
        product_ids = self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'search', [])
        
        products = self.models.execute_kw(self.db, self.uid, self.password, 'product.product', 'read', [product_ids], {'fields': ['default_code', 'name', 'list_price', 'description']})
        
        return [OdooProductDTO.to_domain() for _ in products]
