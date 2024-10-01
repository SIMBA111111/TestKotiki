from starlette.responses import JSONResponse, Response

import services

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, Body
from fastapi import status
from fastapi import APIRouter
from fastapi.responses import UJSONResponse

from schemas import SAllBreeds, SAllCats, SCreateCat, SDeleteCat, SUpdateCat, SFilterData

from dependecies import get_db


router = APIRouter()

@router.get("/all-breeds", response_model=list[SAllBreeds])
async def get_list_breeds(db: AsyncSession = Depends(get_db)):
    all_breeds = await services.get_all_breeds(db)
    return all_breeds


@router.get("/all-cats", response_model=list[SAllCats])
async def get_list_cats(db: AsyncSession = Depends(get_db)):
    all_cats = await services.get_all_cats(db)
    return all_cats


@router.get("/filter-cats", response_model=list[SAllCats])
async def filter_cats(filter_data: str,
                      db: AsyncSession = Depends(get_db)):
    filtered_cats = await services.filter_cats(db, filter_data)
    return filtered_cats


@router.get("/get-cat/{cat_id}", response_model=SAllCats)
async def get_cat(cat_id: int,
                        db: AsyncSession = Depends(get_db)):
    cat = await services.get_cat_by_id(db, cat_id)
    return cat


@router.post("/create-cat")
async def create_cat(cat_data: SCreateCat = Body(...),
                     db: AsyncSession = Depends(get_db),
                     ):
    await services.create_cat(db, cat_data)
    return UJSONResponse(status_code=status.HTTP_201_CREATED, content={"Success": "Cat created successfully"})


@router.patch("/update-cat/{cat_id}")
async def update_cat(cat_id: int,
                     cat_data: SUpdateCat = Body(...),
                     db: AsyncSession = Depends(get_db),):
    updated_cat = await services.update_cat(db, cat_id, cat_data)
    return UJSONResponse(status_code=status.HTTP_200_OK, content=updated_cat)


@router.delete("/delete-cat/{cat_id}")
async def delete_cat(cat_id: int,
                     db: AsyncSession = Depends(get_db),
                     ):
    await services.delete_cat(db, cat_id)
    return UJSONResponse(status_code=status.HTTP_200_OK, content={"Success": "Cat deleted successfully"})