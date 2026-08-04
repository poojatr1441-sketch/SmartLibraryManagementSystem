from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Role


app = FastAPI(
    title="Smart Library Management System"
)


@app.get("/")
def home():
    return {
        "message": "Smart Library Management System running"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):

    roles = db.query(Role).all()

    return {
        "status": "UP",
        "database": "connected",
        "roles_count": len(roles)
    }