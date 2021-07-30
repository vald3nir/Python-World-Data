from geopy import Nominatim, Point

from routers import response_success, response_failed


def get_address_from_geolocation(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="script_python_geolocation")
        location = geolocator.reverse(
            query=Point(latitude, longitude),
            exactly_one=True,
            language="pt-br",
        )
        return response_success(location.raw)

    except Exception:
        return response_failed({"error": f"{latitude}, {longitude}"})
