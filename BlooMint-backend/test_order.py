import requests

url = "http://127.0.0.1:5000/add_order"
data = {
    "name": "Faith",
    "email": "faith@example.com",
    "product": "Custom Period Pack",
    "quantity": 1,
    "custom_pack": "Pads, Soap, Panty, Towel"
}

response = requests.post(url, json=data)
print(response.json())