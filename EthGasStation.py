"""
This script coded by github.com/OmarAEH
Feel free to contact me at anytime.
"""

import json
import requests
import jsonpath


def ethereum_gas_station():
    """
    This function will get Ethereum gas fees from ethgasstation.info in all transaction speeds.
    """
    url = 'https://ethgasstation.info/api/ethgasAPI.json?'  # API url
    respond = requests.get(url)  # Sending the request to the API server
    gas = json.loads(respond.text)  # Converting the request data to JSON
    safe_low = jsonpath.jsonpath(gas, "safeLow")  # Fetching safe low eth gas
    average = jsonpath.jsonpath(gas, "average")   # Fetching average eth gas
    fast = jsonpath.jsonpath(gas, "fast")  # Fetching fast eth gas
    fastest = jsonpath.jsonpath(gas, "fastest")  # Fetching fastest eth gas
    print("Safe low Ethereum gas fees speed : " + str(int(safe_low[0])/10) + " GWEI")
    print("Average Ethereum gas fees speed : " + str(int(average[0])/10) + " GWEI")
    print("Fast Ethereum gas fees speed : " + str(fast[0]/10) + " GWEI")
    print("Fastest Ethereum gas fees speed : " + str(fastest[0]/10) + " GWEI")


if __name__ == "__main__":
    ethereum_gas_station()
