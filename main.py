from fastapi import FastAPI , Depends
from database import engine
import models
import schemas
from sqlalchemy.orm import Session
from database import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/blogs")
def create_blog(request: schemas.Blog , db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title , body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blogs/list")
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blogs/{id}")
def get_blog(id: int , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog


@app.put("/blogs/{id}")
def update_blog(id: int , request: schemas.Blog , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    blog.update(request)
    db.commit()
    return "updated1"
