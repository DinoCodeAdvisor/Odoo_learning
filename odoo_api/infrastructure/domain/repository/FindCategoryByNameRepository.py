from Connection import Connection

class FindCategoryByNameRepository:

    def execute(self, name):
        connection =  Connection()
        category = connection.model_execute_search_read("product.category", [("name", "=", name)])
        return category
    
    