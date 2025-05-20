from fastapi import HTTPException
from sqlmodel import SQLModel, Field,select
from utils.database import Session,engine

import re
import bcrypt




class UserValidator:
    def validate_email(existingemail: str):
     email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

     if not email_regex.match(existingemail):
        raise HTTPException(
            status_code=400,
            detail="Invalid email format. Please provide a valid email."
        )

     return True
    def check_email_exists(existing_user: str):
       from modules.users.user_model import User

        
       with Session(engine) as session:
            existing_user_record = session.query(User).filter_by(email=existing_user).first()

            if existing_user_record:
                
                raise HTTPException(status_code=400, detail="Email is already in use")
    
    def checkall_the_fieldsarefilled(name:str,existingemail:str,hashed_password:str):
        if not name or name.strip() == "":
            raise HTTPException(status_code=400, detail="name cannot be empty")
        
       
        if not existingemail or existingemail.strip() == "":
            raise HTTPException(status_code=400, detail="Email cannot be empty")
        
        if not hashed_password or hashed_password.strip() == "":
            raise HTTPException(status_code=400, detail="Password cannot be empty")
    def password_is_valid(hashed_password:str):
        
      password_regex = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )

      if not password_regex.match(hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character (@$!%*?&)"
        )

      return True
    def email_not_register(useremail:str):
        from modules.users.user_model import User
        with Session(engine) as session:
            emailisthere=session.exec(select(User).where(User.email==useremail)).first()
            if not  emailisthere:
                 raise HTTPException(
            status_code=400,
            detail="Email is not register"
        )
    def verify_password(plain_password: str, hashed_password: str) -> bool:
     return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
     

    
                

        
    