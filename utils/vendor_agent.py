import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_and_score_vendors(product, quantity, location):
    prompt = f"List 3 potential vendors for {product} with quantity {quantity} in or near {location}. Score each vendor out of 100 for reliability."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a vendor recommendation AI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        text = response['choices'][0]['message']['content']
        return parse_vendor_response(text)
    except Exception as e:
        return [{"error": str(e)}]

def parse_vendor_response(text):
    lines = text.strip().split("\n")
    results = []
    for line in lines:
        parts = line.split(" - ")
        if len(parts) >= 3:
            results.append({
                "name": parts[0].strip(),
                "score": int(''.join(filter(str.isdigit, parts[1]))),
                "location": parts[2].strip()
            })
    return results
