import private
import requests
print(private.secret.open_weather_key)

def main():
    api_key = private.secret.open_weather_key
    url = f"https://api.openweathermap.org/data/2.5/forecast?q=Hualien,tw&APPID=75f99c6e5bf613675e743a9c3ab32009&lang=zh_tw&units=metric"

    response = requests.get(url)
    if response.ok :
        print("下載成功")
        allData = response.json()
        city = allData['city']
        print(city)


if __name__ == "__main__":
    main()