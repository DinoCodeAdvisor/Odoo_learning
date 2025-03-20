import xmlrpc.client
import csv, os

class Connection:
    def credentials(self):
        return {
            "url": "http://127.0.0.1:8069",
            "db": 'odoo_db',
            "username": "ferzg2004@gmail.com",
            "password": "Lunatico2019"
        }

    # New helper method to extract specific credentials
    def get_credentials(self):
        credentials = self.credentials()
        return credentials["url"], credentials["db"], credentials["username"], credentials["password"]

    def execute(self) -> int:
        credentials = self.credentials()
        url = credentials["url"]
        db = credentials["db"]
        username = credentials["username"]
        password = credentials["password"]

        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})
        return uid

    # New helper method to send info to an endpoint
    def model_execute_create(self, endpoint, data=None):

        if data is None:
            return False

        url, db, username, password = self.get_credentials()

        uid = self.execute()

        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
        response = models.execute_kw(
            db,
            uid,
            password,
            endpoint,
            'create',
            [data]
        )
        return response
    
    # New helper method to create a product from an CSV file
    def create_products_from_csv(self, csv_file_path):
        path = os.path.dirname(os.path.abspath(__file__)) + csv_file_path
        print(f"Current working directory: {os.path.dirname(os.path.abspath(__file__)) + csv_file_path}")
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return

        with open(path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            products = []

            for row in csv_reader:
                product_data = {
                    'name': row['name'],
                    'default_code': row['default_code'],
                    'list_price': float(row['list_price']),
                    'type': 'product'
                }

                products.append(product_data)

            for product in products:
                response = self.model_execute_create('product.template', product)
                print(f'Created product: {response}')
        