from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.routers import auth, books, members
from app.database import get_db
from app.models import Role


app = FastAPI(
    title="Smart Library Management System"
)


# Routers
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(members.router)



@app.get("/")
def home():
    return {
        "message": "Smart Library Management System running"
    }



@app.get("/health")
def health_check(
    db: Session = Depends(get_db)
):

    roles = db.query(Role).all()

    return {
        "status": "UP",
        "database": "connected",
        "roles_count": len(roles)
    }