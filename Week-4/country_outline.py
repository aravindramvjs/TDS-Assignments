from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'

@app.get("/api/outline")
def get_country_outline(country: str = Query(..., description="Name of the country")):
    # Format the Wikipedia URL
    wikipedia_url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    
    # Fetch the Wikipedia page
    response = requests.get(wikipedia_url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Country Wikipedia page not found")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract headings (H1 to H6)
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    
    # Generate Markdown outline
    markdown_outline = "## Contents\n\n"
    markdown_outline += f"# {country}\n\n"
    
    for heading in headings:
        level = int(heading.name[1])  # Get heading level from tag name (e.g., h2 -> 2)
        heading_text = heading.get_text(strip=True)
        markdown_outline += f"{'#' * level} {heading_text}\n\n"
    
    return {"outline": markdown_outline}

@app.get("/api/weather")
def get_shanghai_weather():
    required_city = "Shanghai"
    location_url = (
        'https://locator-service.api.bbci.co.uk/locations?' +
        urlencode({
            'api_key': API_KEY,
            's': required_city,
            'stack': 'aws',
            'locale': 'en',
            'filter': 'international',
            'place-types': 'settlement,airport,district',
            'order': 'importance',
            'a': 'true',
            'format': 'json'
        })
    )
    
    # Fetch the location data
    location_response = requests.get(location_url)
    if location_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Location data not found for Shanghai")
    
    location_data = location_response.json()
    if not location_data.get('locations'):
        raise HTTPException(status_code=404, detail="No locations found for Shanghai")
    
    # Extract locationId
    location_id = location_data['locations'][0]['id']
    
    # Fetch the weather data
    weather_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/daily/3day/{location_id}"
    weather_response = requests.get(weather_url)
    if weather_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Weather data not found for Shanghai")
    
    weather_data = weather_response.json()
    
    # Extract forecast information
    forecasts = weather_data.get('forecasts', [])
    weather_forecast = {}
    
    for forecast in forecasts:
        issue_date = forecast.get('date')
        description = forecast.get('detailed', {}).get('description')
        if issue_date and description:
            weather_forecast[issue_date] = description
    
    return weather_forecast

