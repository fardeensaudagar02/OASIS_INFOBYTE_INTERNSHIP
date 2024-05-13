import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.location_label = QLabel('Enter Location:')
        self.location_input = QLineEdit()
        self.location_input.returnPressed.connect(self.get_weather)
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.get_weather)
        self.weather_label = QLabel('')
        layout = QVBoxLayout()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.weather_label)
        self.setLayout(layout)

    def get_weather(self):
        location = self.location_input.text()
        if location:
            api_key = '0976d90cc30c21877e4f2497354bc822'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            response = requests.get(url)
            data = response.json()
            if data['cod'] == 200:
                weather_description = data['weather'][0]['description'].capitalize()
                temperature = data['main']['temp']
                wind_speed = data['wind']['speed']
                self.weather_label.setText(f'Weather of {location} is : {weather_description}\nTemperature of {location} is: {temperature}°C\nWind Speed of {location} is: {wind_speed} m/s')
            else:
                self.weather_label.setText('Error fetching weather data')
        else:
            self.weather_label.setText('Please enter a location')

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
