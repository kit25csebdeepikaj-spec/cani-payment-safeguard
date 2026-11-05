import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
BASE_URL = os.getenv("PAYPAL_API_BASE")

def get_access_token():
    url = f"{BASE_URL}/v1/oauth2/token"
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}
    
    response = requests.post(url, auth=(CLIENT_ID, CLIENT_SECRET), headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to get PayPal token: {response.text}")

def create_sandbox_order(amount_usd: str):
    token = get_access_token()
    url = f"{BASE_URL}/v2/checkout/orders"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": amount_usd
            }
        }]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        order_data = response.json()
        return {
            "status": "success",
            "order_id": order_data.get("id"),
            "links": order_data.get("links")
        }
    else:
        return {"status": "error", "message": response.text}