import requests
import json


url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"


currency_1= "USD"
currency_2= "INR"
amount= "2"
querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"x-rapidapi-key": "5c3f34fb42mshb5de68f15bd30a9p183b80jsn1512de77e1cc",
	"x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]
formatted ="{:,.2f}".format(converted_amount)
print(formatted)