from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

# Get DB credentials from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")


@app.get("/")
def read_root():
    try:
        # Try to connect to the database
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            # Run a simple query to get the DB version
            result = connection.execute(text("SELECT version();"))
            db_version = result.fetchone()[0]

        return {
            "status": "Backend is Live!",
            "database": "Connected Successfully!",
            "db_version": db_version.split(",")[0]  # Cleans up the output
        }
    except Exception as e:
        return {
            "status": "Backend is Live!",
            "database": f"Connection Failed: {str(e)}"
        }
    