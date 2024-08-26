# WeatherDataFetcher class handles the fetching of weather data
class WeatherDataFetcher:
    def __init__(self):
        # Simulated data based on city
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_weather_data(self, city):
        # Check if the city is in the weather_data dictionary
        if city not in self.weather_data:
            raise ValueError(f"Error: '{city}' is not in the list of available cities.")
        # Fetch and return the weather data
        print(f"Fetching weather data for {city}...")
        return self.weather_data[city]

# DataParser class handles the parsing of weather data
class DataParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# UserInterface class handles user interaction
class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()
    def get_detailed_forecast(self, city):
        # Method to provide a detailed weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def display_weather(self, city):
        # Method to display the basic weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            try:
                detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
                if detailed == 'yes':
                    forecast = self.get_detailed_forecast(city)
                    print(forecast)
                else:
                    self.display_weather(city)
            except ValueError as e:
                print(e)

# Main function to start the application
def main():
    ui = UserInterface()
    ui.run()

if __name__ == "__main__":
    main()