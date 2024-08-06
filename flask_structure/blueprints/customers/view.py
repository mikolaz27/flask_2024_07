import random
import string

from flask import Blueprint
from webargs.flaskparser import use_kwargs

from ..common.database_handler import execute_query
from validators import password_length_config

customers_blueprint = Blueprint('customers', __name__)


@customers_blueprint.route("/generate-password")
@use_kwargs(
    password_length_config,
    location="query"
)
def generate_password(length):
    password_length = 10

    return "".join(
        random.choices(
            string.digits + string.ascii_letters + string.punctuation, k=password_length
        )
    )


@customers_blueprint.route('/')
def get_all_customers():
    query = "SELECT * FROM customers"

    data = execute_query(query=query)

    return data
