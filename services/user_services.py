from core.database import db
from bson import ObjectId
from fastapi import HTTPException


def is_valid_id(id: str):
    return ObjectId.is_valid(id)


async def create_user(data):
    result = await db.user.insert_one(data)
    return str(result.inserted_id)


async def get_users():
    users = await db.user.find().to_list(length=None)
    for u in users:
        u["id"] = str(u["_id"])
        del u["_id"]
    return users


async def get_user(id: str):
    if not is_valid_id(id):
        raise HTTPException(400, "Invalid ID")

    user = await db.user.find_one({"_id": ObjectId(id)})

    if not user:
        raise HTTPException(404, "User not found")

    user["id"] = str(user["_id"])
    del user["_id"]
    return user


async def update_user(id: str, data):
    if not is_valid_id(id):
        raise HTTPException(400, "Invalid ID")

    result = await db.user.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )

    if result.matched_count == 0:
        raise HTTPException(404, "User not found")

    return {"message": "updated successfully"}


async def delete_user(id: str):
    if not is_valid_id(id):
        raise HTTPException(400, "Invalid ID")

    result = await db.user.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(404, "User not found")

    return {"message": "deleted successfully"}