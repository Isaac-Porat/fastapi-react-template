import uvicorn 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

# dummy response 
@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon available"}

def start_server():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

