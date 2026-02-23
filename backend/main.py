from fastapi import FastAPI,Depends
from models import Product,ProductDTO,ProfessorDTO,ResponseDTO,ProfessorResponseDTO,DeptReq,ProfessorFoundBy
from typing import List
from database_config import session,db_engine
import database_models
from sqlalchemy.orm import Session 
from dbHelper import help_db

app = FastAPI()

database_models.Base.metadata.create_all(bind = db_engine)

# database_models.Base.metadata.create_all(bind = db_engine)

@app.get('/')
def greet():
    return "Welcome Telusko"


products = [
    Product(id=1,name='Ball',price=5,qty=10),
    Product(id=2,name='Car',price=23,qty=12),
    Product(id=3,name='Bike',price=44,qty=2),
    Product(id=-1,name='Bat',price=2,qty=1),
    Product(id=8,name='Spects',price=6,qty=3)
]

summary_products : List[ProductDTO] = [ProductDTO(name=user.name,price=user.price,qty=user.qty) for user in products]


@app.get('/prod')
def get_all_products():
    return products

@app.get('/summary_prod')
def get_all_prod_revised():
    return summary_products

@app.post('/addProd')
def add_prod(prod : Product):
    productAdd = Product(id=prod.id,name=prod.name,price=prod.price,qty=prod.qty)
    products.append(productAdd)
    return prod


@app.get("/fetchProd")
def fetchProd():
    db = session()
    return products

def operdb():
    db =session()
    try:
        yield db
    finally:
        db.close()


@app.get('/fetchAll')
def fetchDataFromDB(db : Session = Depends(operdb)):
    products = db.query(database_models.Product).all()
    return products

@app.get("/fetchById/{id}")
def fetchById(id,db:Session = Depends(operdb)):
    productById = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if(productById is None):
        return "No Object"
    return productById


@app.post('/addProduct')
def addProd(product : ProductDTO,db :Session =Depends(operdb)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.get('/fetchDataOfProfAll')
def fetchProfessorAll(db : Session = Depends(help_db)):
    try:
        professor_data = db.query(database_models.Professor).all()

        profRes = [ ProfessorResponseDTO.model_validate(prof) for prof in professor_data]


        result = ResponseDTO(statusCode=200,message="Success",resObj=profRes)
        return result
    except Exception as e:
        result = ResponseDTO(statusCode=404,message='Error Occured',resObj=e)
        return result


@app.post('/addProfessor')
def addProfessor(professor : ProfessorDTO,db : Session = Depends(help_db)):
    try:
        db.add(database_models.Professor(**professor.model_dump()))
        db.commit()
        dto = ResponseDTO(statusCode=200,message="Added successfully",resObj=[])
        return dto
    except Exception as e:
        dto = ResponseDTO(statusCode=404,message='Error',resObj=e)
        return dto


@app.post("/fetchByDept")
def fetchProfessorByDept(dept : DeptReq,db : Session = Depends(help_db)):
    professor_Data = db.query(database_models.Professor).filter(dept.dept == database_models.Professor.qual).all()
    prof_datas = [ProfessorFoundBy(id = prof.id,name = prof.name,dept = prof.qual) for prof in professor_Data]
    try:
        result = ResponseDTO(statusCode=200,message='Success',resObj=prof_datas)
        return result
    except Exception as e:
        return ResponseDTO(statusCode=404,message="Error",resObj=str(e))






