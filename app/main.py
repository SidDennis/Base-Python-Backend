from fastapi import Fastapi, HTTPException
from models import UserBasic
from database import user_collection

app = Fastapi()

@app.get("/")
def root():
  return {"Hello" : "World"}

@app.post("/register")
def root(user : UserBasic):
  existing_user = await user_collection.find_one({"username" : user.username})
  if existing_user:
    raise HTTPException(status_code=400, detail="Username already in use")

  await user_collection.insert_one({"username": user.username, "password": user.password}) 
  return {"username": user.username}

@app.post("/login")
def root(user : UserBasic):
  existing_user = await user_collection.find_one({"username" : user.username})
  if not existing_user:
    raise HTTPException(status_code=400, detail="User doesn't exist")
  
  if existing_user["password"] != user.password:
    raise HTTPException(status_code=400, detail="Password incorrect")
  
  return {"username": user.username}

