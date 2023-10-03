from fastapi import FastAPI
import logging
from app.api.routes import example
from app.core.config import settings


logger = logging.getLogger("debugLogger")

app = FastAPI(
    title="Humai Numbers",
    description="Esta es una aplicación muy genial",
    version="1.0.0",
)

app.include_router(example.router)




@app.on_event("startup")
async def startup_event():
    logger.info("Inicialización de recursos")
    logger.warning(f"Variable de entorno: {settings.MY_ENV_VAR}")
    pass


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Liberación de recursos")
    pass
