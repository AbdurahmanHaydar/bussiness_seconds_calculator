from flask import Flask
from api_routes import all_routes

app = Flask(__name__)

all_routes(app)

if __name__ == '__main__':
    app.run()
