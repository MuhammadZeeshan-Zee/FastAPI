from fastapi import APIRouter
from schemas.user import UserCreate
from services.user_services import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create(user: UserCreate):
    user_id = await create_user(user.dict())
    return {"id": user_id}


@router.get("/")
async def get_all():
    return await get_users()


@router.get("/{id}")
async def get_one(id: str):
    return await get_user(id)


@router.put("/{id}")
async def update(id: str, user: UserCreate):
    return await update_user(id, user.dict())


@router.delete("/{id}")
async def delete(id: str):
    return await delete_user(id)