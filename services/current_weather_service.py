from models.location import Location
import httpx


async def get_current_weather(location: Location):

    url = f"https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}&units=metric"

    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    return data
