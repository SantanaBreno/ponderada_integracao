from fastapi import APIRouter, HTTPException, Query
from app.services.google_maps import get_address, get_nearby_places

router = APIRouter()

@router.get("/maps/location")
async def location(lat: float = Query(...),lon: float = Query(...)):
    address = await get_address(lat, lon)

    if not address:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    
    return {"address": address}


@router.get("/maps/nearby")
async def nearby(lat: float = Query(...), lon: float = Query(...), type: str = "restaurant"):
    
    places = await get_nearby_places(lat, lon, type)
    if not places:
        raise HTTPException(status_code=404, detail="Nenhum local encontrado")
    
    return {"places": places}

