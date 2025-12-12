from motor.motor_asyncio import AsyncIOMotorClient

URI = "" 
DATABASE = ""
COLLECTION = ""

client = AsyncIOMotorClient(URI)
db = client[DATABASE]
collection = db[COLLECTION]
