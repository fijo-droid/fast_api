from pydantic import BaseModel

class Usercreate(BaseModel):
    email: str       
    password: str         

