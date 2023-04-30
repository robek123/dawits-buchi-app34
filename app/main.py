import logging
import uvicorn

from fastapi import FastAPI
from app.api import api_routerrom app.core.config import get_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=get_settings().project_name)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app='app.main:app', host=get_settings().host,
                port=get_settings().port, reload=get_settings().reload)
