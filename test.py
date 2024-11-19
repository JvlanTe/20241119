import requests
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API")

# print(api_key)

city = input("調べたい都市を入力してください：")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ja&units=metric"

response = requests.get(url)
# print(response)

if response.status_code == 200:
    weather_data = response.json()
    print(f"天気：{weather_data['weather'][0]['main']}")
    print(f"概要：{weather_data['weather'][0]['description']}")
    print(f"気温：{weather_data['main']['temp']}℃")
else:
    print(f"データを取得できませんでした。{response.text}")
