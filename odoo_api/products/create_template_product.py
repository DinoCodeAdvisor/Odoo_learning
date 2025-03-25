from Connection import Connection
from infrastructure.domain.repository.FindTemplateProductByCodeRepository import FindTemplateProductByCodeRepository
from infrastructure.domain.repository.createTemplateProductRepository import createTemplateProductRepository as CreateTemplateProductRepository
import sys




products = [
     {
    "name": "Product 123",
    "default_code": "PROD123",
    "type": "product",
    "list_price": 100,
    "standard_price": 50,
    "categ_id": "peluches"
},
   {
    "name": "Product 123",
    "default_code": "PROD123",
    "type": "product",
    "list_price": 100,
    "standard_price": 50,
    "categ_id": "limpieza"
}

]

for product in products:


    # busqueda de categorya por nombre
    # en caso de no existir se crea la categoria, se toma el ID

    findTemplateProductByCodeRepository = FindTemplateProductByCodeRepository()
    find = findTemplateProductByCodeRepository.execute(product["default_code"])

    if len(find) > 0:
        ## Method de actualización 
        sys.exit("Product already exists")


    createTemplateProductRepository = CreateTemplateProductRepository()
    createTemplateProductRepository.execute(product)

print(product)
    