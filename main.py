from fastapi import FastAPI, Request
from scraper import scrape_alibaba
from utils import score_and_message

app = FastAPI()

@app.post("/vendor-agent")
async def run_agent(req: Request):
    body = await req.json()
    product = body.get("product")
    quantity = body.get("quantity")
    location = body.get("location")

    vendors = scrape_alibaba(product)
    results = []

    for vendor in vendors:
        try:
            ai_response = score_and_message(vendor, product, quantity, location)
            results.append({
                "vendor": vendor,
                "ai_response": ai_response
            })
        except Exception as e:
            results.append({
                "vendor": vendor,
                "error": str(e)
            })

    return {"results": results}