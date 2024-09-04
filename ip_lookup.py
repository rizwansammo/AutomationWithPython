import requests

def ip_geolocation(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()
    if "error" not in data:
        print(f"IP: {data['ip']}\nCity: {data['city']}\nRegion: {data['region']}\nCountry: {data['country_name']}")
    else:
        print("Invalid IP address or API error.")

ip = input("Enter IP address: ")
ip_geolocation(ip)
