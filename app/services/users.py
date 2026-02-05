from sqlalchemy.orm import Session

from ..models import User

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