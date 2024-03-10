import uuid

from fastapi_users import schemas       # Для работы БД
from pydantic import BaseModel, Field   # Для работы с изображениями
from typing import Optional             # Для работы с изображениями

# схемы для работы с БД

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


# схема для работы с изображениями

class ImageProcessionOptions(BaseModel):
    resize: Optional[str] = Field(None, description="Convert to 1980x1200")
    flip: Optional[str] = Field(None, description="Convert to horizontal/vertical")
    grayscale: Optional[bool] = Field(None, description="Convert to grayscale")
    convert_to: Optional[str] = Field(None, description="Example: png, jpg, webp")
