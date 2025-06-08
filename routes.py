from fastapi import APIRouter
from models import VendorRequest

router = APIRouter()

@router.post("/vendors")
def get_vendors(data: VendorRequest):
    vendors = [
        {"name": "Supplier A", "score": 92, "location": "China"},
        {"name": "Supplier B", "score": 85, "location": "India"},
        {"name": "Supplier C", "score": 78, "location": "Vietnam"},
    ]
    return {"results": vendors}
