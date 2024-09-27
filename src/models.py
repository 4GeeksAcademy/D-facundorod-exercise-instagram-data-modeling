import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    fristname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Posts(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    body_post = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    comment = Column(String, ForeignKey('Comments.comment_id'),nullable=True)
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Posts.post_id'), nullable=False)
    body_comment = Column(String, nullable=False)
    post = relationship(Posts)
    user = relationship(User)

class follower(Base):
    __tablename__ = 'follower'
    folower_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    user_folower_id= Column(Integer, ForeignKey('User.user_id'))
    user = relationship(User)
    folower = relationship(User)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
