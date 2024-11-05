# service_b.py

from fastapi import FastAPI, HTTPException
import httpx
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
SERVICE_A_URL = os.getenv("SERVICE_A_URL")

@app.get("/process-user/{user_id}")
async def process_user(user_id: int):
    async with httpx.AsyncClient() as client:
        print(f"this is service url  - {SERVICE_A_URL}")
        response = await client.get(f"{SERVICE_A_URL}/{user_id}")

        if response.status_code == 200:
            user_data = response.json()
            # Process user data (dummy example)
            processed_data = {
                "user_id": user_data["id"],
                "name": user_data["name"].upper(),  # Process: Make name uppercase
                "age_next_year": user_data["age"] + 1  # Process: Age in the next year
            }
            return processed_data
        else:
            raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
