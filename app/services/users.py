import sys

from sqlalchemy.orm import Session

from ..models import User
from .product import Product
from .order import OrderService

class UserServices:

    @staticmethod
    def user_register(db:Session,username:str,password:str,first_name:str | None = None,last_name:str | None = None,):
        
        user = db.query(User).filter(User.username == username).first()

        if user:
            print("User alredy exists!")
            return
        
        user = User(
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)

        print('User yaratildi!')
        return
    
    @staticmethod
    def user_login(db:Session,username:str,password:str,):
        user = db.query(User).filter(User.username == username.strip(),User.password == password.strip()).first()

        if not user:
            print('User not found!')
            return
        
        print('Siz login qilindizgiz!')


        while True:
            Menu = """
            1.Product list
            2.Order
            3.Logout
            """

            print(Menu)
            choice = input('> ')

            if choice == '1':
                Product.show_product()

            elif choice == '2':
                OrderService.show_order(user)

            elif choice == '3':
                print('Biz bilan ishlaganingizdan xursandman!')
                sys.exit()