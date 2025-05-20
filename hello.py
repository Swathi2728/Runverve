from fastapi import FastAPI

from utils.database import create_db_and_table

from contextlib import asynccontextmanager
from modules.users.user_controller import user_router
from modules.products.product_controller import device_router
from modules.metrics.metric_controller import metric_router
from fastapi.middleware.cors import CORSMiddleware
# from modules.orders.order_controller import order_router



@asynccontextmanager
async def lifespan(app):
    create_db_and_table()
    yield
    

    
      
app=FastAPI(title="Runverve",lifespan=lifespan)
app.include_router(router=user_router)
app.include_router(router=device_router)
app.include_router(router=metric_router)
# app.include_router(router=order_router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


