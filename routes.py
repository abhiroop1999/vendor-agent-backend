from fastapi import APIRouter
from models import VendorRequest
from utils.vendor_agent import discover_and_score_vendors

router = APIRouter()

@app.post("/vendor-agent")
def vendor_agent_endpoint(request: VendorAgentRequest):
    return discover_and_score_vendors(request.product, request.quantity, request.location)
