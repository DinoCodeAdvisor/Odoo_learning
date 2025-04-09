from dataclasses import dataclass
from domain.model.Product import Product

@dataclass
class OdooProductDTO:
    reference: str
    name: str
    price: float
    description: str = ""
    id: int = None

    @staticmethod
    def from_domain(product: Product):
        return {
            "default_code": product.reference,
            "name": product.name,
            "list_price": product.price,
            "description": product.description,
            "type": "product",
            "sale_ok": True,
            "purchase_ok": True
        }
    
    def to_domain(self) -> Product:
        return Product(
            id = self.id,
            reference=self.reference,
            name=self.name,
            price=self.price,
            description=self.description
        )

"""
Recordemos que un Data Transfer Object (DTO) tiene el unico proposito de organizar la información que llega a un formato especifico.

En este caso el OdooProductDTO se encarga de mapear sus valores a nuestra clase de Product.

De esta forma podemos manejar lo que llegará de Odoo sabiendo de antemano con que información trabajaremos.

Aqui tambien agregamos la función "from_domain" que nos permite pasar la información de nuestro Producto (traido de prestashop y convertido en tipo Product)
y prepararla para meterla a Odoo
"""
