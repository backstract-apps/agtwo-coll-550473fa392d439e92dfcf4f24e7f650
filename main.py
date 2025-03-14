from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - string-coll-550473fa392d439e92dfcf4f24e7f650',debug=False,docs_url='/gifted-hugle-46699906a02e11ef9a427618e95f26ea15/docs',openapi_url='/gifted-hugle-46699906a02e11ef9a427618e95f26ea15/openapi.json')

app.include_router(router, prefix='/gifted-hugle-46699906a02e11ef9a427618e95f26ea15/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()