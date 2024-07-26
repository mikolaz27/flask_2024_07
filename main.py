from flask import Flask

app = Flask(__name__)


@app.route("/admin")
def hello_world():
    return "<p>Hello, Mykhailo!dsadasds1111</p>"


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
        port=5000, debug=True
    )
