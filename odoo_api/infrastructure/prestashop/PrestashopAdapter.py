import requests
from requests.auth import HTTPBasicAuth
from domain.model.Product import Product
from domain.repository.ProductRepository import ProductRepository
from .dto.PrestashopProductDTO import PrestashopProductDTO

class PrestashopAdapter(ProductRepository):
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.auth = HTTPBasicAuth(api_key, '')
        self.api_key = api_key
    
    def find_all(self):
        products = []
        ids_urls = f"{self.api_url}/products&output_format=JSON&ws_key={self.api_key}"
        response = requests.get(ids_urls, auth=self.auth)
        response.raise_for_status()
        ids = response.json()['products']

        print(f"[PrestaShopAdapter] find_all $ ids $: {ids}")

        for product in ids:
            id = product['id']
            product_detail_url = f"{self.api_url}/products&display=[reference,name,price,description]&filter[id]=[{id}]&output_format=JSON&ws_key={self.api_key}"
            detail_response = requests.get(product_detail_url, auth=self.auth)
            detail_response.raise_for_status()
            data = detail_response.json()['products'][0]

            dto = PrestashopProductDTO(
                reference=data['reference'],
                name=data['name'][0]['value'],
                price=float(data['price']),
                description=data.get('description', [{}])[0].get('value', '')
            )

            products.append(dto.to_domain())

        return products
    
    def find_by_reference(self, reference: str):
        raise NotImplementedError("Not needed for Prestashop Yet... Ñehehehe")
    
    def save(self, product: Product):
        raise NotImplementedError("Not needed for Prestashop Yet... Ñehehehe")

"""
El adaptador `PrestashopAdapter` implementa el repositorio de productos, específicamente para obtener 
productos desde la API de Prestashop y transformarlos en objetos de dominio de la aplicación. 

Los métodos de búsqueda por referencia y de guardado no son necesarios, ya que solo se requiere la
obtención de productos. 

Esta clase permite que la lógica de negocio interactúe con productos sin preocuparse
por los detalles de integración con Prestashop, asegurando consistencia y separación de responsabilidades.
""" 
