import requests


api_key =  "993f3fb8e23b93b84610f0a1"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    conversion_rate = data["conversion_rates"]["BGN"]
    value = float(input("Please enter the currency amount: "))
    bul_leva = value * conversion_rate
    current_data = data["time_last_update_utc"]
    print(f"Last update: {current_data}")
    print(f"{value:.3f} EUR are equal to {bul_leva:.3f} BGN.")

else:
    print("Error connecting to the web service...")
