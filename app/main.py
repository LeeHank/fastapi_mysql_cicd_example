from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .sqlalchemy_models import IqmApiLog
import uvicorn
Base.metadata.create_all(engine)  # 把 BASE 這個 class 底下的所有子類，都去建立 mapping

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/iqm_log/")
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(IqmApiLog).limit(limit).all()
    return logs

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)