import requests
import time
from twilio.rest import Client  # You need to install the twilio package for SMS alerts

# Replace these with your API endpoints and API keys
oil_api_url = 'https://api.example.com/oil'
gas_api_url = 'https://api.example.com/gas'
twilio_account_sid = 'your_twilio_account_sid'
twilio_auth_token = 'your_twilio_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
your_phone_number = 'your_phone_number'

# Function to get the current price of oil
def get_oil_price():
    response = requests.get(oil_api_url)
    if response.status_code == 200:
        data = response.json()
        return data['price']
    else:
        print(f"Failed to fetch oil price. Status code: {response.status_code}")
        return None

# Function to get the current price of gas
def get_gas_price():
    response = requests.get(gas_api_url)
    if response.status_code == 200:
        data = response.json()
        return data['price']
    else:
        print(f"Failed to fetch gas price. Status code: {response.status_code}")
        return None

# Function to send an SMS alert
def send_alert(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        to=your_phone_number,
        from_=twilio_phone_number,
        body=message
    )

# Main loop to track and compare oil and gas prices
while True:
    oil_price = get_oil_price()
    gas_price = get_gas_price()
    
    if oil_price is not None and gas_price is not None:
        price_difference = gas_price - oil_price
        
        # You can set a threshold for price difference
        threshold = 10  # Adjust this value as needed
        
        if price_difference >= threshold:
            alert_message = f"Gas price has surged! Oil price: ${oil_price}, Gas price: ${gas_price}"
            send_alert(alert_message)
            print(alert_message)
    
    # Sleep for a certain interval before checking again (e.g., every hour)
    time.sleep(3600)  # Sleep for 1 hour
