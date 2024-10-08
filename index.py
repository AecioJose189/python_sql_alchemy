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
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
#Livros
class Livro(Base):
    __tablename__="livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qnt_paginas = Column("qnt_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))
    def __init__(self, titulo, qnt_paginas, dono):
        self.titulo = titulo
        self.qnt_paginas = qnt_paginas
        self.dono = dono
Base.metadata.create_all(bind=db)

#O FAMOSO CRUD, CREATE, READ, UPDATE, DELETE
#CREATE
usuario = Usuario(nome="Aécio",email="aeciojunior45@gmail.com",senha="123123")
session.add(usuario)
session.commit()

#READ
# lista_usuarios = session.query(Usuario).all()
usuario_lira = session.query(Usuario).filter_by(email="aeciojunior45@gmail.com").first()
print(usuario_lira.nome)

livro = Livro(titulo="teste", qnt_paginas="200", dono="junior")
session.add(livro)
session.commit()