import requests

user_message = "Tell me the conversion rate of INR to USD for 100000"

request_message = {"message": user_message}

# Using the correct UUID (f0b8ff40-...) and the Production URL (/webhook/)
url = "https://escalator-conducive-valuables.ngrok-free.dev/webhook/f0b8ff40-f872-4c8f-9a68-7564b6ac342c

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json())