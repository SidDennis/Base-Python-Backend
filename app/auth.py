import bcrypt
from jose import jwt
from datetime import datetime, timedelta


TOKEN_EXPIRE_TIME = 10 

def hash_password(unhashed_password: str) -> bytes:
  salt = bcrypt.gensalt()
  password_bytes = unhashed_password.encode('utf-8')
  return bcrypt.hashpw(password_bytes, salt)

def verify_password(unhashed_password: str, hashed_password: bytes) -> bool:
  password_bytes = unhashed_password.encode('utf-8')
  return bcrypt.checkpw(password_bytes, hashed_password)


SECRET_KEY = "secretKey"

def create_token(data: dict):
  payload = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_TIME)
  payload.update({"exp": expire})
  token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
  return token

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

