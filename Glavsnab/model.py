from dataclasses import dataclass

@dataclass
class Product:
    product_key: int
    name: str
    link: str
    price: str