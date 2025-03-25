import base64
import os

class ProductDTO:
    def __init__(self, name, default_code, list_price, standard_price, category_id, image_path):
        self.name = name
        self.default_code = default_code
        self.list_price = list_price
        self.standard_price = standard_price
        self.category_id = category_id
        self.image_1920 = self._encode_image(image_path) if image_path else None

    def _encode_image(self, image_path):
        """Convert image file to Base64"""
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        return None

    def to_dict(self):
        product_data = {
            'name': self.name,
            'default_code': self.default_code,
            'list_price': self.list_price,
            'standard_price': self.standard_price,
            'categ_id': self.category_id,
            'type': 'product'
        }
        if self.image_1920:
            product_data['image_1920'] = self.image_1920
        return product_data
