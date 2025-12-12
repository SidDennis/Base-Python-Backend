from motor.motor_asyncio import AsyncIOMotorClient

URI = "" 
DATABASE = ""
COLLECTION = ""

client = AsyncIOMotorClient(URI)
db = client[DATABASE]
user_collection = db[COLLECTION]
