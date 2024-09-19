from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db") #cria ou conecta um banco de dados existente
Session = sessionmaker(bind=db) #bind vc informa o nome do seu banco de dados
session = Session() #somente para criação da sessão 

Base = declarative_base()

#As tabelas
#Usuarios
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
#Livros
class Livro(Base):
    id = Column("id", Integer)
    titulo = Column("titulo", String)
    qnt_paginas = Column("qnt_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

Base.metadata.create_all(bind=db)