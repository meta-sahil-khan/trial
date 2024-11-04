# service_a.py

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

# Dummy database
users_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 24},
    3: {"name": "Charlie", "age": 29},
}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    if user_id in users_db:
        return {"id": user_id, **users_db[user_id]}
    return {"error": "User not found"}, 404

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
