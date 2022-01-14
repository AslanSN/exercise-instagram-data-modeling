import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nick = Column(String(50), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    surname= Column(String(250))
    email = Column(String(250), nullable=False, unique=True)
    
    follower = relationship("Follower")
    comment = relationship("Comment")
    post = relationship("Post")
    like = relationship("Like")
    chat = relationship("Chat")
    
class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    
    user = relationship(User)

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(10))
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))
    
class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

class Like(Base):
    __tablename__ = 'Like'
    id = Column(Integer, primary_key=True, autoincrement=True)
    postLiked_id = Column(Integer, ForeignKey('Post.id'))
    likedBy_id = Column(Integer, ForeignKey('User.id'))

class Chat(Base):
    __tablename__ = 'Chat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String)
    from_id = Column(Integer, ForeignKey('User.id'))
    to_id = Column(Integer, ForeignKey('User.id'))
    
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e