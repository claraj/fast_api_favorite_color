# from typing import List, Union 

from pydantic import BaseModel 


class ColorBase(BaseModel):
    name: str 


class Color(ColorBase):
    id: int 

    class Config:
        orm_mode = True


class ColorCreate(ColorBase):
    pass  # presumably custom create stuff goes here