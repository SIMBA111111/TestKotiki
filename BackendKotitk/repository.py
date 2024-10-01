from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from models import BreedsModel, CatsModel
from schemas import SCreateCat, SAllBreeds, SUpdateCat


async def get_all_breeds(db: AsyncSession):
    result = await db.execute(select(BreedsModel))
    return result.all()


async def get_all_cats(db: AsyncSession):
    result = await db.execute(
        select(CatsModel, BreedsModel.name, BreedsModel.id)
        .join(BreedsModel)
    )
    return result.all()


async def filter_cats(db: AsyncSession, breed: str):
    result = await db.execute(
        select(CatsModel, BreedsModel.name, BreedsModel.id)
        .join(BreedsModel)
        .filter(BreedsModel.name.ilike(f'%{breed}%'))
    )
    return result.all()


async def get_cat_by_id(db: AsyncSession, cat_id: int):
    result = await db.execute(
        select(CatsModel, BreedsModel.name, BreedsModel.id)
        .join(BreedsModel)
        .filter(CatsModel.id == cat_id)
    )
    return result.first()


async def create_cat(db: AsyncSession, cat_data: SCreateCat):
    obj = CatsModel(
        color=cat_data.color,
        age=cat_data.age,
        description=cat_data.description,
        breed_id=cat_data.breed.id
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)


async def delete_cat(db: AsyncSession, cat_id: int):
    result = await db.execute(select(CatsModel).filter(CatsModel.id == cat_id))
    cat = result.scalars().first()
    await db.delete(cat)
    await db.commit()


async def update_cat(db: AsyncSession, cat_id: int, cat_data: SUpdateCat):
    result = await db.execute(select(CatsModel).filter(CatsModel.id == cat_id))
    cat = result.scalars().first()

    if cat_data.color:
        cat.color = cat_data.color

    if cat_data.age:
        cat.age = cat_data.age

    if cat_data.description:
        cat.description = cat_data.description

    if cat_data.breed_id:
        cat.breed_id = cat_data.breed_id

    await db.commit()
    await db.refresh(cat)