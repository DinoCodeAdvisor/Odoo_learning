from domain.repository.ProductRepository import ProductRepository

class SyncProductUseCase:
    def __init__(self, source_repo: ProductRepository, target_repo: ProductRepository):
        self.source_repo = source_repo
        self.target_repo = target_repo

    def execute(self):
        products = self.source_repo.find_all()
        for product in products:
            self.target_repo.save(product)

"""
El useCase es una definición de una acción en particular, está definido principalmente por dos metodos...

__init__ | Este siempre se ejecuta cuando una clase de esté useCase es llamada.

execute | Esta función es la función a llamar cuando se quiere usar este useCase.
"""
