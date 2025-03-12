import httpx
from app.config import settings
from app.utils.exceptions import GoogleAPIException

GOOGLE_MAPS_API_KEY = settings.GOOGLE_MAPS_API_KEY
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
PLACES_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

async def get_address(lat: float, lon: float):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            GEOCODE_URL,
            params = {"latlng": f"{lat},{lon}", "key": GOOGLE_MAPS_API_KEY},
        )

    if response.status_code != 200:
        raise GoogleAPIException()
    
    data = response.json()
    if not data["results"]:
        return None
    
    return data["results"][0]["formatted_address"]

async def get_nearby_places(lat: float, lon: float, place_type: str = 'restaurant'):
    async with httpx.AsyncClient as client:
        response = await client.get(
            PLACES_URL,
            params = {
                "location": f"{lat},{lon}",
                "radius": 1000,
                "type": place_type,
                "key": GOOGLE_MAPS_API_KEY,
            },
        ) 

    if response != 200:
        raise GoogleAPIException()
    
    data = response.json()
    if not data["results"]:
        return []
    
    return [{"name": place["name"], "address": place.get("vicinity", "")} for place in data["results"]]