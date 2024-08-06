import pprint
from http import HTTPStatus

import httpx
from flask import Response, Blueprint

astronauts_blueprint = Blueprint('astronauts', __name__)


@astronauts_blueprint.route("/get-astronauts")
def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    result = httpx.get(url=url, params={})

    if result.status_code not in (HTTPStatus.OK,):
        return Response("ERROR: Something went wrong with api.open-notify.org!",
                        status=result.status_code)

    result: dict = result.json()
    statistics = {}
    for entry in result.get('people', {}):
        # accumulating crafts count
        statistics[entry['craft']] = statistics.get(entry['craft'], 0) + 1

    pprint.pprint(result)
    return statistics
