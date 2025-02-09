from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "50632ce2faaa6f5f6c9d67dcee8db9c3"
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=" + API_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city").strip()

        if not city:
            error_message = "Введите название города!"
        else:
            try:
                response = requests.get(API_URL.format(city))
                if response.status_code == 200:
                    data = response.json()
                    city_name = data["name"]
                    temperature = data["main"]["temp"]
                    weather_info = f"{city_name}: {temperature}°C"
                else:
                    error_message = "Город не найден!"
            except Exception as e:
                error_message = f"Ошибка: {str(e)}"

    return render_template("index.html", weather_info=weather_info, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
