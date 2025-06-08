import os
import json
from openai import OpenAI

# Don't create the client at module level - create it in the function
def get_openai_client():
    """Get OpenAI client with proper error handling"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    return OpenAI(api_key=api_key)

def score_vendors_with_ai(vendors, product, quantity, location):
    vendor_descriptions = "\n".join([
        f"{vendor['name']} - Based in {vendor['location']}"
        for vendor in vendors
    ])

    prompt = (
        f"You are a procurement assistant. The user wants to buy {quantity} of {product} in {location}.\n"
        f"Here are some supplier options:\n\n{vendor_descriptions}\n\n"
        f"Score each supplier from 0 to 100 based on their suitability for this request. "
        f"Return ONLY a JSON array like:\n"
        f"[{{\"name\": \"Supplier A\", \"score\": 92, \"location\": \"China\"}}, ...]"
    )

    try:
        # Create client here, not at module level
        client = get_openai_client()
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()

        # Try to parse JSON safely
        start_index = content.find("[")
        end_index = content.rfind("]") + 1
        json_data = content[start_index:end_index]

        return json.loads(json_data)
    except Exception as e:
        return [{"error": f"AI scoring failed: {str(e)}"}]

def discover_and_score_vendors(product, quantity, location):
    mock_vendors = [
        {"name": "Supplier A", "location": "China"},
        {"name": "Supplier B", "location": "India"},
        {"name": "Supplier C", "location": "Vietnam"},
    ]
    return score_vendors_with_ai(mock_vendors, product, quantity, location)
