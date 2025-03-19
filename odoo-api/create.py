import xmlrpc.client
from Connection import Connection

connection = Connection()
credentials = connection.credentials()

# Use the get_credentials method to retrieve individual credentials
url, db, username, password = connection.get_credentials()

uid = connection.execute()

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# Crear un nuevo partner
new_partner_id = models.execute_kw(
    db,
    uid,
    password,
    'res.partner',
    'create',
    [{
        'name': 'Nuevo Proveedor',  # Nombre del partner
        'is_company': True,         # Indica si es una compañía
        'email': 'proveedor@example.com',  # Correo electrónico
        'phone': '1234567890',      # Teléfono
    }]
)

print(f'Nuevo partner creado con ID: {new_partner_id}')

connection.create_products_from_csv('files/products.csv')