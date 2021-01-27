import requests
import json
from requests.auth import HTTPBasicAuth
data = {
    "amount" : 50000,
    "currency": "INR",
    "receipt" :"dummy_order_id_1"
}
response = requests.post('https://api.razorpay.com/v1/orders',
                        auth=HTTPBasicAuth('rzp_test_9vEgMk4HDRYKQR', 'jUcGgCuR0EbAWCPBpbhu1SyQ'),
                         data=data)
with open("response.py", "w") as temp:
    json.dump(response.json(), temp, indent=4)

