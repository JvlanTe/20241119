from flask import Flask, render_template, request, flash, redirect
from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("API")

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/", methods=["POST", "GET"])
def index():
    # GETリクエストが発生する際にweather_dataが未定義になるのを防ぐため空の状態にする(?)
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]  # 実際に入力された都市名 form['city']
        if not city:
            flash("都市名を追加してください。", "error")
            return redirect("/")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ja&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            flash("天気データを取得しました！", "success")
            weather_data = response.json()
        else:
            flash("天気の情報を取得できませんでした。正しい都市名を入力してください。", "error")
            return redirect("/")
    return render_template("index.html", weather_data=weather_data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
