from pydantic import BaseModel


class GetUserModel(BaseModel):
    name: str


class SetUserModel(BaseModel):
    name: str
    id: int


class DeleteUserModel(BaseModel):
    id: int
