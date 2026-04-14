# Import required libraries
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from pydantic import BaseModel,EmailStr
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass


# Database model
class Users(Base):
    __tablename__ = "users"
    email = Column(String, index=True,primary_key=True, unique=True)
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
    email:EmailStr
    password: str 

# Pydantic model for response data
class UserResponse(BaseModel):
    email: EmailStr


#Api  end point to create a user  (registering a user)
@app.post("/users/", response_model=UserResponse)
async def create_user(item: UserCreate, db: Session = Depends(get_db)):
    if len(item.password.encode("utf-8")) > 72:
        raise HTTPException(status_code=400, detail="Password too long")
    hashed_password=pwd_context.hash(item.password)
    
    existing = db.query(Users).filter(Users.email == item.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    db_item = Users(email=item.email, password=hashed_password)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item

#checking the entered email and password
@app.post("/login/")
async def login(item: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == item.email).first()

    if not db_user or not pwd_context.verify(item.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login Successful"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
