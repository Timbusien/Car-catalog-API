from fastapi import FastAPI
from post_car.post_car_api import car_router
from database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')
app.include_router(car_router)



