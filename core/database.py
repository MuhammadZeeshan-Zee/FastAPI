from motor.motor_asyncio import AsyncIOMotorClient
from core.config import setting
client = AsyncIOMotorClient(setting.DB_URL)
db = client.mydatabase