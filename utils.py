import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def score_and_message(vendor, product, quantity, location):
    prompt = f"""
Vendor Info: {vendor}
Product: {product}
Quantity: {quantity}
Delivery Location: {location}

Task:
1. Give a reliability score out of 100 for this vendor based on their product name and price.
2. Generate a professional outreach message to the vendor.

Respond in JSON:
{{"score": ..., "message": "..."}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']