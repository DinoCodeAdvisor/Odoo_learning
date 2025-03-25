from Connection import Connection
import xmlrpc.client
import sys

connection  = Connection()

credentials = connection.credentials()


url = credentials["url"]
db = credentials["db"]
username = credentials["username"]
password = credentials["password"]


uid = connection.execute()


if not uid:
    print('Error de autenticación')
    sys.exit()

    # Conectar con el API de objetos
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [
    [
        ['is_company', '=', True]
    ]
    ])

partners = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids, ['name']])


for item in partners:
    print(item)


