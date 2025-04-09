from dataclasses import dataclass
from domain.model.Product import Product

@dataclass
class PrestashopProductDTO:
    reference: str
    name: str
    price: float
    description: str = ""

    def to_domain(self) -> Product:
        return Product(
            reference=self.reference,
            name=self.name,
            price=self.price,
            description=self.description
        )

"""
Recordemos que un Data Transfer Object (DTO) tiene el unico proposito de organizar la información que llega a un formato especifico.

En este caso el PrestashopProductDTO se encarga de mapear sus valores a nuestra clase de Product.

De esta forma podemos manejar lo que llegará de PrestaShop sabiendo de antemano con que información trabajaremos 
"""
