from ast import excepthandler
from logging import Logger
from fastapi import APIRouter
from fastapi.responses import JSONResponse


github__router = APIRouter(
    prefix="/api/v1/users",
    tags=["v1, users"]
)

@github__router.get(
    path="/all",
)
async def users():
    try:
        return JSONResponse(status_code=200, content={
            'res': 'This api is working guys'
        })
    except:
         return JSONResponse(status_code=403, content={
            'result': 'Error',
            'error': Logger.serialize_error(excepthandler)
        })