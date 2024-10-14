from typing import List
from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,database,models
from sqlalchemy.orm import session
from .. import token
from . import oauth2
from ..repository import blog
router=APIRouter(
prefix="/blog",
tags=['blogs']
)
get_db=database.get_db
@router.get('/', response_model=list[schemas.Blog] )
def get( db : session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):


  return blog.get_all(db)


@router.post('/' , status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog , db : session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
  return blog.create(request,db)

@router.get('/{id}',status_code=200 , response_model = schemas.ShowBlog )
def show(id ,response : Response, db : session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
  return blog.show(id,db)




@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id ,response : Response, db : session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
  # db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
  return blog.delete(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED )
def update_blog(id: int, request: schemas.Blog, db: session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
  return blog.update(id,request,db)
    # Récupérer le blog avec l'ID fourni




