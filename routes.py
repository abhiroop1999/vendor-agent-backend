from fastapi import APIRouter
from models import VendorRequest
from utils.vendor_agent import fetch_and_score_vendors

router = APIRouter()

@router.post("/vendor-agent")
def get_vendors(data: VendorRequest):
    return {"results": fetch_and_score_vendors(data.product, data.quantity, data.location)}
