  
def currency_converter(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount 

def main():   
    print("Welcome to Currency Converter")
    print("Available currencies:")
    print("1. USD - United States Dollar")
    print("2. EUR - Euro")
    print("3. GBP - British Pound")
    print("4. JPY - Japanese Yen")
    
    # Exchange rates as of a certain date
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.88,
        'GBP': 0.77,
        'JPY': 109.86
    }
    
    from_currency = input("Enter the currency you are converting from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount you want to convert: "))
    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency. Please try again.")
        return
    
    exchange_rate_from = exchange_rates[from_currency]
    exchange_rate_to = exchange_rates[to_currency]
    
    converted_amount = currency_converter(amount / exchange_rate_from, exchange_rate_to)
    
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
