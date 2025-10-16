from  fastapi import FastAPI,Depends,status,Response,HTTPException
from  .import schemas,models
from  .import engine, sessionlocal
from sqlalchemy.orm import session


app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def Create(request: schemas.Usercreate,db:session=Depends(get_db)):
    new_blog=models.Blog(email=request.email,password=request.password)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
@app.get('/blog')
def all(db: session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs



