# Import required libraries
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from pydantic import BaseModel


app = FastAPI()
# Database setup
DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass


# Database model
class Users(Base):
    __tablename__ = "users"
    id= Column(Integer , primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)

#creating all the tables
Base.metadata.create_all(bind=engine)



# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic model for request data
class UserCreate(BaseModel):
    email: str
    password: str

# Pydantic model for response data
class UserResponse(BaseModel):
    id: int
    email: str
    password: str


#Api  end point to create a user
@app.post("/users/", response_model=UserResponse)
async def create_item(item: UserCreate, db: Session = Depends(get_db)):
    db_item = Users(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# API endpoint to read an item by ID
@app.get("/users/{user_id}", response_model=UserResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Users).filter(Users.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


if __name__ == "__main__":
    import uvicorn
