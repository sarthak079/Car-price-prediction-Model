from pydantic import BaseModel,Field
from enum import Enum


class FuelType(str,Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"
    CNG = "CNG"
class SellerType(str, Enum):
    Dealer = "Dealer"
    Individual = "Individual"
class TransmissionType(str, Enum):
    Manual = "Manual"
    Automatic = "Automatic"

class CarFeatures(BaseModel):
    Car_Name: str=Field(...,examples=["ritz"])
    Year: int=Field(...,examples=[2014])
    Present_Price:float=Field(...,examples=[5.59])
    Kms_Driven:int=Field(...,examples=[27000])
    Fuel_Type:FuelType
    Seller_Type:SellerType
    Transmission:TransmissionType
    Owner: int=Field(...,ge=0,le=3,examples=[0],description="Number of previous owners, should be between 0 and 3")

class PredictionResponse(BaseModel):
    prediction_price: float=Field(...,examples=[3.5])