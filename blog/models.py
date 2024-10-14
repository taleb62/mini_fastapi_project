from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String(255), nullable=False) 

    body = Column(String(2555), nullable=False) 
    user_id= Column(Integer(),ForeignKey('users.id')) 
    
    creator = relationship("User" , back_populates="blogs") 
    
  
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String(255), nullable=False) 

    email = Column(String(2555), nullable=False)  
    
    password = Column(String(2555), nullable=False) 
    
    
    
    blogs = relationship("Blog" , back_populates="creator") 