import pprint
import random
import string
from http import HTTPStatus

import httpx
from flask import Flask, request, Response
from webargs.flaskparser import use_kwargs
from webargs import validate, fields

from validators import password_length_config

app = Flask(__name__)


@app.route("/admin")
def hello_world():
    return "<p>Hello, Mykhailo!dsadasds1111</p>"


@app.route("/generate-password")
@use_kwargs(
    password_length_config,
    location="query"
)
def generate_password(length):
    # password_length = request.args.get("length", '10')
    # max_limit = request.args.get("max_limit", '100')
    #
    # if not password_length.isdigit():
    #     return "ERROR: length should be a number!"
    #
    # password_length = int(password_length)
    #
    # if not 8 <= password_length <= 100:
    #     return "ERROR: password length should in range: [8, 100]"

    password_length = 10

    return "".join(
        random.choices(
            string.digits + string.ascii_letters + string.punctuation, k=password_length
        )
    )


@app.route("/get-astronauts")
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


# 100 - inform
# 200 - OK
# 300 - Redirect
# 400 - client error
# 500 - server error


# CamelCase - classes
# snake_case - all python code except classes
# kebab-case - for urls


# https://flask.palletsprojects.com:443/en/2.0.x/quickstart/
#
# category/food/apples/
# category/food/oranges/

# ? & : @ + ~ / # \

# https | http
# SSL

# r1 -> r2 -> r3 -> r4 -> r5 -> r6 -> r10

# flask.palletsprojects.com
# facebook.com -> 57.144.112.1

# DNS

# 443 - https
# 80 - http
# 5432 - postgres
# 587 - smtp
# 22 - ssh

# /quickstart


if __name__ == '__main__':
    app.run(
        port=5000
        # , debug=True
    )

# ll | grep 1
# cat file.txt | grep 1

# ll > example.txt

# tail -f example.txt


# POST
# body
# secure
# for changing on server

# GET
# in url
# insecure
# filtering, search, get data.
