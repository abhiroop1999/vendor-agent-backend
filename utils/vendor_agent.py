import os
import re
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def score_and_message(vendor, product, quantity, location):
    prompt = f"""Rate the following vendor for a procurement manager looking to buy {quantity} units of {product} delivered to {location}. 
Vendor info: {vendor}.
Respond only with a score out of 100 and a one-line reasoning."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        raw = response.choices[0].message.content.strip()
        return parse_vendor_response(raw)
    except Exception as e:
        return {"error": f"OpenAI error: {e}"}


def parse_vendor_response(text):
    """Parses a string like '87 - Good delivery reputation' into structured fields."""
    match = re.match(r"(\d+)\s*[-:]?\s*(.*)", text)
    if match:
        score = int(match.group(1))
        explanation = match.group(2).strip()
        return {"score": score, "reason": explanation}
    return {"error": f"Could not parse response: {text}"}
