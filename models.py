from pydantic import BaseModel

class VendorRequest(BaseModel):
    product: str
    quantity: str
    location: str
