import xmlrpc.client

class ProductRepository:
    def __init__(self, odoo_url, db, username, password):
        self.url = odoo_url
        self.db = db
        self.username = username
        self.password = password
        self.uid = None
        self.models = None
        self._authenticate()

    def _authenticate(self):
        common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common')
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object')

    def create_product(self, product_dto):
        return self.models.execute_kw(self.db, self.uid, self.password, 'product.template', 'create', [product_dto.to_dict()])
