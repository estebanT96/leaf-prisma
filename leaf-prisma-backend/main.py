from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "LeafPrisma Backend is Live!"}