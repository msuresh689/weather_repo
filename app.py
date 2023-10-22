from flask import Flask, render_template as rt, request
import requests as req


app = Flask(__name__)

@app.route("/",)
def homepage():
    return rt('index.html')


@app.route('/weather_app', methods = ['POST', 'GET'])
def get_weather_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param ={
        'q': request.form.get('city'),
        'appid': request.form.get('appid'),
        'units': request.form.get('units')
    }
    response = req.get(url, params= param)
    data = response.json()
    return data



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5059)
    