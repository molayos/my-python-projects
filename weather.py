from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__, template_folder='weather_templates')
GEOCODING_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_URL = 'https://api.open-meteo.com/v1/forecast'

# Weather code mapping to emoji (WMO Weather interpretation codes)
WEATHER_ICONS = {
    0: '☀️',      # Clear sky
    1: '🌤️',      # Mainly clear
    2: '⛅',      # Partly cloudy
    3: '☁️',      # Overcast
    45: '🌫️',     # Foggy
    48: '🌫️',     # Depositing rime fog
    51: '🌦️',     # Light drizzle
    53: '🌧️',     # Moderate drizzle
    55: '🌧️',     # Dense drizzle
    61: '🌦️',     # Slight rain
    63: '🌧️',     # Moderate rain
    65: '⛈️',     # Heavy rain
    71: '❄️',      # Slight snow
    73: '❄️',      # Moderate snow
    75: '❄️',      # Heavy snow
    80: '🌦️',     # Slight rain showers
    82: '🌧️',     # Moderate rain showers
    85: '❄️',      # Slight snow showers
    95: '⛈️',     # Thunderstorm
    96: '⛈️',     # Thunderstorm with slight hail
    99: '⛈️',     # Thunderstorm with heavy hail
}

def get_weather_icon(code):
    """Convert WMO weather code to emoji"""
    return WEATHER_ICONS.get(code, '🌡️')

def get_weather_description(code):
    """Convert WMO weather code to description"""
    descriptions = {
        0: 'Clear sky',
        1: 'Mainly clear',
        2: 'Partly cloudy',
        3: 'Overcast',
        45: 'Foggy',
        48: 'Depositing rime fog',
        51: 'Light drizzle',
        53: 'Moderate drizzle',
        55: 'Dense drizzle',
        61: 'Slight rain',
        63: 'Moderate rain',
        65: 'Heavy rain',
        71: 'Slight snow',
        73: 'Moderate snow',
        75: 'Heavy snow',
        80: 'Slight rain showers',
        82: 'Moderate rain showers',
        85: 'Slight snow showers',
        95: 'Thunderstorm',
        96: 'Thunderstorm with slight hail',
        99: 'Thunderstorm with heavy hail',
    }
    return descriptions.get(code, 'Unknown')

@app.route('/')
def home():
    """Render home page"""
    return render_template('base.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    """Fetch weather data for a city using Open-Meteo API"""
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({'error': 'Please enter a city name'}), 400
        
        # Step 1: Geocode city name to get coordinates
        geo_response = requests.get(GEOCODING_URL, params={
            'name': city,
            'count': 1,
            'language': 'en',
            'format': 'json'
        })
        
        geo_data = geo_response.json()
        
        if not geo_data.get('results') or len(geo_data['results']) == 0:
            return jsonify({'error': f'City "{city}" not found'}), 404
        
        location = geo_data['results'][0]
        lat = location['latitude']
        lon = location['longitude']
        city_name = location['name']
        country = location.get('country', '')
        
        # Step 2: Get weather data
        weather_response = requests.get(WEATHER_URL, params={
            'latitude': lat,
            'longitude': lon,
            'current': 'temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,pressure_msl',
            'daily': 'weather_code,temperature_2m_max,temperature_2m_min,relative_humidity_2m_max',
            'temperature_unit': 'fahrenheit',
            'wind_speed_unit': 'ms',
            'timezone': 'auto'
        })
        
        weather_data = weather_response.json()
        
        if weather_response.status_code != 200:
            return jsonify({'error': 'Unable to fetch weather data'}), 500
        
        # Parse current weather
        current = weather_data['current']
        current_weather = {
            'city': city_name,
            'country': country,
            'temperature': round(current['temperature_2m']),
            'feels_like': round(current['temperature_2m']),  # Open-Meteo doesn't provide feels_like, use actual temp
            'condition': get_weather_description(current['weather_code']),
            'description': get_weather_description(current['weather_code']),
            'humidity': current['relative_humidity_2m'],
            'wind_speed': round(current['wind_speed_10m'], 1),
            'pressure': round(current.get('pressure_msl', 0)),
            'icon': get_weather_icon(current['weather_code']),
            'icon_code': str(current['weather_code']),
        }
        
        # Parse 5-day forecast
        daily = weather_data['daily']
        forecast = []
        
        for i in range(min(5, len(daily['time']))):
            date = datetime.strptime(daily['time'][i], '%Y-%m-%d')
            forecast.append({
                'date': date.strftime('%a, %b %d'),
                'day_full': date.strftime('%A'),
                'temp_max': round(daily['temperature_2m_max'][i]),
                'temp_min': round(daily['temperature_2m_min'][i]),
                'condition': get_weather_description(daily['weather_code'][i]),
                'description': get_weather_description(daily['weather_code'][i]),
                'humidity': daily['relative_humidity_2m_max'][i],
                'wind_speed': 'N/A',  # Open-Meteo doesn't provide daily wind in free tier
                'icon': get_weather_icon(daily['weather_code'][i]),
                'icon_code': str(daily['weather_code'][i]),
            })
        
        return jsonify({
            'current': current_weather,
            'forecast': forecast,
            'success': True
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Network error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    print("\n🌤️  Weather App - Open-Meteo Edition")
    print("No API key required! Starting server...\n")
    app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
 #..replaced with above for render deployment   app.run(debug=True, host='0.0.0.0', port=5000)
