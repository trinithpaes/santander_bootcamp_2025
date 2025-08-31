from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.responses import JSONResponse
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy import Column, Integer, String, create_engine, Date
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from typing import Optional

DATABASE_URL = "sqlite:///./atletas.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MODELS
class AtletaModel(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    centro_treinamento = Column(String)
    categoria = Column(String)

# SCHEMAS
class AtletaBase(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str
    categoria: str

class AtletaResumo(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

    model_config = {
        "from_attributes": True
    }

class AtletaCreate(AtletaBase):
    pass

class AtletaOut(AtletaBase):
    id: int

    model_config = {
        "from_attributes": True
    }

# DB DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# APP SETUP
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/atleta", response_model=AtletaOut)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo_atleta = AtletaModel(**atleta.dict())
    db.add(novo_atleta)
    try:
        db.commit()
        db.refresh(novo_atleta)
        return novo_atleta
    except IntegrityError:
        db.rollback()
        return JSONResponse(
            status_code=303,
            content={"message": f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"}
        )

@app.get("/atleta", response_model=Page[AtletaResumo])
def listar_atletas(
    nome: Optional[str] = Query(None),
    cpf: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(AtletaModel)

    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)

    atletas = query.all()
    return paginate([AtletaResumo.from_orm(atleta) for atleta in atletas])

add_pagination(app)
