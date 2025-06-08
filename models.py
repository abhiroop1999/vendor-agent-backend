from pydantic import BaseModel

class VendorRequest(BaseModel):
    product: str
    quantity: int
    location: str
