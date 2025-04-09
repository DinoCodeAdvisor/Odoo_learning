from abc import ABC, abstractmethod
from domain.model.Product import Product
from typing import Optional, List

class ProductRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Product]:
        pass
    
    @abstractmethod
    def find_by_reference(self, reference: str) -> Optional[Product]:
        pass
    
    @abstractmethod
    def save(self, product: Product) -> None:
        pass

"""

Veamoslo paso por paso:

1. Imports raros:
    Verás que hay imports como 'abc' o 'typing'...
    - ABC o más conocido como Abstract Base Class nos permite definir interfaces en python mediante clases abstractas. 
        (Al usar ABC como parametro le decimos a python que es una abstract base class; A este tipo de tipado se le conoce como duck-typing)
    
    - typing es una libreria que nos permite agregar tipado para marcar lo que se espera que una función retorne.
        Como te podrás imaginar, List es para que retorne una lista y Optional es para que retorne el Producto o None en caso de no encontrarlo.

2. Explicación de un repository.
    Un repository es una clase que guardará las funciones que posee nuestro programa en forma de clases abstractas.
    Esta será luego usada por el UseCase y los Adapters.

    Tenerlo de está forma separado nos permitirá luego crear nuestras compatibilidades para que no solo se puedan guardar productos de PrestaShop en Odoo,
    si no que también pueda ocurrir al revés. (Guardar productos de Odoo en Prestashop)

"""