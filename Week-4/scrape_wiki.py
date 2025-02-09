from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
