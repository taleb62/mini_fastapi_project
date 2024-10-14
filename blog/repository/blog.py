from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db:Session ):
  
  blogs = db.query(models.Blog).all()
  return blogs

def create(request:schemas.Blog,db:Session):
  new_blog = models.Blog(title = request.title , body = request.body,user_id=1)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

def delete(id:int,db:Session):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # Vérifier si le blog existe
  if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
  db.delete(blog)

  db.commit()
  return {'Done'}

def update(id:int ,request:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # Vérifier si le blog existe
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    # Mettre à jour le blog avec les nouvelles valeurs
    blog.title = request.title
    blog.body = request.bo
    # Ajouter d'autres champs à mettre à jour si nécessaire

    # Enregistrer les modifications dans la base de données
    db.commit()
    db.refresh(blog)

    return {"detail": "Blog updated successfully", "blog": blog}
  
  
def show(id:int,db:Session):
  blog = db.query(models.Blog).filter(models.Blog.id==id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"blog ith the id {id} is not available ")
    # response.status_code=status.HTTP_404_NOT_FOUND
    # return {"detail":f"blog ith the id {id} is not available "}

  return blog