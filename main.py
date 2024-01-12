from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class User(BaseModel):
    email: str
    password: str

app = FastAPI()

origins = [
    "http://localhost:3000"
];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def create_user(user_credentials: User):
    print(user_credentials)

    return user_credentials