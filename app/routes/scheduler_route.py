from flask import Blueprint, request
import logging
from datetime import datetime

scheduler_bp = Blueprint('scheduler', __name__)

@scheduler_bp.route('/scheduler', methods=['POST'])
def scheduler_trigger():
    payload = request.get_json(silent=True) or {}
    timestamp = datetime.now().isoformat()
    logging.info(f"Scheduler triggered at {timestamp} with payload: {payload}")
    return {"message": "Scheduler executed", "timestamp": timestamp}, 200
