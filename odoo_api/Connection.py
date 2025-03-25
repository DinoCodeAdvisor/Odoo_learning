import xmlrpc.client

#http://localhost:8069/web/database/manager
class Connection:
    url = 'http://127.0.0.1:8069'

    def __init__(self):
        url = self.url

    def credentials(self):
        return {
            "url": "http://127.0.0.1:8069",
            "db": 'odoo_db',
            "username": "ferzg2004@gmail.com",
            "password": "Lunatico2019"
        }
        
    def execute(self) -> int:
        credentials = self.credentials()

        url = credentials["url"]
        db = credentials["db"] 
        username = credentials["username"]
        password = credentials["password"]
        
        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})
        return uid
    
    def getModel(self):
        return  xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
    

    def model_execute_search_read(self, endpoint,filters):
        credentials = self.credentials()
        db = credentials["db"]
        password = credentials["password"]

        uid = self.execute()

        models = self.getModel()

        
        ids = models.execute_kw(db, uid, password, endpoint, 'search', [filters])  #product.template
        data = models.execute_kw(db, uid, password, endpoint, 'read', [ids])  #product.template

        return data

    def model_execute_create(self, endpoint, data=None):

        
        credentials = self.credentials()
        db = credentials["db"]
        password = credentials["password"]

        uid = self.execute()
        models = self.getModel()
        try:
            response = models.execute_kw(
                db,
                uid,
                password,
                endpoint,
                "create",
                [data]
            )
            return response
        except Exception as e:
            print(e)
            return False