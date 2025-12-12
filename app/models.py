from pydantic import BaseModel

class UserBasic(BaseModel):
  username: str
  password: str

