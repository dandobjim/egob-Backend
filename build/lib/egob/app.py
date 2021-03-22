import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from egob import __version__
from egob.config import settings
from egob.logger import logger
from egob.routes.virtuoso import router as virtuoso_router



app = FastAPI(
    title="Egob",
    docs_url="/api/docs",
    openapi_prefix=settings.ROOT_PATH,
    description="",
    version=__version__,
)

# cors

origins = ["*"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


# routes


@app.get("/api/health", name="Health check", status_code=status.HTTP_200_OK, tags=["health"])
async def health():
    return Response(status_code=status.HTTP_200_OK)


app.include_router(virtuoso_router, prefix="/api/v2/virtuoso")


def run_server():
    logger.info(f"🚀 Deploying server at http://{settings.API_HOST}:{settings.API_PORT}")
    uvicorn.run(
        app, host=settings.API_HOST, port=settings.API_PORT, root_path=settings.ROOT_PATH, log_level="info",
    )


run_server()
