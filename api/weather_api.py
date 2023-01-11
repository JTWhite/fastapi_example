import fastapi
from models.location import Location
from api.jacket_weather import JacketWeather
from services.current_weather_service import get_current_weather

router = fastapi.APIRouter()


@router.get("/api/weather", response_model=JacketWeather)
async def get_weather(location: Location = fastapi.Depends()):

    data = await get_current_weather(location)

    weather = data.get("weather", {})
    category = weather.get("category", "Unknown")

    forecast = data.get("forecast", {})
    temp = forecast.get("temp", 0.0)

    waterproof = category.lower().strip() == "rain"
    jacket_needed = temp < 10

    jacket_type = JacketWeather(
        jacket_needed=jacket_needed, waterproof=waterproof
    )

    print(jacket_type)
    print(location)

    return jacket_type
