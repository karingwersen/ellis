from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Pega a URL do banco de dados da variável de ambiente 'DATABASE_URL'.
# Se não estiver definida, usa um arquivo SQLite na raiz do projeto como padrão.
# Isso torna a aplicação flexível para rodar localmente ou em um contêiner.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./escola.db")

# O argumento 'check_same_thread' é necessário apenas para SQLite.
# Esta lógica condicional permite usar outros bancos de dados (como PostgreSQL)
# sem causar erros, bastando mudar a DATABASE_URL.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
