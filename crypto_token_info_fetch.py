import requests
import pandas as pd
import datetime


def get_tokens(threshold, apikey):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?cryptocurrency_type=tokens&aux=platform,volume_7d&start=1&limit=5000"
    headers = {
        "Accepts": "application/json",
        "X-CMC_Pro_API_Key": apikey
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    data_df = pd.DataFrame(data['data'])
    data_df = data_df.dropna(subset=['platform'])
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    data_df.to_csv('token_raw_data_{}.csv'.format(timestamp))

    tokens_dict_list = []
    chain_list = []
    for token in data["data"]:
        if token['platform'] is not None:
            chain_list.append(token['platform']['name'])
        if token["platform"] is None:
            continue
        #if token["platform"]["name"] != "Ethereum":
        #    continue

        vol_7d = token["quote"]['USD']['volume_7d']

        if vol_7d >= threshold:
            tokens_dict_list.append({
                "name": token["name"],
                "symbol": token["symbol"],
                "chain": token['platform']['name'],
                "contract_address": token["platform"]["token_address"],
                "avg_vol_7d": vol_7d
            })

    save_tokens_data(tokens_dict_list)
    pd.DataFrame(chain_list).to_csv("chain_name.csv")


def save_tokens_data(token_list):
    df = pd.DataFrame(token_list)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"tokens_data_{timestamp}.csv"
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    api_key = "your_api_key"
    avg_vol_7d = 2000000  # This is the pre-determined 7-Day averaged daily trading volume threshold variable
    get_tokens(avg_vol_7d, api_key)
