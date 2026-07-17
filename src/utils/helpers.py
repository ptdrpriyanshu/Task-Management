from fastapi import Request,HTTPException,status,Depends
from src.utils.settings import settings
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError
from src.user.models import UserModel
from src.utils.db import get_db
from datetime import datetime
import jwt





def is_authenticated(request:Request,db:Session=Depends(get_db)):
     
    try:
       token=request.headers.get("authorization")
       if not token:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
       token =token.  split(" ")[-1]
       data =jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
       user_id = data.get("_id")
       exp_time=data.get("exp")
       current_time =datetime.now().timestamp()
 
       
       user=db.query(UserModel).filter(UserModel.id == user_id).first()
       if not user:
         raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
     #  print(data)

       return user
    except   InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
