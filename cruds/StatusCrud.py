from pydantic import BaseModel


class GetStatusModel(BaseModel):
    name: str


class SetStatusModel(BaseModel):
    name: str
    id: str


class DeleteStatusModel(BaseModel):
    id: str
