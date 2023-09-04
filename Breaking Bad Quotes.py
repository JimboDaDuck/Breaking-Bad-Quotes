import requests

response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")

if response.status_code == 200:
    data = response.json()
    for item in data:
        print('"' + item["quote"] + '" ' + '- ' + item["author"])
else:
    print(f"Failed to retrieve quote. Status code: {response.status_code}")

input("Enter Anything To Exit: ")
