from sqlmodel import SQLModel, Field
from datetime import date


class Legend(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    category: str
    description: str
    date: date
    province: str
    canton: str
    district: str
    image_url: str