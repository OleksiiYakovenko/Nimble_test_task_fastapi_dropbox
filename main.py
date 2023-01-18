from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from app.schemas.schemas import settings
from app.routes.routes import router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router)

#To start application type: python main.py in terminal
#To test it type in browser http://localhost:8000/docs

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
