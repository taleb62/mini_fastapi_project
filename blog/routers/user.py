from typing import List
from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,database,models
from sqlalchemy.orm import session
from ..hashing import Hassh
from ..repository import user



router=APIRouter(
  prefix="/user",
  tags=['users']
)
get_db=database.get_db



@router.post('/' , status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser )
def create(request : schemas.User , db : session = Depends(get_db)):
  return user.create(request,db)




@router.get('/{id}',status_code=200 , response_model = schemas.ShowUser)
def get_user(id ,response : Response, db : session = Depends(get_db)):
  return user.get_user(id,db)
