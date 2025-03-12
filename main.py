from fastapi import FastAPI
from app.routers import maps

app = FastAPI(tile="Google Maps API Integration")

app.include_router(maps.router)

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port="8000")