from Connection import Connection


class FindTemplateProductByCodeRepository:

    def execute(self, code):
        connection =  Connection()
        response = connection.model_execute_search_read("product.template", [("default_code", "=", code)])
        return response
        