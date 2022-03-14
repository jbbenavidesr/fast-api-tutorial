from tkinter.tix import Tree
from typing import Sequence

from pydantic import BaseModel, HttpUrl


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class RecipeCreate(RecipeBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


class RecipeUpdate(RecipeBase):
    label: str


class RecipeIndDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


class Recipe(RecipeIndDBBase):
    pass


class RecipeInDB(RecipeIndDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
