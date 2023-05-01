import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import distinct

from database import *
from query import QuestionPaser, Responser

app = FastAPI()

database = Database('mysql+pymysql://root:20131114@localhost:3306/drug?charset=utf8mb4')
parser = QuestionPaser(database)
responser = Responser(database)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
error_400 = JSONResponse(content={"message": "Bad Request", "code": 400, "time": time.time(), "data": {}},
                         status_code=400)
error_404 = JSONResponse(content={"message": "Not Found", "code": 404, "time": time.time(), "data": {}},
                         status_code=404)
error_500 = JSONResponse(content={"message": "Internal Server Error", "code": 500, "time": time.time(), "data": {}},
                         status_code=500)


@app.get("/")
async def root():
    return {"message": "Hello World", "code": 200, "time": time.time()}


@app.get("/{types}/{ids}/")
async def get_detail(types: str, ids: Union[int, str], limit: int = 10, offset: int = 0):
    if types == 'disease':
        types = disease
        column = disease.disease_id
        column_list = [distinct(disease.disease_id), disease.name]
    elif types == 'drug':
        types = drug
        column = drug.drug_id
        column_list = [distinct(drug.drug_id), drug.name]
    elif types == 'symptom':
        types = symptom
        column = symptom.symptom_id
        column_list = [distinct(symptom.symptom_id), symptom.name]
    else:
        return error_400

    if ids == 'list':
        data = responser.query_list(column_list, limit, offset)
    elif isinstance(ids, int):
        data = responser.query_one(types, column, ids)
        if not data:
            return error_404
        else:
            data = data.json()
    else:
        return error_400
    return {"message": "success", "code": 200, "time": time.time(), "data": data}


@app.get("/query/")
async def query(message: str = None):
    if not message:
        return error_400
    return {"message": message, "code": 200, "time": time.time(), "data": parser.parse(message)}


