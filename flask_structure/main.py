from flask import Flask, request, Response, jsonify
from blueprints.astronauts.view import astronauts_blueprint
from blueprints.customers.view import customers_blueprint

app = Flask(__name__)

app.register_blueprint(astronauts_blueprint, url_prefix='/astronauts')
app.register_blueprint(customers_blueprint,  url_prefix='/customers')

if __name__ == '__main__':
    app.run(
        port=5001
        , debug=True
    )
