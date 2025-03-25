from Connection import Connection

class createTemplateProductRepository :

    def execute(self,data):
        connection  = Connection()
        response = connection.model_execute_create("product.template", data)
        print(response)
        return response
         