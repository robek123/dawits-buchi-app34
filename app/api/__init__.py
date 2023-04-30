from fastapi import APIRouter

from app.api.endpoints import router as api_router


def include_router(app):
    app.include_router(api_router, prefix='/api', tags=['api'])


def register_routers(app):
    include_router(app)


register_routers(app)
