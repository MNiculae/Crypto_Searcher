import json

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url_token = "https://bravenewcoin.p.rapidapi.com/oauth/token"
payload_token = {
    "audience": "https://api.bravenewcoin.com",
    "client_id": "oCdQoZoI96ERE9HY3sQ7JmbACfBf55RY",
    "grant_type": "client_credentials"
}
headers_token = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
    "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
}

response_token = requests.request("POST", url_token, json=payload_token, headers=headers_token)
access_token = response_token.json()["access_token"]

# print(access_token)



def get_id(symbol):
    url = "https://bravenewcoin.p.rapidapi.com/asset"
    querystring = {"symbol": symbol, "status": "ACTIVE"}

    headers = {
        "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
        "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()["content"]
    id = response[0]['id']
    return id

# print(get_id('ETH'))



# get list of coins from API
def get_coins_from_api():
    url = "https://bravenewcoin.p.rapidapi.com/asset"
    querystring = {"status": "ACTIVE"}
    headers = {
        "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
        "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()["content"]
    return response

# print(get_coins_from_api())



symbol = []
def get_details(assetId=get_id(symbol)):
    url = "https://bravenewcoin.p.rapidapi.com/market-cap"
    querystring = {"assetId": assetId}
    headers = {
        "Authorization": "Bearer " + access_token,
        "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
        "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()['content']
    price = response[0]['price']
    price = round(price, 4)
    return price

# print(get_details('f1ff77b6-3ab4-4719-9ded-2fc7e71cff1f'))



def get_details_coin(cryptocurrency):
    url = "https://bravenewcoin.p.rapidapi.com/market-cap"
    querystring = {"assetId": cryptocurrency}
    headers = {
        "Authorization": "Bearer " + access_token,
        "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
        "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()['content']
    details = response[0]
    return details

# print(get_details_coin('f1ff77b6-3ab4-4719-9ded-2fc7e71cff1f'))



def get_assetid(cryptocurrency):
    url = "https://bravenewcoin.p.rapidapi.com/market-cap"
    querystring = {"assetId": cryptocurrency}
    headers = {
        "Authorization": "Bearer " + access_token,
        "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
        "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()['content']
    assetId = response[0]['assetId']
    return assetId

# print(get_assetid('f1ff77b6-3ab4-4719-9ded-2fc7e71cff1f'))



def get_crypto(assetId):
    url = f"https://bravenewcoin.p.rapidapi.com/asset/{assetId}"
    headers = {
        "X-RapidAPI-Key": "04c3ca47fcmsh165b804ddb5085dp1ba183jsn980a959026bc",
        "X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers).json()
    response = response
    return response

# print(get_crypto('f1ff77b6-3ab4-4719-9ded-2fc7e71cff1f'))



@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/search')
def search():
    coins = get_coins_from_api()
    symbol = ["BTC", "ETH", "LTC", "XRP"]
    price_BTC = get_details(assetId=get_id(symbol[0]))
    price_ETH = get_details(assetId=get_id(symbol[1]))
    price_LTC = get_details(assetId=get_id(symbol[2]))
    price_XRP = get_details(assetId=get_id(symbol[3]))
    return render_template('search.html', coins=coins, price_BTC=price_BTC, price_ETH=price_ETH, price_LTC=price_LTC, price_XRP=price_XRP)


@app.route('/search_results')
def search_results():
    cryptocurrency = request.args.get('cryptocurrency')
    details = get_details_coin(cryptocurrency)
    assetId = get_details_coin(cryptocurrency)['assetId']
    crypto = get_crypto(assetId)
    short_details = [details["timestamp"], details["price"]]
    return render_template('search_results.html', details=details, short_details=short_details, crypto=crypto)


@app.route('/price_data')
def price_data():
    # obtine datele criptomonedei
    data = get_details_coin()
    return data


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()



