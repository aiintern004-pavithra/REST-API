from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.chat_router import router as chat_router

app = FastAPI(
    title="Institute360 REST API",
    description="Institute360 Chatbot Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")


@app.get("/")
def home():
    return {"message": "Welcome to Institute360 API"}


@app.get("/health")
def health():
    return {"status": "API is running"}