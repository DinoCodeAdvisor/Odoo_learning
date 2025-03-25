import xmlrpc.client
import csv, objetos

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
                'standar_price': float(row['standart_price']),
                'categ_id': float(row['category']),
                'image': row['image']
                'type': 'product'
            }

            products.append(product_data)

        for product in products:
            response = self.model_execute_create('product.template', product)
            print(f'Created product: {response}')