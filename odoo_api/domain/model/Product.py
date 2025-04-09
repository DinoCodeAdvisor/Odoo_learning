from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    reference: str
    name: str
    price: float
    description: str = ""
    id: Optional[int] = None

"""

Es una plantilla general de lo minimo indispensable que requiere un producto.

Da igual si es de Prestashop o Odoo, esos ya los definiremos luego.

Esto nos permite mantener una lógica de negocio estable, consistente y sin la necesidad de depender de formatos externos (como lo serian Odoo o Prestashop)

"""