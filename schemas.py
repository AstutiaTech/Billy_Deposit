from pydantic import BaseModel, EmailStr
from  datetime import datetime
from typing import Optional

class CreateDeposit(BaseModel):
    customer_id: int
    branch_id: int
    account_id: int
    channel_id: int
    tenure: int
    amount: float
    yield_amount: float
    rate: float
    maturity_date: str

    class Config:
        orm_mode = True
    
class LiquidateDeposit(BaseModel):
    id: int

    class Config:
        orm_mode = True

class RateModel(BaseModel):
    amount: float
    tenure: int

    class Config:
        orm_mode = True