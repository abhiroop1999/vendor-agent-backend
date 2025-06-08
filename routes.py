from fastapi import APIRouter
from models import VendorRequest
from utils.vendor_agent import discover_and_score_vendors

router = APIRouter()

@router.post("/vendor-agent")
def vendor_agent_endpoint(request: VendorRequest):
    return discover_and_score_vendors(request.product, request.quantity, request.location)