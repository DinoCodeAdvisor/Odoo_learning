import xmlrpc.client
from Connection import Connection

connection = Connection()

response =  connection.model_execute_create("res.parther", {
        'name': 'Proveedor prueba clase 2',  
        'is_company': True,       
        'email': 'proveedor@example.com', 
        'phone': '1234567890',      
})




print(f'Nuevo partner creado con ID: {response}')