"""Pydantic schemas for request/response validation"""

from pydantic import BaseModel, Field
from typing import Optional


class ItemBase(BaseModel):
    """Base schema for an item"""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class ItemCreate(ItemBase):
    """Schema for creating an item"""
    pass


class ItemUpdate(BaseModel):
    """Schema for updating an item"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class Item(ItemBase):
    """Complete item schema"""
    id: int
    
    class Config:
        from_attributes = True
