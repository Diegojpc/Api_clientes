from flask import Flask
from apps.controllers.cliente_controller import cliente_controller
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(cliente_controller)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
