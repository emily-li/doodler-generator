from flask import Flask
from flask_cors import CORS
from routes import setup_routes

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/api/v1/idea": {
            "origins": ["http://localhost:*", "https://emily-li.github.io"]
        }
    },
)

# Middleware can be added here

setup_routes(app)

if __name__ == "__main__":
    app.run()
