import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()  # .envファイルを読み込む

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True, index=True)
    barcode = Column(String(13), unique=True, index=True)
    name = Column(String(50))
    price = Column(Float)

Base.metadata.create_all(bind=engine)

class ProductIn(BaseModel):
    barcode: str
    name: str
    price: float

class CheckoutItem(BaseModel):
    barcode: str
    name: str
    price: float

class Checkout(BaseModel):
    cart: list[CheckoutItem]

@app.get("/api/product")
def get_product(barcode: str):
    db = SessionLocal()
    product = db.query(Product).filter(Product.barcode == barcode).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/api/checkout")
def checkout(checkout: Checkout):
    total_excluding_tax = sum(item.price for item in checkout.cart)
    total = total_excluding_tax * 1.1  # 10% tax
    return {"total": total, "totalExcludingTax": total_excluding_tax}

print(f"DATABASE_URL: {DATABASE_URL}")
