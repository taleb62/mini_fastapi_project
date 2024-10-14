
from ..hashing import Hassh
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def create(request:schemas.User,db:Session):
  hashedpassword = Hassh.bcrypt(request.password)
  new_user = models.User(name = request.name , email = request.email , password = hashedpassword)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user 


def get_user(id:int,db:Session):
  user = db.query(models.User).filter(models.User.id==id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"user with the id {id} is not available ")
    # response.status_code=status.HTTP_404_NOT_FOUND
    # return {"detail":f"blog ith the id {id} is not available "}

  return user