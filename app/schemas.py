from pydantic import BaseModel

class Recipein(BaseModel):
    id : int
    name : str
    description : str