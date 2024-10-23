from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/")
async def index():
    return JSONResponse(content={'Message': 'Success'})


@app.get("/jobs")
async def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)