import requests


api_key =  "993f3fb8e23b93b84610f0a1"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("*** EUR/Currency Converter ***")
    print("BGN")
    print("USD")
    print("GBP")
    print("JPY")
    print("CAD")
    currency = input("Enter a currency from the list above: ").upper()
    while True:
        if currency == "BGN" or currency == "USD" or currency == "GBP" or currency == "JPY" or currency == "CAD":
            break
        else:
            print("The currency is invalid!!")
            currency=input("Enter a currency from the list above: ").upper()

    amount = float(input("Enter the currency amount: "))

    conversion_rate = data["conversion_rates"][f"{currency}"]
    converted_amount = amount * conversion_rate
    current_data = data["time_last_update_utc"]

    print(f"Last update: {current_data}")
    print(f"{amount:.3f} EUR are equal to {converted_amount:.3f} {currency}.")

else:
    print("Error connecting to the web service...")
