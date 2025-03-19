import xmlrpc.client
class Connection:
    def credentials(self):
        return {
            "url": "http://127.0.0.1:8069",
            "db": 'odoo_db',
            "username": "ferzg2004@gmail.com",
            "password": "e5f76044f62b4a8cc3c5c9f3db7079c2d3bec136"
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