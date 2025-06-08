import os
from openai import OpenAI

client = OpenAI()

def score_vendors_with_ai(vendors, product, quantity, location):
    vendor_descriptions = "\n".join([
        f"{vendor['name']} - Based in {vendor['location']}"
        for vendor in vendors
    ])

    prompt = (
        f"You are a procurement assistant. The user wants to buy {quantity} of {product} in {location}.\n"
        f"Here are some supplier options:\n\n{vendor_descriptions}\n\n"
        f"Score each supplier from 0-100 based on their suitability for this request. "
        f"Return a JSON list in this format:\n"
        f"[{{\"name\": \"Supplier A\", \"score\": 90, \"location\": \"China\"}}, ...]"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        ai_response = response.choices[0].message.content.strip()
        return eval(ai_response)
    except Exception as e:
        return [{"error": str(e)}]

def discover_and_score_vendors(product, quantity, location):
    # Mock vendor list - Replace this with actual scraping later
    mock_vendors = [
        {"name": "Supplier A", "location": "China"},
        {"name": "Supplier B", "location": "India"},
        {"name": "Supplier C", "location": "Vietnam"},
    ]
    return score_vendors_with_ai(mock_vendors, product, quantity, location)
