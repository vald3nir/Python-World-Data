import json

import requests

from routers import response_success, response_failed

# ------------------------------------------------------------------
# APIs
# ------------------------------------------------------------------

API_KEY = "959b7f17fb27b94fcb4eceef61224bca"
CURRENCY_LAYER_API_URL = f"http://api.currencylayer.com/list?access_key={API_KEY}"

REST_COUNTRIES_API_URL = "https://restcountries.eu/rest/v2/currency"


# ------------------------------------------------------------------
# Use cases
# ------------------------------------------------------------------


def list_country_money_code():
    try:

        response = requests.get(CURRENCY_LAYER_API_URL)
        money_list_json = json.loads(response.text)

        return response_success(money_list_json["currencies"])

    except Exception:
        return response_failed({"error": CURRENCY_LAYER_API_URL})


def get_country_flag_by_money_code(money_code):
    try:

        response = requests.get(f"{REST_COUNTRIES_API_URL}/{money_code}")
        country_json = json.loads(response.text)

        flag_data = (money_code, country_json[0]["flag"])
        return response_success({"url": flag_data[1]})

    except Exception:
        return response_failed({"error": money_code})
