from pydantic import BaseModel


class CreateStatusModel(BaseModel):
    name: str


class UpdateStatusModel(BaseModel):
    name: str
    id: str

