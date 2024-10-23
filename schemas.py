# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProductBase(BaseModel):
    code: str
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class TransactionDetailBase(BaseModel):
    prd_id: int
    prd_code: str
    prd_name: str
    prd_price: float
    tax_cd: Optional[str] = None

class TransactionDetailCreate(TransactionDetailBase):
    quantity: int

class TransactionDetail(TransactionDetailBase):
    trd_id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    datetime: datetime
    emp_cd: str
    store_cd: str
    pos_no: str
    total_amt: float
    ttl_amt_ex_tax: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    trd_id: int
    details: List[TransactionDetail] = []

    class Config:
        orm_mode = True

class TaxMasterBase(BaseModel):
    tax_cd: str
    tax_rate: float

class TaxMasterCreate(TaxMasterBase):
    pass

class TaxMaster(TaxMasterBase):
    id: int

    class Config:
        orm_mode = True
