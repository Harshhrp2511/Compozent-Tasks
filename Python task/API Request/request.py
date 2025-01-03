import requests

# Use the provided API key
api_key = "2f745fa85d563da5adb87b6cd4b81caf"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Extract specific weather information
    city_name = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Display the weather data
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Failed to get data. City not found or invalid API key.")
