from fastapi import FastAPI, Depends, Header, HTTPException
from models import UserBasic
from database import user_collection
from auth import hash_password, verify_password, create_token, decode_token

app = FastAPI()

async def get_user_from_token(authorization: str = Header(...)):
  try:
    scheme, token = authorization.split()
    if scheme.lower() != "bearer":
      raise HTTPException(status_code=401, detail="Invalid auth scheme")
    payload = decode_token(token)
    return payload["username"]
  except Exception:
    raise HTTPException(status_code=401, detail="Invalid or expired token")

@app.get("/")
async def root():
  return {"Hello" : "World"}

@app.post("/register")
async def register(user : UserBasic):
  existing_user = await user_collection.find_one({"username" : user.username})
  if existing_user:
    raise HTTPException(status_code=400, detail="Username already in use")

  hashed_password = hash_password(user.password)

  await user_collection.insert_one({"username": user.username, "password": hashed_password}) 
  token = create_token({"username": user.username})
  return {"access_token": token, "token_type": "bearer"}

@app.post("/login")
async def login(user : UserBasic):
  existing_user = await user_collection.find_one({"username" : user.username})
  if not existing_user:
    raise HTTPException(status_code=400, detail="User doesn't exist")
  
  if not verify_password(user.password, existing_user["password"]):
    raise HTTPException(status_code=400, detail="Password incorrect")
  
  token = create_token({"username": user.username})
  return {"access_token": token, "token_type": "bearer"}

