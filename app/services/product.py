from sqlalchemy.orm import Session

from ..db import LocalSession
from ..models import ProductModel


class Product:

    @staticmethod
    def show_product():

        db = LocalSession()
        products = db.query(ProductModel).all()

        for product in products:
            print(
        f"""
        id :{product.id}
        name : {product.name},
        price: {product.price},
        quantity:{product.quantity}
        """
        )
        