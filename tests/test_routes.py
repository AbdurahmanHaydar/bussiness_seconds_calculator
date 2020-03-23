from flask import Flask
import json

from api_routes import all_routes


def test_base_route():
    app = Flask(__name__)
    all_routes(app)
    client = app.test_client()
    url = '/?start_time=2020-03-23T04:00:00&end_time=2020-03-25T00:00:00'

    response = client.get(url)
    assert response.get_data() == b'64800'

    assert response.status_code == 200

def test_base_weekend_and_hol():
    app = Flask(__name__)
    all_routes(app)
    client = app.test_client()
    url = '/?start_time=2020-12-25T09:00:00&end_time=2020-12-29T10:00:00'  # testing weekends and public holidays

    response = client.get(url)
    assert response.get_data() == b'39600'

    assert response.status_code == 200
