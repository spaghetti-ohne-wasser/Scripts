import requests

def show_price():
    response: dict = requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json").json()
    dollar: str = response["bpi"]["EUR"]["rate"]
    pfund: str = response["bpi"]["EUR"]["rate"]
    euro: str = response["bpi"]["EUR"]["rate"]
    updated: str = response["time"]["updated"]
    
    print("Bitcoin Price List:\nUnited States Dollar: " + dollar + " $\nBritish Pound Sterling: " + pfund + " £\nEuro: " + euro + " €\nUpdated " + updated)

if __name__ == "__main__":
    show_price()
