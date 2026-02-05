from .services import UserServices
from .db import LocalSession
from .db import create_db

class Cli:

    create_db()

    while True:
        Menu = """
        1.Register,
        2.Login
        """

        print(Menu)

        choice = input('> ')
        if choice == '1':
            username = input('username: ')
            password = input('password: ')
            first_name = input('first_name: ')
            last_name = input('last_name: ')

            UserServices.user_register(LocalSession(),username,password,first_name,last_name)

        elif choice == '2':
            username = input('username: ')
            password = input('password: ')
            UserServices.user_login(LocalSession(),username,password)