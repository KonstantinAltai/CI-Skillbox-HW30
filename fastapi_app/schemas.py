from pydantic import BaseModel


class BaseDish(BaseModel):
    title: str
    cooking_time: int
    ingredients: str
    recipe: str

class DishIn(BaseDish):
    ...

class DishOutOne(BaseDish):
    id: int

    class Config:
        orm_mode = True

class DishOut(BaseModel):
    id: int
    title: str
    cooking_time: int
    views: int

    class Config:
        orm_mode = True
