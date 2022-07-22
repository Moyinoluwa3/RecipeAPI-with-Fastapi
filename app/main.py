from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine,get_db
from typing import List
from . import schemas,models,crud



app = FastAPI(title="Recipe APP")
models.Base.metadata.create_all(bind=engine)



@app.get("/all",response_model=List[schemas.Recipein])
def get_all_recipes(db: Session = Depends(get_db)):
    if recipes := crud.get_all_recipes(db=db):
        return recipes
    else:
        return{"message":"recipes not found"}

@app.get("/recipes/{id}")
def get_a_recipe(id:int,db: Session = Depends(get_db)):
    if recipe := crud.get_recipe(db=db,id=id):
        return recipe
    else:
        return{"message":"recipe not found"}

@app.post("/recipes", response_model=schemas.Recipein)
def create_a_recipe(recipe:schemas.Recipein,db: Session = Depends(get_db)):
    recipe = crud.create_recipe(db=db, recipe=recipe)
    return recipe

@app.put("/recipes/{id}", response_model= schemas.Recipein)
def update_recipe(id:int,recipe:schemas.Recipein,db: Session = Depends(get_db)):
    recipe = crud.update_recipe(db=db,id=id,recipe=recipe)
    return recipe

@app.delete("/recipes/{id}")
def delete_recipe(id:int,db: Session = Depends(get_db)):
    recipe= crud.delete_recipe(db=db,id=id)
    message = f"Successfully deleted recipe: '{id}'"
    return {"detail": message}




