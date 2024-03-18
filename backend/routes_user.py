from fastapi import  APIRouter, FastAPI, Depends, HTTPException, status, Response

from  database import engine,SessionLocal, Base
from schema import UserSchema
from sqlalchemy.orm import Session
from models import User


Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/users")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()




@router.post("/add")
async def add_usuario(request:UserSchema, db: Session = Depends(get_db)):
    usuario_on_db = User(id=request.id, username=request.username, password=request.password)
    db.add(usuario_on_db)
    db.commit()
    db.refresh(usuario_on_db)
    return usuario_on_db

@router.get("/{user_name}", description="Listar nome do usuario")
def get_usuario(user_name,db: Session = Depends(get_db)):
    usuario_on_db = db.query(User).filter(User.item == user_name).first()
    return usuario_on_db

@router.get("/listar", description="Listar todos os usuarios")
def get_usuario_all(db: Session = Depends(get_db)):
    usuario = db.query(User).a
    return usuario

@router.delete("/{id}", description="Deletar o usuario pelo id")
def delete_usuario(id: int, db: Session = Depends(get_db)):
    usuario_on_db = db.query(User).filter(User.id == id).first()
    if usuario_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Nao existe usuario com esse id')
    db.delete(usuario_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)

# @app.put("/produto/{id}",response_model=Produtos)
# async def update_produto(request:ProdutosSchema, id: int, db: Session = Depends(get_db)):
#     produto_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     print(produto_on_db)
#     if produto_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
#     produto_on_db = Produtos(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(produto_on_db)
#     db.commit()
#     db.refresh(produto_on_db)
#     return produto_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()