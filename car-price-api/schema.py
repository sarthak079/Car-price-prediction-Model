from pydantic import BaseModel,Field
from enum import Enum


class FuelType(str,Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"
    CNG = "CNG"
class Seller_Type(str, Enum):
    Dealer = "Dealer"
    Individual = "Individual"
class TransmissionType(str, Enum):
    Manual = "Manual"
    Automatic = "Automatic"

class CarFeatures(BaseModel):
    Car_name: str = Field(..., alias="Car_Name")
    Year: int = Field(...) # Changed to int to match your JSON data
    Present_price: float = Field(..., alias="Present_Price")
    Kms_driven: int = Field(..., alias="Kms_Driven")
    Fuel_type: str = Field(..., alias="Fuel_Type")
    Seller_type: str = Field(..., alias="Seller_Type")
    Transmission: str = Field(...) 
    Owner: int = Field(...)

class PredictionResponse(BaseModel):
    prediction_price: float=Field(...,examples=[3.5])