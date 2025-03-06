from pydantic import BaseModel
from datetime import date


class LegendCreate(BaseModel):
    name: str
    category: str
    description: str
    date: date
    province: str
    canton: str
    district: str
    image_url: str
