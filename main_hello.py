from fastapi import FastAPI, Path




weather = {
    "Newcastle" : {
        "temp": 24.5,
    }
}

app = FastAPI()


@app.get("/")
def home():
    return {"data": "Test"}

@app.get("/about")
def about():
    return {"data": "Test"}

@app.get("/get-weather/{location}")
def get_weather(location: str = Path(None, description="Location of interest")):
        return weather[location]

@app.get("/get-weather-at")
def get_weather_at(location: str=None):

        if location in weather:
            return weather[location]
        return {"Data": "Not Found"}