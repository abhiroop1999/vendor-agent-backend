import os
import json
import google.generativeai as genai

def score_vendors_with_ai(vendors, product, quantity, location):
    # --- TEMPORARY DEBUGGING STEP ---
    # The key is hardcoded directly.
    api_key = "AIzaSyCO25tiGgjznyGDreS7qu2CwTCtU0tf_VY"

    try:
        # Configure the generative AI client
        genai.configure(api_key=api_key)
    except Exception as e:
        return {"error": f"Failed to configure Google AI: {str(e)}"}

    # Create the model - UPDATED MODEL NAME
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

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
        # Generate content
        response = model.generate_content(prompt)
        content = response.text.strip()

        # Robust JSON parsing
        start_index = content.find("[")
        end_index = content.rfind("]") + 1
        if start_index == -1 or end_index == 0:
            return {"error": "AI response did not contain a valid JSON array.", "raw_response": content}
        
        json_data = content[start_index:end_index]
        return json.loads(json_data)

    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON from AI response.", "raw_response": content}
    except Exception as e:
        return {"error": f"AI scoring failed: {str(e)}"}

def discover_and_score_vendors(product, quantity, location):
    mock_vendors = [
        {"name": "Supplier A", "location": "China"},
        {"name": "Supplier B", "location": "India"},
        {"name": "Supplier C", "location": "Vietnam"},
    ]
    return score_vendors_with_ai(mock_vendors, product, quantity, location)
