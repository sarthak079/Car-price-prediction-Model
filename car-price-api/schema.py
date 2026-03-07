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
    Car_name: str=Field(...,examples=["ritz"])
    Year: str=Field(...,examples=["2014"])
    Present_price:float=Field(...,examples=[5.59])
    Kms_Driven:int=Field(...,examples=[27000])
    Fuel_Type:FuelType
    Seller_Type:Seller_Type
    Transmission:TransmissionType
    Owner: int=Field(...,ge=0,le=3,examples=[0],description="Number of previous owners, should be between 0 and 3")

class PredictionResponse(BaseModel):
    prediction_price: float=Field(...,examples=[3.5])