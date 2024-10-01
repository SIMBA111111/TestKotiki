import repository

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from schemas import SAllBreeds, SAllCats, SCreateCat, SUpdateCat


async def get_all_breeds(db: AsyncSession):
    try:
        result = await repository.get_all_breeds(db)
    except Exception as e:
        print(f"Error get all breeds from db: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    all_breeds = []
    try:
        for breed in result:
            breed_serialize = SAllBreeds(id=breed[0].id, name=breed[0].name)
            all_breeds.append(breed_serialize)
    except Exception as e:
        print(f"Error serializable all breeds: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    return all_breeds


async def get_all_cats(db: AsyncSession):
    try:
        result = await repository.get_all_cats(db)
    except Exception as e:
        print(f"Error get all cats from db: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    all_cats = []
    try:
        for cat, name, id in result:
            cat_serialize = SAllCats(
                id=cat.id,
                color=cat.color,
                age=cat.age,
                description=cat.description,
                breed=SAllBreeds(
                    id=id,
                    name=name
                )
            )

            all_cats.append(cat_serialize)
    except Exception as e:
        print(f"Error serializable all cats: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    return all_cats


async def filter_cats(db: AsyncSession, breed: str):
    try:
        result = await repository.filter_cats(db, breed)
    except Exception as e:
        print(f"Error get all cats from db: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    all_cats = []
    try:
        for cat, name, id in result:
            cat_serialize = SAllCats(
                id=cat.id,
                color=cat.color,
                age=cat.age,
                description=cat.description,
                breed=SAllBreeds(
                    id=id,
                    name=name
                )
            )

            all_cats.append(cat_serialize)
    except Exception as e:
        print(f"Error serializable all cats: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    return all_cats


async def get_cat_by_id(db: AsyncSession, cat_id: int):
    try:
        result = await repository.get_cat_by_id(db, cat_id)
    except Exception as e:
        print(f"Error get cat by id: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
    if result is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    print(result)
    cat_serialize = SAllCats(
        id=result[0].id,
        color=result[0].color,
        age=result[0].age,
        description=result[0].description,
        breed=SAllBreeds(
            id=result.id,
            name=result.name
        )
    )
    return cat_serialize


async def create_cat(db: AsyncSession, cat_data: SCreateCat):
    try:
        print(cat_data)
        await repository.create_cat(db, cat_data)
    except Exception as e:
        print(f"Error create cat: {e}")
        raise HTTPException(status_code=500, detail="Server Error")


async def delete_cat(db: AsyncSession, cat_id: int):
    try:
        await repository.delete_cat(db, cat_id)
    except Exception as e:
        print(f"Error delete cat: {e}")
        raise HTTPException(status_code=500, detail="Server Error")


async def update_cat(db: AsyncSession, cat_id: int, cat_data: SUpdateCat):
    try:
        await repository.update_cat(db, cat_id, cat_data)
    except Exception as e:
        print(f"Error update cat: {e}")
        raise HTTPException(status_code=500, detail="Server Error")
