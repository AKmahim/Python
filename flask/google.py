import requests

def main():
    currency = input("Enter the currency to see the conversion from EUR: ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=fd90d71fe1218510c280d457149ad749",params={"symbols":currency})
    
    if res.status_code != 200:
        raise Exception("ERROR:API request unsuccessful.")
    data = res.json()
    rate = data["rates"][currency]
    # print(data)
    print(f"1 EUR is equal to {rate} {currency}")

if __name__ == "__main__":
    main()




