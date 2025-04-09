from infrastructure.prestashop.PrestashopAdapter import PrestashopAdapter
from infrastructure.odoo.OdooAdapter import OdooAdapter
from useCase.SyncProductsUseCase import SyncProductUseCase


prestashop_adapter = PrestashopAdapter(
    api_url="http://localhost:8080/api",
    api_key="LSI3F15S5T13XMZKB5PTJL27GV4HRIEC"
)
odoo_adapter = OdooAdapter(
    url="http://localhost:8069",  
    db="odoo_db",           
    username="ferzg2004@gmail.com",            
    password="Lunatico2019"     
)
sync_use_case = SyncProductUseCase(prestashop_adapter, odoo_adapter)
sync_use_case.execute()

"""
Todo esto esta corriendo desde main, este archivo.

Este archivo se encarga de correr el UseCase, lllamando su función execute
"""