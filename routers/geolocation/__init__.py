from flask import Blueprint, request

from routers.geolocation.use_case_geolocation import get_address_from_geolocation

geolocation_router = Blueprint('geolocation_router', __name__)


# ------------------------------------------------------------------
# Routers
# ------------------------------------------------------------------

@geolocation_router.route('/address/', methods=['GET'])
def route_get_country_flag_by_money_code():
    return get_address_from_geolocation(
        latitude=request.args.get('latitude', type=float),
        longitude=request.args.get('longitude', type=float)
    )
