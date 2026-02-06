from sqlalchemy.orm import Session

from ..models import User,Order
from .product import Product

class OrderService:

    @staticmethod
    def show_order(user:User):
        for order in user.orders:
            print(f"""
                "id": {order.id}, 
                "user_id":{order.user_id}, 
                price:{order.total_price},
                product_id:{order.product_id}
            """)

            return
        print('Order not found!')


    