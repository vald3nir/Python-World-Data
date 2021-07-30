from flask import Blueprint

from routers.country_money.use_case_country_money import *

money_router = Blueprint('money_router', __name__)


# ------------------------------------------------------------------
# Routers
# ------------------------------------------------------------------

@money_router.route('/country_money', methods=['GET'])
def route_list_country_money_code():
    return list_country_money_code()


@money_router.route('/country_flag/<money_code>', methods=['GET'])
def route_get_country_flag_by_money_code(money_code):
    return get_country_flag_by_money_code(money_code)
