from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

#タスク作成受け取り用の TaskCreate
class TaskCreate(BaseModel):
    title: str
    description: str

#レスポンス用の TaskResponse
class TaskResponse(TaskCreate):
    id: int
    completed: bool
    owner_id: int

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True