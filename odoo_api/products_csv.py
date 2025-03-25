from infrastructure.adapter.product_adapter import ProductAdapter

def main():
    odoo_url = "http://localhost:8069"
    db = "odoo_db"
    username = "ferzg2004@gmail.com"
    password = "Lunatico2019"

    adapter = ProductAdapter(odoo_url, db, username, password)
    adapter.import_products_from_csv("..\data\products.csv")

if __name__ == "__main__":
    main()