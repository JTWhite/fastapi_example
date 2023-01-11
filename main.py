from fastapi import FastAPI, Path
from views import home
from api import weather_api


api = FastAPI()


def configure():
    api.include_router(home.router, include_in_schema=False)
    api.include_router(weather_api.router)


configure()
