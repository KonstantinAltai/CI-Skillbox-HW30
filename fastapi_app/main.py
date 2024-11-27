from typing import List

from fastapi import FastAPI
from sqlalchemy.future import select
from sqlalchemy import update

import fastapi_app.models
import fastapi_app.schemas
from fastapi_app.database import engine, session

from fastapi.testclient import TestClient

app = FastAPI(title='Recipes for the soul')
client = TestClient(app)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.post('/recipe', response_model=schemas.DishOut)
async def post_dishs(dish: schemas.DishIn) -> models.Dish:
    new_dish = models.Dish(**dish.dict())
    async with session.begin():
        session.add(new_dish)
    return new_dish


@app.get('/recipes', response_model=List[schemas.DishOut])
async def get_dishs() -> List[models.Dish]:
    res = await session.execute(
        select(models.Dish)
        .order_by(models.Dish.views.desc(), models.Dish.cooking_time)
    )
    return res.scalars().all()


@app.get('/recipes/{num_id}', response_model=schemas.DishOutOne)
async def dish(num_id: int) -> schemas.DishOutOne:
    res = await session.execute(select(models.Dish).where(models.Dish.id == num_id))
    if res:
        await session.execute(
            update(models.Dish)
            .where(models.Dish.id == num_id)
            .values(views = models.Dish.views+1)
        )
        await session.commit()
    return res.scalars().first()
