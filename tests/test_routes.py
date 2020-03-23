from flask import Flask
import json

from api_routes import all_routes


def test_base_route():
    app = Flask(__name__)
    all_routes(app)
    client = app.test_client()
    url = '/?start_time=2020-03-23T00:00:00&end_time=2020-03-27T00:00:00'

    response = client.get(url)
    assert response.get_data() == b'115200'

    assert response.status_code == 200
