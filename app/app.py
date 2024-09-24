import logging
import os
from flask import Flask
from routes.https_route import https_bp
from routes.scheduler_route import scheduler_bp

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(https_bp)
    app.register_blueprint(scheduler_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
