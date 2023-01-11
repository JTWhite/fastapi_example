from pydantic import BaseModel


class JacketWeather(BaseModel):

    jacket_needed: bool
    waterproof: bool
