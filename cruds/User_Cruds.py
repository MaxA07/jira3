from pydantic import BaseModel


class GetUserModel(BaseModel):
    name: str
    position: str
    email: str
    phone_number: str


class SetUserModel(BaseModel):
    name: str
    id: str


class DeleteUserModel(BaseModel):
    id: str
