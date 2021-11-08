from pydantic import BaseModel


class GetUserModel(BaseModel):
    name: str


class SetUserModel(BaseModel):
    name: str
    id: str


class DeleteUserModel(BaseModel):
    id: str
