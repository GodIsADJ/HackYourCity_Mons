from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


class LocationUnknownException(Exception):
    pass


def __do_geocode(address: str, attempt: int = 1, max_attempts: int = 5) -> object:
    geolocator = Nominatim(user_agent="Hackaton-Mons")
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return __do_geocode(address, attempt=attempt + 1)
        raise


def get_coordinates(address: str):
    location = __do_geocode(address)
    if location == None:
        return None
    else:
        return (location.latitude, location.longitude)  # , location.address)
