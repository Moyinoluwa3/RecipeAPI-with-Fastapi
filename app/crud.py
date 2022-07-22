from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Recipe 

from . import models,schemas

def get_all_recipes(db:Session) -> models.Recipe:
    return (db.query(models.Recipe).all())

def get_recipe(db:Session,id:int) -> models.Recipe:
    return (db.query(models.Recipe).filter(models.Recipe.id == id ).first())

def create_recipe(db:Session, recipe=schemas.Recipein) ->models.Recipe:
    new_recipe = models.Recipe(**recipe.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

def delete_recipe(db:Session, id:int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == id)
    if recipe.first() == None:
        raise HTTPException(status_code=404,detail="Recipe not found")
    recipe.delete(synchronize_session=False)
    db.commit()

def update_recipe(db:Session,id=int,recipe=schemas.Recipein) -> models.Recipe:
    recipe = db.query(models.Recipe).filter(models.Recipe.id == id)
    if recipe.first() == None:
        raise HTTPException(status_code=404,detail="Recipe not found")

    recipe.update(recipe.dict(), synchronize_session=False)
    db.commit()



