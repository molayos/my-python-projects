# My Python Projects

A collection of web applications built with FastAPI and Flask.

## Projects

### 1. Calculator (FastAPI)
A modern web calculator with a beautiful UI that performs mathematical calculations safely.

**Features:**
- Clean, modern interface with gradient design
- Basic operations: addition, subtraction, multiplication, division
- Advanced math functions: sqrt, sin, cos, tan
- Support for mathematical constants (π, e)
- Direct expression input with Enter key support
- Real-time result calculation via REST API
- Error handling and validation

**Tech Stack:**
- FastAPI (Python web framework)
- Uvicorn (ASGI server)
- HTML/CSS/JavaScript (frontend)

**Run:**
```bash
python calculator.py
```
Then open http://localhost:8000 in your browser.

**API Endpoint:**
- `POST /api/calc` - Calculate expression
  ```json
  {
    "expression": "5 + 3 * 2"
  }
  ```

---

### 2. Weather App (Flask)
A weather application that displays current weather and 5-day forecasts for any city worldwide.

**Features:**
- City search functionality
- Current weather display:
  - Temperature (Fahrenheit)
  - Weather condition with emoji icons
  - Humidity percentage
  - Wind speed
  - Atmospheric pressure
- 5-day forecast with daily highs/lows
- Weather-specific emoji icons
- Mobile-responsive design
- Error handling for invalid cities
- **No API key required** - Uses free Open-Meteo API

**Tech Stack:**
- Flask (Python web framework)
- Open-Meteo API (free weather data)
- HTML/CSS/JavaScript (frontend)
- Requests library (HTTP client)

**Run:**
```bash
python weather.py
```
Then open http://localhost:5000 in your browser.

**API Endpoint:**
- `POST /weather` - Get weather data for a city
  ```json
  {
    "city": "London"
  }
  ```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone or navigate to the project:**
   ```bash
   cd c:\Users\molay\my-python-projects
   ```

2. **Create virtual environment (if not already created):**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Dependencies

See `requirements.txt` for all dependencies:
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI web server
- **Flask** - Lightweight web framework
- **Requests** - HTTP library for API calls

---

## Project Structure

```
my-python-projects/
├── calculator.py              # FastAPI calculator app
├── weather.py                 # Flask weather app
├── static/                    # Static files for calculator
│   └── index.html            # Calculator UI
├── weather_templates/         # Templates for weather app
│   └── base.html             # Weather app UI
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (if needed)
├── .venv/                    # Virtual environment
└── README.md                 # This file
```

---

## Usage

### Run Both Apps Simultaneously

You can run both apps on different ports:

**Terminal 1 - Calculator:**
```bash
python calculator.py
# Opens on http://localhost:8000
```

**Terminal 2 - Weather App:**
```bash
python weather.py
# Opens on http://localhost:5000
```

### Calculator Examples
- `5 + 3 * 2` = 11
- `sqrt(16)` = 4
- `sin(0)` = 0
- `pi * 2` = 6.28...

### Weather App Examples
- Search: "London" → Shows current weather + 5-day forecast
- Search: "Tokyo" → Works worldwide!
- Search: "New York" → Full weather details

---

## Features

### Calculator
✅ Safe expression evaluation  
✅ Mathematical functions  
✅ Real-time calculations  
✅ Responsive UI  
✅ REST API endpoint  

### Weather
✅ Worldwide city search  
✅ No API key required  
✅ Current weather display  
✅ 5-day forecast  
✅ Weather condition icons  
✅ Responsive design  
✅ Error handling  

---

## Troubleshooting

### "Port already in use"
If port 8000 or 5000 is already in use, modify the port in the app:
- Calculator: Change `port=8000` in `calculator.py`
- Weather: Change `port=5000` in `weather.py`

### "ModuleNotFoundError"
Ensure virtual environment is activated and dependencies installed:
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### "Template not found"
Ensure you're running the apps from the project root directory:
```bash
cd c:\Users\molay\my-python-projects
python weather.py
```

---

## License

These are personal projects. Feel free to modify and use as needed.

---

## Future Enhancements

**Calculator:**
- History of calculations
- Keyboard support (already partial)
- Dark mode theme
- Memory functions

**Weather:**
- Temperature unit toggle (Celsius/Fahrenheit)
- Saved favorite cities
- Weather alerts
- Hourly forecast
- Historical weather data

---

## Contact & Support

For issues or questions about these projects, refer to the code comments or review the implementation.
